/*
 *        Name: TARREADC REXX
 *              read a tar "deck" in the reader
 *              Copyright 1992, Richard M. Troth
 */
 
rdr = "00C"
 
Parse Arg tf . '(' . ')' .
 
'CALLPIPE CP QUERY VIRTUAL' rdr '| VAR READER'
Parse Var reader . . . . . hold . '15'x .
'CALLPIPE CP SPOOL' rdr 'HOLD'
'CALLPIPE CP CLOSE' rdr
 
If tf ^= "-" Then Do
    'CALLPIPE CP ORDER READER' tf '| VAR RS'
    If rc ^= 0 Then Do
        orc = rc
        'OUTPUT' rs
        'CALLPIPE CP SPOOL' rdr hold
        Exit orc
        End  /*  If  ..  Do  */
    End  /*  If  ..  Do  */
 
'CALLPIPE READER' rdr ,
    '| NLOCATE 1-1 /' || '03'x || '/' ,
        '| SPEC 2-* 1 | PAD 80 40 | *:'
 
'CALLPIPE CP CLOSE' rdr
'CALLPIPE CP SPOOL' rdr hold
 
Exit
 
 
