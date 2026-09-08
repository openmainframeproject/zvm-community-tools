/*
 *        Name: MIMEREAD REXX
 *              CMS Pipelines stage to interpret MIME-ified mail
 *      Author: Rick Troth, Rice University, Information Systems
 *              Rick Troth, Houston, Texas, USA
 *        Date: 1992-Aug-01, 1993-May-21
 */
 
Trace "OFF"
 
Parse Source . . arg0 .
Parse Upper Arg args '(' opts ')' .
'CALLPIPE COMMAND IDENTIFY | VAR IDENTITY'
Parse Var identity userid . hostid . rscsid .
 
'CALLPIPE COMMAND QUERY LANGUAGE ALL' ,
    '| SPEC / / 1 1-* N / / N | VAR LANGLIST'
If Index(langlist," WEB ") = 0 Then ,
    Address "COMMAND" 'SET LANGUAGE (ADD WEB USER'
 
version = ""
date = ""
name = ""
subject = ""
from = ""
tag = "";   content = "";   code = ""
 
Address "COMMAND" 'GLOBALV SELECT MIME GET MAILBOOK'
 
i = 0
 
Do Forever
 
    'READTO LINE'
    /*  watch for end-of-file  */
    If rc ^= 0 Then Leave
 
    /*  eliminate TAB characters in the header  */
    line = Translate(line,' ','05'x)
 
    /*  watch for end-of-header  */
    If Strip(line) = "" Then Leave
 
    i = i + 1
    head.i = line
 
    If Left(line,1) = ' ' Then val = val Strip(line)
                         Else Do; Parse Var line tag val; Upper tag; End
 
    Select  /*  tag  */
 
        /* MIME specific tags */
        When tag = "MIME-VERSION:" Then version = val
        When tag = "CONTENT-TYPE:" Then content = val
        When tag = "CONTENT-TRANSFER-ENCODING:" Then code = val
 
        /* regular mail tags */
        When tag = "DATE:" Then date = val
        When tag = "SUBJECT:" Then subject = Strip(val)
        When tag = "FROM:" Then from = val
 
        Otherwise /* Say "command/parameter" tag "ignored" 843 */ nop
        End  /*  Select  tag  */
 
    End  /*  Do  While  */
 
If rc ^= 0 Then Exit rc * (rc ^= 12)
 
head.0 = i
 
content = Strip(content)
If version = "" & content = "" & mailbook Then Exit -1
/*
If version = "" & content = "" Then Do
    Say "Version is empty and content is empty."
/*  637, 693,  others?  */
Exit -1
    End
 */
 
'PEEKTO'
If rc ^= 0 Then Exit rc * (rc ^= 12)
If content = "" Then content = "TEXT/PLAIN"
 
Address "COMMAND" 'GLOBALV SELECT MIME PUT VERSION'
Parse Var content content ';' parms
Upper content code
/*  Say "Content-Type:" content  */
/*  Say "Content-Transfer-Encoding:" code  */
Parse Var content major '/' minor
 
Select  /*  from  */
    When Index(from,'<') > 0 Then Parse Var from . '<' user
    When Index(from,'(') > 0 Then Parse Var from user '(' .
    Otherwise user = from
    End
If Index(user,'!') > 0 Then Do
    Parse Value Reverse(user) With user '!' .
    user = Reverse(user)
    End  /*  If  ..  Do  */
Parse Var user user '@' host
Parse Var user user '%' .
user = Translate(user,'__','.=')
 
Select  /*  content  */
 
    When content = "MULTIPART/X-SIFT" | content = "MULTIPART/X-UFT" ,
        | content = "MULTIPART/SIFT" | content = "MULTIPART/UFT" Then Do
 
        /*  extract the boundary string from the "parms"  */
        Do While parms ^= ""
            Parse Var parms parm ';' parms
            Parse Upper Var parm var '='  .
            Parse       Var parm  .  '=' val
            If var = "BOUNDARY" Then boundary = Strip(val)
            End  /*  Do While  */
        If Left(boundary,1) = '"' Then ,
            Parse Var boundary . '"' boundary '"' .
 
        /*  consume the first part (should be empty)  */
        'CALLPIPE *: | TOLABEL --' || boundary || '| CONSOLE'
        'READTO'    /*  waste that first boundary  */
 
        prev.0 = 0
        /*  split the parts at the boundary  */
        Do Forever
            'CALLPIPE (END !) *: | TOLABEL --' || boundary || ,
                '| FB:' arg0 args '(' opts '| STEM NEXT.' ,
                    '! STEM PREV. | FB:'
            'READTO'    /*  eat the boundary  */
            'PEEKTO'    /*  is there any more?  */
            If rc ^= 0 Then Leave
            'CALLPIPE STEM NEXT. | STEM PREV.'
            End  /*  Do Forever  */
 
        End  /*  When .. Do  */
 
    When content = "X-SIFT/METAFILE" | content = "SIFT/METAFILE" ,
        | content = "X-SIFT/META" | content = "SIFT/META" ,
        | content = "APPLICATION/X-SIFT" ,
        | content = "APPLICATION/SIFT" Then Do
