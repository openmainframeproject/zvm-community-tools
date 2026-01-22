/* © Copyright 1995, Richard M. Troth, all rights reserved.  <plaintext>
 *
 *        Name: TELL REXX
 *              send interactive messages to other users
 *      Author: Rick Troth, Houston, Texas, USA
 *              Rick Troth, Houston, Texas, USA
 *        Date: 1993-Feb-24, and prior, 1993-Aug-27
 *              1995-May-02
 */
 
Parse Arg userlist
'CALLPIPE VAR USERLIST | USERLIST | STEM USER.'
 
'CALLPIPE COMMAND IDENTIFY | VAR IDENTITY'
Parse Var identity userid . nodeid . rscsid .
'CALLPIPE VAR USERID | XLATE LOWER | VAR LOCALUSER'
localhost = hostname()
 
Parse Value diag(08,'QUERY VIRTUAL CONSOLE') ,
    With . vaddr on type raddr term start . '15'x .
If on = "DISCONNECTED" Then localterm = "Not connected"
                       Else localterm = raddr
 
'CALLPIPE COMMAND GLOBALV SELECT' "$" || Userid() ,
    'LIST TELL | DROP | VAR OPTIONS'
Parse Var options . "MSGCMD" msg .
If msg = "" Then msg = "MSG"
 
/* ---------------------------------------------------------------- TELL
 */
Do Forever
 
    'PEEKTO MESSAGE'
    If rc ^= 0 Then Leave
    If Strip(message) = "." Then Leave
 
    Do i = 1 to user.0
        Parse Var user.i user '@' node
        If user = "" Then Iterate
        Select  /*  node  */
            When node = "" Then Do
                Upper user
                Parse Value Diagrc(08, msg user message) ,
                    With 1 rc 10 . 17 rs '15'x .
                If rc ^= 0 & rs ^= "" Then 'OUTPUT' rs
                End  /*  When  ..  Do  */
            When Index(node,'.') = 0 Then Do
                If user = '*' Then user = userid
                If node = '*' Then node = nodeid
                Upper user node
                Parse Value Diagrc(08,'SMSG' rscsid 'MSG' ,
                    node user message) With 1 rc 10 . 17 rs '15'x .
                If rc ^= 0 & node = nodeid Then
                    Parse Value Diagrc(08, msg user message) ,
                        With 1 rc 10 . 17 rs '15'x .
                If rc ^= 0 & rs ^= "" Then 'OUTPUT' rs
                End  /*  When  ..  Do  */
            Otherwise Do
                If user = '*' Then user = localuser
                If node = '*' Then node = localhost
                Call VIA_MSGD user, node, message
                End  /*  Otherwise  Do  */
            End  /*  Select  node  */
        End  /*  Do  For  */
 
    'READTO'
 
    End  /*  Do  Forever  */
 
Exit rc * (rc ^= 12)
 
 
 
/* ------------------------------------------------------------ VIA_MSGD
 */
VIA_MSGD: Procedure Expose localuser localterm
Parse Arg user, host, text
ver = 'B'
term = '*'
port = 18
 
/*
 *  Verify REXX/Sockets (RXSOCKET version 2).
 */
Parse Value Socket("VERSION") With rc . rv .
v1 = (rv < 2)
 
/*
 *  Initialize RXSOCKET
 */
If v1 Then Do
    maxdesc = Socket('Initialize', 'MessageC')
    If maxdesc = "-1" Then Do
        If errno ^= "ESUBTASKALREADYACTIVE" Then Do
            Say tcperror()
            Return -1
            End  /*  If  ..  Do  */
        rc = Socket('Terminate')
        maxdesc = Socket('Initialize', 'MessageC')
        End  /*  If  ..  Do  */
    If maxdesc = "-1" Then Do
        Say tcperror()
        Return -1
        End  /*  If  ..  Do  */
    End  /*  If  ..  Do  */
 
Else Do
    Parse Value Socket("INITIALIZE", "MessageC") With rc errno maxdesc .
    If rc ^= 0 Then Do
        If errno ^= "ESUBTASKALREADYACTIVE" Then Do
            Say tcperror()
            Return rc
            End  /*  If  ..  Do  */
        Parse Value Socket("TERMINATE") With rc .
        Parse Value Socket("INITIALIZE", "MessageC") With rc . maxdesc .
        If rc ^= 0 Then Do
            Say tcperror()
            Return rc
            End  /*  If  ..  Do  */
        End  /*  If  ..  Do  */
    End  /*  Else  Do  */
 
/*
 *  Get a socket descriptor (TCP protocol)
 */
If v1 Then Do
    socket = Socket('Socket', 'AF_INET', 'Sock_Stream')
    If socket = "-1" Then Return -1
    End  /*  If  ..  Do  */
 
