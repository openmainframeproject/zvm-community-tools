/* © Copyright 1992, 1995, Richard M. Troth, all rights reserved. 
 *		(casita sourced) <plaintext>
 *
 *        Name: TAR REXX
 *              a from-scratch replacement for CMS 'tar' v1 
 *	Author: Rick Troth, Houston, Texas, USA 
 */
 
vrm = "2.3.0" 
 
dfmt = 'U'              /* date format used by LISTFILE */
tzoh = -6               /* timezone offset in hours */
tzoh = tzoffset('H') 
tzos = tzoh * 60 * 60   /* timezone offset in seconds */
tzos = tzoffset('S') 
 
/* ASCII non-printables */ 
a_nprint = '00010203040506FF'x 
/* EBCDIC non-printables */ 
e_nprint = '0001020304FF'x 
 
Parse Arg cmd args '(' opts ')' .
Upper cmd opts
Parse Source . . . . . arg0 .
argo = arg0 || ':'
 
tc = ""     /*  primary operation  (tar command)  */
tf = ""     /*  archive file  (tar file)  */
td = ""     /*  archive device  (disk, tape, or SPOOL)  */
 
verbose = 0;    modtime = 1;    prompt = 0 
include = "";   tarlist = 0;    skip = 0 
peek = 0;       once = 0;       replace = 0 
 
Do While cmd ^= ""
    Parse Var cmd 1 c 2 cmd
    Select  /*  c  */
        When c = '-' Then nop
        When c = 'C' Then Do
            If tc ^= "" Then Do
                Address "COMMAND" 'XMITMSG 66 TC C (ERRMSG'
                Say argo "multiple primary operations."
                Exit 24
                End  /*  If  ..  Do  */
            tc = c
            End  /*  When  Do  */
        When c = 'X' Then Do
            If tc ^= "" Then Do
                Say argo "multiple primary operations."
                Exit 24
                End  /*  If  ..  Do  */
            tc = c
            End  /*  When  Do  */
        When c = 'T' Then Do
            If tc ^= "" Then Do
                Say argo "multiple primary operations."
                Exit 24
                End  /*  If  ..  Do  */
            tc = c
            End  /*  When  Do  */
        When c = 'R' Then Do
            If tc ^= "" Then Do
                Say argo "multiple primary operations."
                Exit 24
                End  /*  If  ..  Do  */
            tc = c
            End  /*  When  Do  */
        When c = 'F' Then Do
            If tf ^= "" Then Do
                Say argo "multiple archives specified."
                Exit 24
                End  /*  If  ..  Do  */
            Parse Var args tf args
            td = 'F'
            End  /*  When  Do  */
        When c = 'S' Then Do
            If tf ^= "" Then Do
                Say argo "multiple archives specified."
                Exit 24
                End  /*  If  ..  Do  */
            Parse Var args tf args
            td = 'S'
            End  /*  When  Do  */
        When c = '0' | c = '1' | c = '2' | c = '3' ,
             c = '4' | c = '5' | c = '6' | c = '7' Then Do
            If tf ^= "" Then Do
                Say argo "multiple archives specified."
                Exit 24
                End  /*  If  ..  Do  */
            tf = "TAP" || c
            td = 'T'
            End  /*  When  Do  */
        When c = 'V' Then Do
            verbose = 1
            Say "CMS TAR - Version" vrm "(piped)"
            End  /*  When  Do  */
        When c = 'M' Then modtime = 0
        When c = 'W' Then prompt = 1
        Otherwise Do
            Address "COMMAND" 'XMITMSG 3 C (ERRMSG'
            Say argo "unrecognized command token" c
            Exit 24
            End  /*  Otherwise  Do  */
        End  /*  Select  c  */
    End
 
If tf = "" Then tf = "TAP1"
If td = "" Then td = "T"
 
Do While opts ^= ""
    Parse Var opts op opts
    Select  /*  op  */
        When Abbrev("TARLIST",op,4)     Then tarlist = 1
        When Abbrev("NOTARLIST",op,3)   Then tarlist = 0
        When Abbrev("INCLUDE",op,3)     Then Parse Var opts include opts
        When Abbrev("SKIP",op,1)        Then Parse Var opts skip opts
        When Abbrev("PEEK",op,2)        Then Do; peek = 1; once = 1; End
        When Abbrev("ONCE",op,1)        Then once = 1
        When Abbrev("VERBOSE",op,1)     Then verbose = 1
        When Abbrev("TERSE",op,5)       Then verbose = 0
        When Abbrev("MODTIME",op,1)     Then modtime = 1
        When Abbrev("NOMODTIME",op,3)   Then modtime = 0
        When Abbrev("PROMPT",op,2)      Then prompt = 1
        When Abbrev("NOPROMPT",op,3)    Then prompt = 0
        When Abbrev("REPLACE",op,3)     Then replace = 1
        When Abbrev("NOREPLACE",op,3)   Then replace = 0
        Otherwise Do
            Address "COMMAND" 'XMITMSG 3 OP (ERRMSG'
