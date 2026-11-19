/*
 *        Name: MAILCONVERT REXX
 *              tool to convert CMS NOTEBOOKs to/from UNIX "mbox" files
 *      Author: Rick Troth, Houston, Texas, USA 
 *        Date: 1993-May-21
 */
 
Parse Upper Arg fn to sy . '(' . ')' .
If fn = "" Then Do
    Address "COMMAND" 'XMITMSG 386 (ERRMSG CALLER MCV'
    Exit 24
    End  /*  If  ..  Do  */
If to ^= "TO" & to ^= "FROM" Then Do
    Address "COMMAND" 'XMITMSG 29 TO (ERRMSG CALLER MCV'
    Exit 24
    End  /*  If  ..  Do  */
If sy ^= "CMS" & sy ^= "UNIX" & sy ^= "VM" Then Do
    Address "COMMAND" 'XMITMSG 29 SY (ERRMSG CALLER MCV'
    Exit 24
    End  /*  If  ..  Do  */
 
If to = "TO"   & sy = "CMS"  Then Signal TO_CMS
If to = "FROM" & sy = "CMS"  Then Signal TO_UNIX
If to = "TO"   & sy = "UNIX" Then Signal TO_UNIX
If to = "FROM" & sy = "UNIX" Then Signal TO_CMS
If to = "TO"   & sy = "VM"   Then Signal TO_CMS
If to = "FROM" & sy = "VM"   Then Signal TO_UNIX
 
Exit 24
 
/* -------------------------------------------------------------- TO_CMS
 */
TO_CMS:
 
If fn ^= '-' Then Do
    'ADDPIPE <' fn 'MBOX | *.INPUT:'
    If rc ^= 0 Then Exit rc
    'ADDPIPE *.OUTPUT: | >' fn 'NOTEBOOK A'
    If rc ^= 0 Then Exit rc
    End  /*  If  ..  Do  */
 
'ADDPIPE *.INPUT: | DEBLOCK LINEND 0A | A2E | PAD 1 | *.INPUT:'
If rc ^= 0 Then Exit rc
 
Do Forever
 
    'PEEKTO LINE'
    If rc ^= 0 Then Leave
 
/*  Parse Upper Var line from orig day mon dd time year .             */
    If Left(line,5) = "From " Then 'OUTPUT' Copies('=',72)
    Else Do
        Do While Length(line) > 80
            'OUTPUT' Left(line,80)
            line = " " || Substr(line,81)
            End  /*  Do  While  */
        'OUTPUT' line
        End  /*  Else  Do  */
    If rc ^= 0 Then Leave
 
    'READTO'
 
    End  /*  Do  Forever  */
 
Exit rc * (rc ^= 12)
 
/* ------------------------------------------------------------- TO_UNIX
 */
TO_UNIX:
 
If fn ^= '-' Then Do
    'ADDPIPE <' fn 'NOTEBOOK | *.INPUT:'
    If rc ^= 0 Then Exit rc
    'ADDPIPE *.OUTPUT: | >' fn 'MBOX A'
    If rc ^= 0 Then Exit rc
    End  /*  If  ..  Do  */
 
'ADDPIPE *.OUTPUT: | E2A | FBLOCK 4094 | *.OUTPUT:'
If rc ^= 0 Then Exit rc
 
Do Forever
 
    'READTO RECORD'
    If rc ^= 0 Then Leave
    Parse Var record . i .
    If Datatype(i,'N') Then i = Trunc(i)
                       Else i = 0
 
    user = Userid()
    day  = Left(Date('W'),3)
    mon  = Left(Date('M'),3)
/*  dd   = Word(Date('N'),1)  */
    time = Time()
    Parse Value Date('N') With dd . year .
 
    j = 0
    Do Forever
        'READTO RECORD'
        If rc ^= 0 Then Leave
        If Strip(Translate(record,,'05'x)) = "" Then Leave
        j = j + 1
        head.j = record
        Parse Var record tag val
        /* ----------------------------------- */
        /*  crunch header to modify FROM line  */
        /* ----------------------------------- */
        End
    head.0 = j
 
    'OUTPUT' "From" user day mon dd time year || '25'x
    'CALLPIPE STEM HEAD. | SPEC 1-* 1 x25 NEXT | *:'
    'OUTPUT' '25'x      /*  and NO spaces!  */
                        /*  because some UNIX MUAs are picky  */
 
    i = i - j - 1
    If i > 0 Then 'CALLPIPE *: | TAKE' i ,
                        '| SPEC 1-* 1 x25 NEXT | *:'
    'CALLPIPE *: | TOLABEL' Copies('=',72) || ,
                        '| SPEC 1-* 1 x25 NEXT | *:'
 
    'PEEKTO'
    If rc ^= 0 Then Leave
 
    End
 
Exit rc * (rc ^= 12)
 