Say "Definite SIFT/UFT header:"
        If code = "BASE64" Then ,
            'ADDPIPE *.INPUT: | DEBASE64 | MAKETEXT LOCAL | *.INPUT:'
        Do Forever
            'READTO RECORD'
            If rc ^= 0 Then Leave
            If Strip(record) = "" Then Iterate
            Parse Var record a b .
            Select
                When Index(a,'=') > 0 | Left(b,1) = '=' Then ,
                    Parse Var record tag '=' val
                When Index(a,':') > 0 Then ,
                    Parse Var record tag ':' val
                Otherwise ,
                    Parse Var record tag val
                End  /*  Select  */
            tag = Strip(tag); If tag ^= "" Then ,
                'OUTPUT' Translate(tag) || '=' || Strip(val)
            End  /*  Do Forever  */
        End  /*  When .. Do  */
 
    When content = "X-SIFT/DATAFILE" | content = "SIFT/DATAFILE" ,
        | content = "X-SIFT/DATA" | content = "SIFT/DATA" Then Do
Say "Definite SIFT/UFT body:"
        _fn = Right(Date('D'),3,'0') || Right(Time('S'),5,'0')
        'CALLPIPE *.INPUT.1: | >' _fn 'METAFILE A'
        'CALLPIPE *: | >' _fn 'DATAFILE A'
