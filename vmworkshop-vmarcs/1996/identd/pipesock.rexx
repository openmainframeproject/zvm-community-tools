/* © Copyright 1994, Richard M. Troth, all rights reserved.  <plaintext>
 *
 *        Name: PIPESOCKET REXX
 *              until the day when there's a true asynch SOCKET stage
 *      Author: Rick Troth, Rice University, Information Systems
 *        Date: 1993-Feb-23, Aug-25
 */
 
Parse Source . . . . . arg0 .
argo = arg0 || ':'
 
'ADDSTREAM OUTPUT STAT'
'ADDPIPE *.OUTPUT.STAT: | SPEC /' || argo || ' / 1 1-* NEXT | CONSOLE'
 
Parse Upper Arg func sock opts
 
Select  /*  func  */
    When Abbrev("READ",func,1)     Then Signal READ
    When Abbrev("WRITE",func,1)    Then Signal WRITE
    Otherwise Do
        Address "COMMAND" 'XMITMSG 3 FUNC (CALLER SOX ERRMSG'
        Exit 24
        End  /*  Otherwise  Do  */
    End  /*  Select  func  */
 
/* ---------------------------------------------------------------- READ
 *  Send packets from the socket to the output stream.
 */
READ:
 
If Index(opts,"WAIT") > 0 Then Do
    Say Socket('Ioctl', sock, 'FIONBIO')
    End  /*  If  ..  Do  */
 
'CALLPIPE *: | *:'              /*  allow follow-through  */
 
'OUTPUT'        /*  this is e-ssential to binary mode!  */
 
Do Forever
 
    Parse Value Socket("READ", sock, 61440) With rc bc data
    If rc ^= 0 Then If bc ^= "EWOULDBLOCK" Then Do
        tcprc = rc
        'CALLPIPE LITERAL' tcperror() '| *.OUTPUT.STAT:'
        If rc ^= 0 Then Say argo tcperror()
        rc = tcprc
        Leave
        End  /*  If  ..  Do  */
    If bc < 1 Then Leave
 
    'OUTPUT' data
    If rc ^= 0 Then Leave
 
    End  /*  Do  Forever  */
 
Exit rc * (rc ^= 12)
 
 
/* --------------------------------------------------------------- WRITE
 *  Send records from the input stream to the socket.
 */
WRITE:
 
Do Forever
 
    'PEEKTO DATA'
    If rc ^= 0 Then Leave
 
    Parse Value Socket("WRITE", sock, data) With rc bc .
    If rc ^= 0 Then Do
        tcprc = rc
        'CALLPIPE LITERAL' tcperror() '| *.OUTPUT.STAT:'
        If rc ^= 0 Then Say argo tcperror()
        Exit tcprc
        End  /*  If  ..  Do  */
 
    'OUTPUT' data       /*  allow follow-through  */
    'READTO'
 
    End  /*  Do  Forever  */
 
Exit rc * (rc ^= 12)
 
