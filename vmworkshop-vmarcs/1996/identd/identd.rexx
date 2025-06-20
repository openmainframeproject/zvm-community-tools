/* © Copyright 1995, Richard M. Troth, all rights reserved.  <plaintext>
 *
 *        Name: IDENTD REXX
 *              IDENT/TAP (RFC 1413) server for VM/CMS pipeline stage
 *      Author: Rick Troth, Houston, Texas, USA
 *        Date: 1994-Oct-15
 *     Version: 1.1.1, aka (V1) R1 M1, or just "1.1"
 */
 
/*  read the IDENT request  */
'PEEKTO LINE'
If rc ^= 0 Then Exit rc
 
Parse Var line lsoc ',' fsoc ',' . ':' .
If ^Datatype(lsoc,'W') | ^Datatype(fsoc,'W') Then Do
    Say argo "0 , 0 : ERROR : INVALID-PORT"
    'OUTPUT' "0 , 0 : ERROR : INVALID-PORT"
    Exit
    End  /*  If .. Do  */
 
/*  attach NETSTAT now, in case it someday runs asynch  */
'ADDPIPE COMMAND NETSTAT | NLOCATE /*/ | *.INPUT:'
 
/*  crunch CMS' equivalent of /etc/services  */
'CALLPIPE < ETC SERVICES | NLOCATE 1.1 /#/' ,
    '| XLATE UPPER | STEM SERVICES.'
Do i = 1 to services.0
    Parse Var services.i name numb .
    Parse Var numb numb '/' .
    service.name = numb
    End
 
/*  read that NETSTAT output, looking for a match  */
Do Forever
 
    'PEEKTO LINE'
    If rc ^= 0 Then Leave
 
    Parse Var line user conn lsok fsok stat .
    Parse Var lsok . '..' lsok
    If ^Datatype(lsok,'W') Then lsok = service.lsok
    Parse Var fsok . '..' fsok
    If ^Datatype(fsok,'W') Then fsok = service.fsok
 
    If lsok = lsoc & fsok = fsoc Then Do
        Say argo lsok ',' fsok ': USERID : CMS :' user
        'OUTPUT' lsok ',' fsok ': USERID : CMS :' user
        Exit
        End  /*  If .. Do  */
 
    'READTO'
    If rc ^= 0 Then Leave
 
    End  /*  Do Forever  */
 
Say argo lsoc ',' fsoc ": ERROR : NO-USER"
'OUTPUT' lsoc ',' fsoc ": ERROR : NO-USER"
 
Exit
 
