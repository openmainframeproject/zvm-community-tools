/* © Copyright 1995, Richard M. Troth, all rights reserved.  <plaintext>
 *
 *        Name: TARPUNCH REXX
 *              "punch" a tar "deck" to another user
 *              Copyright 1992, 1995, Richard M. Troth
 */
 
Parse Arg target . '(' . ')' .
 
/*  if target is a dash,  feed to punch w/o closing  */ 
If target = '-' Then Do 
    'CALLPIPE *.INPUT: | FBLOCK 80 00 | PUNCH'
    Exit rc 
    End  /*  If .. Do  */ 
 
/*  okay,  so we really want to send this  */ 
'CALLPIPE COMMAND IDENTIFY | VAR IDENTITY'
Parse Var identity userid . hostid . rscsid . '15'x .
Parse Var target user '@' host
If user = "" Then user = userid
If host = "" Then host = hostid
 
/*  careful!  this is a raw SIFT/UFT job  */ 
Address "COMMAND" 'STATE UFTCHOST REXX *'
If rc = 0 Then Do
    'ADDPIPE *.OUTPUT: | UFTCHOST' host '(TYPE I | *.OUTPUT:'
    'CALLPIPE VAR USERID | XLATE LOWER | VAR USERID'
    'OUTPUT FILE 0' userid '-' 
/*  'OUTPUT USER' user || '@' || host  */ 
    'OUTPUT USER' user 
    'OUTPUT TYPE I'
    'OUTPUT DATA'
/*  'SHORT'  */ 
    'CALLPIPE *: | *:' 
    End  /*  If  ..  Do  */
 
/*  that didn't work,  so punt to RSCS  */ 
Else Do
    Address "COMMAND" 'GETFMADR'
    If rc ^= 0 Then Exit rc
    Parse Pull . . tmp .
    'CALLPIPE CP DEFINE PUNCH' tmp
    'CALLPIPE CP TAG DEV' tmp host user '50'
    'CALLPIPE CP SPOOL' tmp 'TO' rscsid
    'CALLPIPE *.INPUT: | FBLOCK 80 00 | SPEC x41 1 1-* NEXT | URO' tmp
    'CALLPIPE CP DETACH' tmp
    End  /*  Else  Do  */
 
Exit
 