/*          Say argo "unrecognized option" op                         */
            Exit 24
            End  /*  Otherwise  Do  */
        End  /*  Select  op  */
    End  /*  Do  While  */
 
Select  /*  tc  */
 
    When tc = 'C' Then Do
        Select  /*  td  */
            When td = 'F' Then Do
                If tf ^= "-" Then Do
                    Parse Var tf tfn '.' tft '.' tfm '.' .
                    If tft = "" Then tft = "TAR"
                    If tfm = "" Then tfm = "A"
                    'ADDPIPE *.OUTPUT: | >' tfn tft tfm 'F 512'
                    End  /*  If  ..  Do  */
                Call CREATE
                End  /*  When  ..  Do  */
            When td = 'T' Then Do
                'ADDPIPE *.OUTPUT: | TAPE' tf
                Call CREATE
                End  /*  When  ..  Do  */
            When td = 'S' Then Do
                'ADDPIPE *.OUTPUT: | TARPUNCH' tf
                Call CREATE
                End  /*  When  ..  Do  */
            Otherwise Do
                Say argo "internal error: unknown TAR target" td tf
                End  /*  Otherwise  Do  */
            End  /*  Select  td  */
        End  /*  When  ..  Do  */
 
    When tc = 'X' Then Do
        Select  /*  td  */
            When td = 'F' Then Do
                If tf ^= "-" Then Do
                    Parse Var tf tfn '.' tft '.' tfm '.' .
                    If tft = "" Then tft = "TAR"
                    'ADDPIPE <' tfn tft tfm '| *.INPUT:'
                    End  /*  If  ..  Do  */
                Call XTRACT
                End  /*  When  ..  Do  */
            When td = 'T' Then Do
                'CALLPIPE CMS TAPE REW (' tf    /*  not quite right  */
                'ADDPIPE TAPE' tf '| *.INPUT:'
                Call XTRACT
                'CALLPIPE CMS TAPE REW (' tf    /*  not quite right  */
                End  /*  When  ..  Do  */
            When td = 'S' Then Do
                'ADDPIPE TARREADC' tf '| *.INPUT:'
                Call XTRACT
                End  /*  When  ..  Do  */
            Otherwise Do
                Say argo "internal error: unknown TAR source" td tf
                End  /*  Otherwise  Do  */
            End  /*  Select  td  */
        End  /*  When  ..  Do  */
 
    When tc = 'T' Then Do
        Select  /*  td  */
            When td = 'F' Then Do
                If tf ^= "-" Then Do
                    Parse Var tf tfn '.' tft
                    If tft = "" Then tft = "TAR"
                    'ADDPIPE <' tfn tft '| *.INPUT:'
                    End  /*  If  ..  Do  */
                Call LISTOC
                End  /*  When  ..  Do  */
            When td = 'T' Then Do
                'CALLPIPE CMS TAPE REW (' tf    /*  not quite right  */
                'ADDPIPE TAPE' tf '| *.INPUT:'
                Call LISTOC
                'CALLPIPE CMS TAPE REW (' tf    /*  not quite right  */
                End  /*  When  ..  Do  */
            When td = 'S' Then Do
                'ADDPIPE TARREADC' tf '| *.INPUT:'
                Call LISTOC
                End  /*  When  ..  Do  */
            Otherwise Do
                Say argo "internal error: unknown TAR source" td tf
                End  /*  Otherwise  Do  */
            End  /*  Select  td  */
        End  /*  When  ..  Do  */
 
    End  /*  Select  tc  */
 
Exit rc * (rc ^= 12)
 
 
/* ---------------------------------------------------------------------
 *  create or update
 */
CREATE:
 
If include = "" Then 'ADDPIPE TARINDEX' args '| *.INPUT:'
                Else 'ADDPIPE <' include 'FILELIST | *.INPUT:'
 
