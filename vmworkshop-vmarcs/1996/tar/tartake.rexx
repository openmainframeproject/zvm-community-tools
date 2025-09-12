/*
 *        Name: TARTAKE REXX
 *              pass an exact number of bytes
 *              while consuming an integral number of 512-byte records.
 *              Copyright 1993, Richard M. Troth
 */
 
Parse Arg size . '(' . ')' .
If ^Datatype(size,'N') Then Exit
If size = 0 Then Exit
 
full = size % 512
'CALLPIPE *: | TAKE' full '| *:'
If rc ^= 0 Then Exit rc
 
part = size // 512
If part = 0 Then Exit
'PEEKTO RECORD'
'OUTPUT' Left(record,part)
'READTO'
If rc ^= 0 Then Exit rc
 
Exit
 
 