Address "COMMAND" 'XEDIT' _fn 'DATAFILE'
        End  /*  When .. Do  */
 
    When content = "APPLICATION/OCTET-STREAM" Then Do
        'ADDPIPE *.OUTPUT: | UFTXREAD'
        'CALLPIPE LITERAL FILE -' user '| *:'
        If date ^= "" Then 'CALLPIPE LITERAL DATE' date '| *:'
        Parse Var subject . "FILE" name
        If name ^= "" Then 'CALLPIPE LITERAL NAME' name '| *:'
        'CALLPIPE VAR PARMS | DEBLOCK LINEND ; | CHANGE /=/ / | *:'
        'CALLPIPE LITERAL DATA | *:'
        If code = "BASE64" Then ,
            'CALLPIPE *: | DEBASE64 | *:'
        Else
            'CALLPIPE *: | MAKETEXT NETWORK | *:'
        End  /*  When .. Do  */
 
    When content = "IMAGE/GIF" Then Do
        /*  verify that we have VMGIF accessed  */
        'CALLPIPE CMS STATE VMGIF MODULE * | *:'
        If rc ^= 0 Then Exit rc
 
        /*  try to stash the input stream in a temp file  */
        If code = "BASE64" Then ,
            'CALLPIPE *: | DEBASE64 | > TEMP#GIF GIF A3'
        If code = "QUOTED-PRINTABLE" Then ,
            'CALLPIPE *: | DECODEQP | > TEMP#GIF GIF A3'
        If rc ^= 0 Then Do
            grc = rc
            'CALLPIPE COMMAND ERASE TEMP#GIF GIF A'
            Exit grc
            End  /*  If  ..  Do  */
 
        /*  ensure the right libraries GLOBALed  (I hate this!)  */
        'CALLPIPE COMMAND QUERY TXTLIB' ,
            '| STRIP LEADING STRING /TXTLIB   = / | JOIN * | VAR TXTLIB'
        Upper txtlib;   If Strip(txtlib) = "NONE" Then txtlib = ""
        'CALLPIPE COMMAND GLOBAL TXTLIB ADMPLIB ADMGLIB' txtlib
 
        /*  now run VMGIF  */
        'CALLPIPE CMS VMGIF -em5 TEMP#GIF | *:'; grc = rc
 
        /*  restore GLOBALed libraries  */
        'CALLPIPE COMMAND GLOBAL TXTLIB' txtlib
 
        Exit grc
        End  /*  When  ..  Do  */
 
    When major = "TEXT" | content = "APPLICATION/POSTSCRIPT" Then Do
        If code = "BASE64" Then 'ADDPIPE *.INPUT: | DEBASE64 |' ,
            'MAKETEXT LOCAL | *.INPUT:'
        If code = "QUOTED-PRINTABLE" Then 'ADDPIPE *.INPUT:' ,
            '| DECODEQP | MAKETEXT LOCAL | *.INPUT:'
        If minor = "RICHTEXT" | minor = "ENRICHED" Then ,
            'CALLPIPE *: | RICHTEXT | >' arg0 'CMSUT1 A3'
        Else ,
            'CALLPIPE *: | UNTAB -8 | >' arg0 'CMSUT1 A3'
        'CALLPIPE STEM HEAD. | >' arg0 'CMSUT2 A3'
        If user ^= "" Then
        Push "COMMAND SET FN" user
        Push "COMMAND SET FT MAIL"
        Push "COMMAND SET FM A1"
        If subject ^= "" Then
        Push "COMMAND MSG Subject:" subject
        Push "COMMAND MACRO MIMEPROF" arg0 "(" opts
        /*  do NOT wrap the following with MAKEBUF/DROPBUF  */
        Address "COMMAND" 'XEDIT' arg0 'CMSUT1'
        End  /*  When  ..  Do  */
 
    When major = "MULTIPART" Then Do
 
        /*  extract the boundary string from the "parms"  */
        Do While parms ^= ""
            Parse Var parms parm ';' parms
            Parse Upper Var parm var '='  .
            Parse       Var parm  .  '=' val
            If var = "BOUNDARY" Then boundary = Strip(val)
            End  /*  Do While  */
        If Left(boundary,1) = '"' Then
            Parse Var boundary . '"' boundary '"' .
        label = Right(Time('S'),5,'0') || '#'
        i = 0
 
        /*  split the parts at the boundary  */
        Do Forever
            'CALLPIPE (END !) *: | TOLABEL --' || boundary || ,
                '| P: MIMEPART' label || Right(i,2,'0') i ,
                '! STEM HEAD. | P:'
            'READTO'    /*  eat the boundary  */
            'PEEKTO'    /*  is there any more?  */
            i = i + 1
            If rc ^= 0 Then Leave
            End  /*  Do Forever  */
 
        /*  are we running under MAILBOOK?  */
        Address "COMMAND" 'GLOBALV SELECT MIME GET MAILBOOK'
        mailbook = (mailbook = 1)
        If mailbook Then  /*  turn it off under FILELIST  */ ,
            Address "COMMAND" 'GLOBALV SELECT MIME SET MAILBOOK 0'
 
        /*  invoke FILELIST on the now disk-resident separated parts  */
        Address "COMMAND" 'MAKEBUF'
        Push "COMMAND SET PF11 MACRO EXECUTE CURSOR EXEC MIMEREAD"
        Push "COMMAND SET LINEND OFF"
        Push "SNAME"    /*  sort the list by filename  */
        Push "MSG These files will be erased when you leave FILELIST"
        If subject ^= "" Then
        Push "COMMAND MSG Subject:" subject
        Push "COMMAND MSG From:" from
        Address "COMMAND" 'EXEC FILELIST' label || '*'
        flrc = rc
        Address "COMMAND" 'DROPBUF'
 
        /*  restore MAILBOOK flag  */
        Address "COMMAND" 'GLOBALV SELECT MIME PUT MAILBOOK'
 
        /*  clean-up after ourselves  */
        Do j = 0 to i
            'CALLPIPE COMMAND ERASE' label || Right(j,2,'0') '* A'
            End  /*  Do  For  */
        rc = flrc
 
        End  /*  When  ..  Do  */
 
    When content = "MESSAGE/EXTERNAL-BODY" Then Do
        Do While parms ^= ""
            Parse Var parms parm ';' parms
            Parse Upper Var parm var '='  .
            Parse       Var parm  .  '=' val
            var = Strip(var)
            val = Strip(val)
            If Left(val,1) = '"' Then Parse Var val '"'val'"'
            Select  /*  var  */
                When Abbrev("NAME",var,4) Then name = val
                When Abbrev("SITE",var,4) Then host = val
                When Abbrev("ACCESS-TYPE",var,4) Then mode = val
                When Abbrev("DIRECTORY",var,3) Then directory = val
                Otherwise Say var '=' val
                End  /*  Select  var  */
            End  /*  Do  While  */
        If mode ^= "anon-ftp" Then Exit -1
        Address "COMMAND" 'MAKEBUF'
        Queue "anonymous" userid || '@' || hostid
        Queue "CD" directory
        Queue "GET" name arg0 || ".CMSUT1.A3"
        Address "COMMAND" 'FTP' host
        Parse Var name fn '.' ft '.' .
        If fn = "" Then ft = userid
        Push "COMMAND SET FN" fn
        If ft = "" Then ft = "TXT"
        Push "COMMAND SET FT" ft
        Push "COMMAND SET FM A1"
        Address "COMMAND" 'XEDIT' arg0 'CMSUT1'
        Address "COMMAND" 'DROPBUF'
        End  /*  When  ..  Do  */
 
    When content = "MESSAGE/RFC822" Then ,
        'CALLPIPE *: |' arg0 args '(' opts
 
    Otherwise  Do
/*      Address "COMMAND" 'XMITMSG 88 CONTENT (APPLID WEB ERRMSG'     */
        Address "COMMAND" 'XMITMSG 636 CONTENT (APPLID WEB ERRMSG'
/*      Say "Unsupported MIME content type:" '"'content'"'            */
        rc = 8
        End
 
    End  /*  Select  maj  */
 
Exit rc * (rc ^= 12)
 