userid = Userid() 
groupid = "N/A" /* vmgroup(userid) */ 
'CALLPIPE VAR USERID   | XLATE LOWER | VAR USERID' 
'CALLPIPE VAR GROUPID  | XLATE LOWER | VAR GROUPID' 
 
Do Forever
 
    'READTO RECORD'
    If rc ^= 0 Then Leave
    If Strip(record) = "" Then Iterate
 
    If Left(record,1) = '*' Then Iterate
    If Left(record,1) = '#' Then Iterate
 
/* 
    Parse Upper Var record fn ft fm  .   '(' opts ')' .
    Parse       Var record .  .  .  name '('  .   ')' .
 */ 
    q1 = Index(record,"'");     q2 = Index(record,'"')
    Select
        When  q1 = 0  & q2 = 0  Then ,
            Parse Var record fn ft fm name '05'x . '05'x type '05'x .
        When  q1 = 0  Then ,
            Parse Var record fn ft fm name '"' . '"' type 
        When  q2 = 0  Then ,
            Parse Var record fn ft fm name "'" . "'" type 
        When  q1 > q2  Then ,
            Parse Var record fn ft fm name '"' . '"' type 
        When  q2 > q1  Then ,
            Parse Var record fn ft fm name "'" . "'" type 
        End  /*  Select  */
    Upper fn ft fm 
    Parse Var name . '(' opts ')' . 
    name = Strip(name)
    If name = "" Then , 
        'CALLPIPE LITERAL' Strip(fn) || '.' || Strip(ft) ,
            '| XLATE LOWER | STRIP | VAR NAME' 
    'CALLPIPE COMMAND LISTFILE' fn ft fm '(DATE | DROP | VAR FILESPEC' 
    Parse Var filespec . . fmode recfm lrecl . . date time .
    fmode = Right(fmode,1)
    Select  /*  fmode  */
        When fmode = 0 Then perm = '600'
        When fmode = 1 Then perm = '644'
        When fmode = 2 Then perm = '644'
        When fmode = 3 Then perm = '444'
        When fmode = 4 Then perm = '644'
        When fmode = 5 Then perm = '644'
        When fmode = 6 Then perm = '666'
        Otherwise           perm = '644'
        End  /*  Select  fmode  */
 
    If recfm = 'V' Then lrecl = 0
 
    'CALLPIPE <' fn ft fm '| TAKE FIRST 1 | VAR SAMPLE'
    If Verify(sample,e_nprint,'M') = 0 Then trans = 't'
                                       Else trans = 'b'
 
    Select
        When trans = 't' Then
            pipe = '| STRIP TRAILING | E2A | SPEC 1-* 1 .0A. X2C NEXT'
        When lrecl = 0 Then
            pipe = '| BLOCK 512 CMS'
        Otherwise
            pipe = ""
        End  /*  Select  */
 
    'CALLPIPE <' fn ft fm pipe '| COUNT BYTES | VAR SIZE'
 
    Call MKTARENT
 
    'CALLPIPE VAR TARENT | E2A | *:'
    'CALLPIPE <' fn ft fm pipe '| FBLOCK 512 00 | *:'
    If verbose Then Say "a" name || "," size "bytes," trans lrecl
 
    End  /*  Do  Forever  */
 
/*  a trailer of nulls  */ 
'OUTPUT' Copies('00'x,512)
 
Return
 
 
/* ---------------------------------------------------------------------
 *  extract
 */
XTRACT:
 
'ADDPIPE *: | FBLOCK 512 | *.INPUT:'
'CALLPIPE *: | TAKE' skip '| HOLE'
 
Parse Var args xtf xfn xft xfm .
If xfn = "" Then xfn = "="
If xft = "" Then xft = "="
If xfm = "" Then xfm = "A"
 
