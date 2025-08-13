/*
 *        Name: TARINDEX REXX
 *              create a CMS TAR "include file" (FILELIST format)
 *      Author: Rick Troth, Houston, Texas, USA 
 *        Date: 1992-Oct-01, 1993-Feb-01
 */
 
Parse Upper Arg fn ft fm fp . '(' .
Select
    When  fp ^= ""  Then  nop
    When  fn = '.'  Then  Do
        fn = '*';   ft = '*'
        fm = 'A';   fp = '.'
        End
    When  fm = '.'  Then  Do
        fm = 'A';   fp = '.'
        End
    Otherwise Do
        If  fn = "" Then fn = '*'
        If  ft = "" Then ft = '*'
        If  fm = "" Then fm = 'A'
        'CALLPIPE COMMAND QUERY DISK' fm '| DROP' ,
            '| SPEC 1.6 1 | STRIP | VAR FP'
        If rc ^= 0 Then Exit rc
        If  fp = '-' Then fp = '.'
        End  /*  Otherwise Do  */
    End  /*  Select  */
 
'ADDPIPE COMMAND LISTFILE' fn ft fm '(ALLOC ALLFILE NOHEADER | *.INPUT:'
If rc ^= 0 & rc ^= 28 Then , 
    'ADDPIPE COMMAND LISTFILE' fn ft fm '| *.INPUT:'
If rc ^= 0 & rc ^= 28 Then Exit rc
If rc = 28 Then Exit 0 
 
Parse Source . . arg0 .
 
uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lc = "abcdefghijklmnopqrstuvwxyz"
 
Do Forever
 
    'PEEKTO FILEID'
    If rc ^= 0 Then Leave
 
    Parse Var fileid _fn _ft _fm .
 
    If _fm = "DIR" Then Do
        'READTO'
        If rc ^= 0 Then Leave
        'CALLPIPE COMMAND ACCESS +' || _ft || '.' || _fn _ft
        If rc ^= 0 Then Iterate
        _fp = Translate(fp || '/' || _fn, lc, uc)
        'OUTPUT' "*!mkdir" _fp
        'CALLPIPE' arg0 '* *' _ft _fp '| *:'
        'CALLPIPE COMMAND ACCESS -' || _ft _ft
        Iterate
        End  /*  If  ..  Do  */
 
    'OUTPUT' "     " _fn _ft _fm ,
        Translate(fp || '/' || _fn || '.' || _ft, lc, uc)
    If rc ^= 0 Then Leave
 
    'READTO'
    If rc ^= 0 Then Leave
 
    End  /*  Do  While  */
 
Exit rc * (rc ^= 12)
 
 
