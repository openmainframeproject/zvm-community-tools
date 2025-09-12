/*
 *        Name: USERLIST REXX
 *              generates a list of users from nickname input
 *      Author: Rick Troth, Houston, Texas, USA
 *        Date: 1992-Oct-02, Dec-09
 *
 *        Note: this does not presently support the TCPADDR hack
 */
 
Parse Arg list '(' opts
Parse Source . . arg0 .
 
If list ^= "" Then 'CALLPIPE VAR LIST |' arg0 '| *:'
 
'ADDPIPE *: | CHANGE /@/ AT / | SPLIT | *.INPUT:'
 
Do Forever
 
    'READTO USER'
    If rc ^= 0 Then Leave
    If user = "" Then Iterate
 
    'PEEKTO AT'; Upper at
    If rc = 0 & at = "AT" Then Do
        'READTO'
        'READTO HOST'
        If rc ^= 0 | host = "" Then 'OUTPUT' user
                               Else 'OUTPUT' user || '@' || host
        End  /*  If  ..  Do  */
    Else Do
        nick = user
        'CALLPIPE CMS NAMEFIND :NICK' nick ':USERID :NODE :LIST' ,
            '| VAR USER | DROP | VAR HOST | DROP | VAR LIST'
        If rc = 0 Then Do
            If host = "" Then 'OUTPUT' user
                         Else 'OUTPUT' user || '@' || host
            If list ^= "" Then 'CALLPIPE VAR LIST |' arg0 '| *:'
            End  /*  If  ..  Do  */
        Else 'OUTPUT' nick
        End  /*  Else  Do  */
 
    End  /*  Do  Forever  */
 
Exit rc * (rc ^= 12)
 