Do Forever
 
    'PEEKTO'
    If rc ^= 0 Then Leave
 
    'CALLPIPE *: | TAKE 1 | A2E | VAR RECORD'
    Call EXTARENT
    If size = 0 & name = "" Then Leave
    If size = 0 Then Iterate
    If name ^= xtf & xtf ^= '*' & xtf ^= '' Then Do
        'CALLPIPE *: | TARTAKE' size '| HOLE'
        Iterate
        End  /*  If  ..  Do  */
 
    Parse Value Reverse(name) With basename '/' .
    basename = Reverse(basename)
    Parse Upper Var basename fn '.' ft '.' .
    If fn = "" Then fn = Userid()
    If xfn ^= "=" Then fn = xfn
    If ft = "" Then ft = "$"
    If xft ^= "=" Then ft = xft
    fm = xfm
    filespec = fn ft fm
 
    If ^peek Then Do
        'CALLPIPE STATE' filespec
        If rc = 0 Then Do
            If ^replace Then Do
                If verbose Then ,
                    Say "x" name || "," size "bytes," ,
                        (size+511)%512 "tape blocks"
                Address "COMMAND" 'XMITMSG 24 FILESPEC (CALLER TAR'
                Leave
                End  /*  If  ..  Do  */
            Else Address "COMMAND" 'ERASE' filespec
            End  /*  If  ..  Do  */
        End  /*  If  ..  Do  */
 
    If trans ^= 'T' & trans ^= 'B' Then Do
        'PEEKTO RECORD'
        If size < 512 Then record = Left(record,size)
        If Verify(record,a_nprint,'M') = 0 Then Do
            trans = 'T'
            lrecl = 0
            End  /*  If  ..  Do  */
        Else Do
            trans = 'B'
            If size < 65536 Then lrecl = size
                            Else lrecl = 512
            End  /*  Else  Do  */
        End  /*  If  ..  Do  */
 
    Select
        When trans = 'T' & lrecl = 0 Then
            pipe = 'DEBLOCK LINEND 0A | STRIP TRAILING 0D' ,
                '| DROP LAST | A2E | PAD 1'
        When trans = 'T' & lrecl > 0 Then , 
            pipe = 'DEBLOCK LINEND 0A | STRIP TRAILING 0D' , 
                '| DROP LAST | A2E | PAD' lrecl 
        When trans = 'B' & lrecl = 0 Then , 
            pipe = 'DEBLOCK CMS' 
        When trans = 'B' & lrecl > 0 Then , 
            pipe = 'FBLOCK' lrecl '00' 
        When trans = 'V' Then , 
            pipe = 'DEBLOCK CMS' 
        End  /*  Select  */ 
  
    If lrecl = 0 Then fix = ""
                 Else fix = "FIXED" lrecl
 
    If verbose Then ,
        Say "x" name || "," size "bytes," ,
                (size+511)%512 "tape blocks, as" ,
                    filespec || fmode trans fix
    'CALLPIPE' ,
        '*: | TARTAKE' size '|' pipe '| > TAR CMSUT1' fm || '3' fix
 
    If peek Then Do
        Address "COMMAND" 'MAKEBUF'
        Push "COMMAND MSG x" name || "," size "bytes," ,
                (size+511)%512 "tape blocks"
        Push "COMMAND SET FN" fn
        Push "COMMAND SET FT" ft
        Push "COMMAND SET FM" fm || fmode
        Address "COMMAND" 'XEDIT TAR CMSUT1' fm
        Address "COMMAND" 'DROPBUF'
        End  /*  If  ..  Do  */
    Else Do
        Address "COMMAND" 'RENAME TAR CMSUT1' fm filespec || fmode
        Address "COMMAND" 'DMSPLU' filespec date time
        End  /*  Else  Do  */
 
    If once Then Leave
    If xtf ^= '*' & xtf ^= '' Then Leave
 
    End  /*  Do  Forever  */
 
Return
 
 
/* ---------------------------------------------------------------------
 *  list table of contents
 */
LISTOC:
 
'ADDPIPE *: | FBLOCK 512 | *.INPUT:'
'CALLPIPE *: | TAKE' skip '| HOLE'
 
Do Forever
 
    'PEEKTO'
    If rc ^= 0 Then Leave
 
    'CALLPIPE *: | TAKE 1 | A2E | VAR RECORD'
    Call EXTARENT
    If size = 0 & name = "" Then Leave
 
    If size > 0 Then Do
        Select
            When tarlist  Then 'OUTPUT' "      " || Left(name,46) ,
                Right(size,8) Right(date,8) Right(time,8) ,
                    Right(skip,8) name
/*                             trans recfm lrecl fmode                */
            When verbose  Then 'OUTPUT' Left(name,42) '-' ,
                Right(date,8) Right(time,8) Right(size,8) "bytes."
            Otherwise          'OUTPUT' name
            End  /*  Select  */
 
        take = Trunc((size + 511) / 512)
        'CALLPIPE *: | TAKE' take '| HOLE'
        skip = skip + take
        End  /*  If  ..  Do  */
    skip = skip + 1
 
    If args ^= "" Then Leave
 
    End  /*  Do  Forever  */
 