Else Do
    Parse Value Socket("SOCKET", "AF_INET", "SOCK_STREAM") ,
        With rc socket .
    If rc ^= 0 Then Do
        Say tcperror()
        Parse Value Socket("TERMINATE") With rc .
        Return rc
        End  /*  If  ..  Do  */
    End  /*  Else  Do  */
 
/*
 *  Enable ASCII<->EBCDIC translation option
 */
If v1 Then Do
    rc = Socket('SetSockOpt', socket, 'SOL_SOCKET', 'SO_EBCDIC', 1)
    If rc = "-1" Then Return -1
    End  /*  If  ..  Do  */
 
Else Do
    Parse Value Socket("SETSOCKOPT", socket, "SOL_SOCKET", ,
        "SO_ASCII", "ON") With rc .
    If rc ^= 0 Then Do
        Say tcperror()
        Parse Value Socket("CLOSE", socket) With rc .
        Parse Value Socket("TERMINATE") With rc .
        Return rc
        End  /*  If  ..  Do  */
    End  /*  Else  Do  */
 
/*
 *  Figure out the target host address
 */
If v1 Then Do
    Parse Var host h1 '.' h2 '.' h3 '.' h4 '.' .
    If  Datatype(h1,'N') &,
        Datatype(h2,'N') &,
        Datatype(h3,'N') &,
        Datatype(h4,'N')    Then
        hisaddr = d2c(h1) || d2c(h2) || d2c(h3) || d2c(h4)
    Else Do
        hisaddr = Socket('GetHostByName', host)
        If hisaddr = "-1" Then Return -1
        End  /*  Else  Do  */
    End  /*  If  ..  Do  */
 
Else Do
    Parse Value Socket("RESOLVE", host) With rc hisaddr hisname .
    If rc ^= 0 Then Do
        Say tcperror()
        Parse Value Socket("CLOSE", socket) With rc .
        Parse Value Socket("TERMINATE") With rc .
        Return rc
        End  /*  If  ..  Do  */
    End  /*  Else  Do  */
 
/*
 *  Connect to the MessageD server.
 */
If v1 Then Do
    rc = Socket('Connect', socket, AF_INET || Htons(port) || hisaddr)
    If rc = "-1" Then Return -1
    End  /*  If  ..  Do  */
 
Else Do
    Parse Value Socket("CONNECT", socket, "AF_INET" port hisaddr) ,
        With rc .
    If rc ^= 0 Then Do
        Say tcperror()
        Parse Value Socket("CLOSE", socket) With .
        Parse Value Socket("TERMINATE") With .
        Return rc
        End  /*  If  ..  Do  */
    End  /*  Else  Do  */
 
/*
 *  Compose the message packet.
 */
data = ver || user || '00'x || term || '00'x || text || '00'x || ,
              localuser || '00'x || localterm || '00'x || ,
              Time('S') || '00'x || "?" '00'x
 
/*
 *  Send the message.
 */
If v1 Then Do
    bc = Socket('Write', socket, data)
    If bc = "-1" Then Return -1
    End  /*  If  ..  Do  */
 
Else Do
    Parse Value Socket("WRITE", socket, data) With rc bc .
    If rc ^= 0 Then Do
        Say tcperror()
        Parse Value Socket("CLOSE", socket) With rc .
        Parse Value Socket("TERMINATE") With rc .
        Return rc
        End  /*  If  ..  Do  */
    End  /*  Else  Do  */
 
/*
 *  Recover some response  (if available).
 */
If v1 Then Do
    bc = Socket('Read', socket, 'DATA')
    If bc = "-1" Then Return -1
    End  /*  If  ..  Do  */
 
Else Do
    Parse Value Socket("READ", socket) With rc bc data
    If rc ^= 0 Then Do
        Say tcperror()
        Parse Value Socket("CLOSE", socket) With rc .
        Parse Value Socket("TERMINATE") With rc .
        Return rc
        End  /*  If  ..  Do  */
    End  /*  Else  Do  */
 
/*
 *  Display the response  (if any).
 */
If bc > 0 Then
    If Left(data,1) ^= '+' Then Do
        If Left(data,1) = '-' Then data = Substr(data,2)
        Parse Var data data '00'x .
        'CALLPIPE VAR DATA | STRIP BOTH 25' ,
            '| XLATE *-* 25 15 | VAR DATA'
        Say data
        End  /*  If  ..  Do  */
 
/*
 *  All done, relinquish our socket descriptor
 */
Parse Value Socket("CLOSE", socket) With rc .
If rc ^= 0 Then Do
    Say tcperror()
    Parse Value Socket("TERMINATE") With .
    Return rc
    End  /*  If  ..  Do  */
 
/*
 *  Tell REXX/Sockets that we are done with this IUCV path.
 */
Parse Value Socket("TERMINATE") With rc .
If rc ^= 0 Then Do
    Say tcperror()
    Return rc
    End  /*  If  ..  Do  */
 
Return 0
 
