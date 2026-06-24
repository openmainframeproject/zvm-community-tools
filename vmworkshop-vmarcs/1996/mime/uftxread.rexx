/*
 *        Name: UFTXREAD REXX
 *              Pipelines stage to interpret SIFT/UFT jobs
 *              as extracted from the mailbox
 *      Author: Rick Troth, Rice University, Information Systems
 *        Date: 1993-Apr-07 and prior
 */
 
pipe = ""
name = "mime.text"
 
Do Forever
 
    'PEEKTO LINE'
    If rc ^= 0 Then Leave
 
    Parse Upper Var line cmnd .
    Select  /*  cmnd  */
        When  cmnd = "FILE"     Then Parse Var line . size from .
        When  cmnd = "SIZE"     Then Parse Var line . size .
        When  cmnd = "USER"     Then nop
        When  cmnd = "DATE"     Then nop
        When  cmnd = "TYPE"     Then Do
            Parse Var line . type .
            Select  /*  type  */
                When type = "A" Then pipe = ,
                    'CHANGE /' || '0D0A'x || '/' || '0A'x || '/' ,
                        '| DEBLOCK LINEND 0A | DROP LAST | A2E'
                When type = "E" Then pipe = 'DEBLOCK LINEND 15 | DROP'
                When type = "V" Then pipe = 'DEBLOCK CMS'
                When type = "N" Then pipe = 'DEBLOCK NETDATA' ,
                    '| LOCATE' '00C000'x '| SPEC 2-* 1'
                Otherwise pipe = 'FBLOCK 80' /* binary */
                End  /*  Select  code  */
            End  /*  When  ..  Do  */
        When  cmnd = "NAME"     Then Parse Var line . name
 
        When  cmnd = "CLASS"    Then Parse Var line . class .
        When  cmnd = "FORM"     Then Parse Var line . form .
        When  cmnd = "DEST"     Then Parse Var line . dest .
        When  cmnd = "DIST"     Then Parse Var line . dist .
        When  cmnd = "FCB"      Then Parse Var line . fcb .
        When  cmnd = "CTAPE"    Then Parse Var line . fcb .
        When  cmnd = "UCS"      Then Parse Var line . ucs .
        When  cmnd = "CHARS"    Then Parse Var line . ucs .
        When  cmnd = "TRAIN"    Then Parse Var line . ucs .
 
        When  cmnd = "DATA"     Then Leave
        Otherwise Say "command/parameter" cmnd "ignored"
        End  /*  Select  cmnd  */
 
    'READTO'
 
    End  /*  Do  While  */
 
If rc ^= 0 Then Exit rc * (rc ^= 12)
 
'READTO'
 
If pipe = "" Then 'CALLPIPE *: | > UFTXREAD CMSUT1 A3'
             Else 'CALLPIPE *: |' pipe '| > UFTXREAD CMSUT1 A3'
 
If Index(name,'"') > 0 Then
    Parse Var name . '"' name '"' .
Parse Var name fn '.' ft '.' .
If fn = "" Then Parse Var from fn '.' . '@' .
Push "COMMAND SET FN" fn
Push "COMMAND SET FT" ft
Push "COMMAND SET FM A1"
Address "COMMAND" 'XEDIT UFTXREAD CMSUT1 A3'
 
Return rc
 