Return
 
 
/* ------------------------------------------------------------ EXTARENT
 *  Extract TAR entry (directory info) values.
 *  Sets: size, and other variables.
 */
EXTARENT:
Parse Var record   1 name '00'x .
record = Translate(record,' ','00'x)
Parse Upper Var record 101 perm . ,
                       125 size date chksum trans lrecl fmode . ,
                       257 . ,
                       385 .
size = o2d(size)                /* convert to decimal */
If size > 0 Then Do
    Parse Value sysdate(o2d(date)) With date time .
    chksum = o2d(chksum)        /* convert to decimal */
    lrecl = o2d(lrecl)          /* convert to decimal */
    If lrecl = 0 Then recfm = 'V'
                 Else recfm = 'F'
    If ^Datatype(fmode,'N') Then fmode = '1'
    End  /*  If  ..  Do  */
 
Return
 
 
/* ------------------------------------------------------------------ */
O2D:        Procedure   /*  Octal to Decimal conversion  */
Parse Arg o
d = 0
Do While o ^= ""
    Parse Var o 1 c 2 o
    If Datatype(c,'N') Then d = d * 8 + c
    End  /*  Do  While  */
Return d
 
 
/* ------------------------------------------------------------------ */
D2O:        Procedure   /*  Decimal to Octal conversion  */
Parse Arg d
If ^Datatype(d,'N') Then d = 0
d = trunc(d)
If d < 1 Then Return 0
o = ""
Do While d ^= 0
    o = d // 8 || o
    d = d % 8
    End  /*  Do While  */
Return o
 
 
/* ------------------------------------------------------------------ */
DATEREAD:   Procedure   /*  return textual date from octal  */
Parse Arg date
 
year = 1970
Do Forever
    If year - (year % 4) * 4 = 0 Then days = 366
                                 Else days = 365
    If date < days Then Leave
    date = date - days
    year = year + 1
    End
 
Return year || '.' || date
 
 
/* ------------------------------------------------------------------ */
DATEMAKE:   Procedure   /*  return octal date from textual  */
Parse Arg date
 
_m.1  = 31;     _m.2  = 28;     _m.3  = 31;     _m.4  = 30
_m.5  = 31;     _m.6  = 30;     _m.7  = 31;     _m.8  = 31
_m.9  = 30;     _m.10 = 31;     _m.11 = 30;     _m.12 = 31
 
year = 1970
Do Forever
    If year - (year % 4) * 4 = 0 Then days = 366
                                 Else days = 365
    If date < days Then Leave
    date = date - days
    year = year + 1
    End
 
Return year || '.' || date
 
/* 
If yy // 4 = 0 & yy // 100 ^= 0 Then _m.2 = 29
                                Else _m.2 = 28
 */ 
 
 
/* ------------------------------------------------------------- TARDATE
 */
TARDATE:  Procedure Expose dfmt tzos
Parse Arg date time .
Parse Var time hh ':' mm ':' ss
Parse Var date mo '/' dd '/' yy         /*  If dfmt = 'U'  */
ly = (yy // 4 = 0 & (yy // 100 ^= 0 | yy // 400 = 0))
Select  /*  mo  */
    When  mo =  1   Then nop
    When  mo =  2   Then dd = dd + 31
    When  mo =  3   Then dd = dd + 59 + ly
    When  mo =  4   Then dd = dd + 90 + ly
    When  mo =  5   Then dd = dd + 120 + ly
    When  mo =  6   Then dd = dd + 151 + ly
    When  mo =  7   Then dd = dd + 181 + ly
    When  mo =  8   Then dd = dd + 212 + ly
    When  mo =  9   Then dd = dd + 243 + ly
    When  mo = 10   Then dd = dd + 273 + ly
    When  mo = 11   Then dd = dd + 304 + ly
    When  mo = 12   Then dd = dd + 334 + ly
    End  /*  Select  mm  */
Do yy = yy - 1 to 70 by -1
    ly = (yy // 4 = 0 & (yy // 100 ^= 0 | yy // 400 = 0))
    dd = dd + 365 + ly
    End  /*  Do  For  */
dd = dd - 1
Return dd*86400+hh*3600+mm*60+ss-tzos
 
 
/* ------------------------------------------------------------- SYSDATE
 */
SYSDATE:  Procedure Expose dfmt tzos
Parse Arg base .
base = base + tzos
dd   = base % 86400 + 1
time = base // 86400
yy = 70
ly = (yy // 4 = 0 & (yy // 100 ^= 0 | yy // 400 = 0))
Do While dd > 365 + ly
    yy = yy + 1
    dd = dd - 365 - ly
    ly = (yy // 4 = 0 & (yy // 100 ^= 0 | yy // 400 = 0))
    End  /*  Do  While  */
Select  /*  mo  */
    When  dd <=  31      Then     mm =  1
    When  dd <=  59 + ly Then Do; mm =  2; dd = dd - 31;       End
    When  dd <=  90 + ly Then Do; mm =  3; dd = dd - 59  - ly; End
    When  dd <= 120 + ly Then Do; mm =  4; dd = dd - 90  - ly; End
    When  dd <= 151 + ly Then Do; mm =  5; dd = dd - 120 - ly; End
    When  dd <= 181 + ly Then Do; mm =  6; dd = dd - 151 - ly; End
    When  dd <= 212 + ly Then Do; mm =  7; dd = dd - 181 - ly; End
    When  dd <= 243 + ly Then Do; mm =  8; dd = dd - 212 - ly; End
    When  dd <= 273 + ly Then Do; mm =  9; dd = dd - 243 - ly; End
    When  dd <= 304 + ly Then Do; mm = 10; dd = dd - 273 - ly; End
    When  dd <= 334 + ly Then Do; mm = 11; dd = dd - 304 - ly; End
    Otherwise                 Do; mm = 12; dd = dd - 334 - ly; End
    End  /*  Select  dd  */
Return Right(mm,2,'0') || '/' || ,
       Right(dd,2,'0') || '/' || ,
       Right(yy,2,'0') ,
       Right(time%3600,2,'0') || ':' || ,
       Right((time//3600)%60,2,'0') || ':' || ,
       Right(time//60,2,'0')
 
 
/* ------------------------------------------------------------ MKTARENT
 *  Create a TAR entry (directory info) from values.
 */
MKTARENT:
 
chksum = 0
 
tarent   =  Left(name,100,'00'x) || ,
            Right(perm,6) '00'x || ,
            "     1" '00'x || "     1" '00'x || ,
            Right(d2o(size),11) ,
            Right(d2o(tardate(date time)),11) ,
            Right(d2o(chksum),6) || '00'x || ,
            Right(trans,2) ,
            Right(d2o(lrecl),8) ,
            Right(fmode,1) || '00'x
 
'CALLPIPE VAR TARENT | E2A | VAR TARENT'
Do i = 1 to Length(tarent)
    chksum = chksum + c2d(Substr(tarent,i,1))
    End
 
chksum = chksum + 16
 
 
tarent   =  Left(name,100,'00'x) || ,
            Right(perm,6) '00'x || ,
            "     1" '00'x || "     1" '00'x || ,
            Right(d2o(size),11) ,
            Right(d2o(tardate(date time)),11) ,
            Right(d2o(chksum),6) || '00'x || ,
            Right(trans,2) ,
            Right(d2o(lrecl),8) ,
            Right(fmode,1) || '00'x
 
tarent = Left(tarent,256,'00'x)
tarent = Left(tarent,512,'00'x)
 
Return
 
tarent02 = '00'x || "ustar" || '00'x || "00" || ,
    Left(userid,32,'00'x) || Left(groupid,32,'00'x) || ,
           "0000000" || '00'x || "0000000" || '00'x
 
Return
 
 
/* ------------------------------------------------------------ TZOFFSET
 *  Compute timezone offset based on timezone string from 'CP Q TIME'. 
 *  (we probably have a CSL routine to do this ... but maybe not) 
 */
TZOFFSET: Procedure 
 
Parse Upper Arg denom . ',' . , . 
Parse Upper Value Diag(08,'QUERY TIME') With . . . tz . 
 
Select  /*  tz  */ 
    When tz = "CST" Then zo = -6 
    When tz = "CDT" Then zo = -5 
    When tz = "EST" Then zo = -5 
    When tz = "EDT" Then zo = -4 
    Otherwise zo = 0 
    End  /*  Select tz  */ 
 
denom = Left(denom,1) 
Select  /*  denom  */ 
    When denom = "S" Then Return zo * 60 * 60    /* offset in seconds */
    When denom = "M" Then Return zo * 60         /* offset in minutes */
    Otherwise Return zo 
    End  /*  Select denom  */ 
 
 
