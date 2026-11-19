/*
 *        Name: RICHTEXT REXX
 *              convert MIME "richtext" ("enriched" text) to plain-text.
 */
 
'STREAMSTATE OUTPUT 0'                  /* Have a primary stream? */
If rc = 12 Then Do
    'ADDPIPE *.OUTPUT.0: | CONSOLE'
    End  /*  If .. Do  */
 
'STREAMSTATE OUTPUT 1'                  /* Have a secondary stream? */
If rc = -4 Then Do
    'ADDSTREAM OUTPUT'
    'ADDPIPE *.OUTPUT.1: | HOLE'
    End  /*  If .. Do  */
 
meta = "TEST_VAR"
data = "test value"
'CALLPIPE VAR DATA | SPEC /' ,
                    || meta || '/ 1 /=/ NEXT 1-* NEXT | *.OUTPUT.1:'
 
meta = ""               /*  start with NOT collecting meta data  */
data = ""               /*  start with an EMPTY meta-data buffer  */
 
qs = "> "               /*  quote prefix string  */
xs = "> "               /*  excerpt prefix string  */
indent = 4
 
'CALLPIPE COMMAND QUERY DISPLAY | VAR DISPLAY'
Parse Var display . . width .
If ^Datatype(width,'N') Then width = 72
                        Else width = width - 8
 
/*  what about TAB characters?  */
'ADDPIPE *.INPUT: | UNTAB -8 | SPLIT BEFORE /</' ,
    '| SPLIT BEFORE /&/ | SPEC 1-* 1 / / NEXT | *.INPUT:'
 
line = ""
center = 0
quote = 0
excerpt = 0
li = 0
ri = 0
hs = 0
 
Do Forever
 
    'PEEKTO TEXT'
    If rc ^= 0 Then Leave
 
    If Strip(text) = "" Then text = "<P>"
 
    If Left(text,1) = '<' Then Do
        Parse Var text '<'command'>'text
        Parse Upper Var command verb args
    If Right(text,2) = "= " Then text = Left(text,Length(text)-2)
 
        Select  /*  verb  */
 
            When Left(verb,1) = "!" Then nop
            When verb = "LT" Then line = line || '<'
            When verb = "GT" Then line = line || '>'
            When verb = "CENTER" Then center = 1
            When verb = "/CENTER" Then center = 0
            When verb = "QUOTATION" Then quote = 1
            When verb = "/QUOTATION" Then quote = 0
/*  what about BLOCKQUOTE?  is it = EXCERPT?  */
            When verb = "EXCERPT" Then Do
                Call FLUSH
                'OUTPUT'
                excerpt = 1
                End  /*  When .. Do  */
            When verb = "/EXCERPT" Then Do
                Call FLUSH
                'OUTPUT'
                excerpt = 0
                End  /*  When .. Do  */
            When verb = "LEFTINDENT" Then li = li + indent
            When verb = "/LEFTINDENT" Then li = li - indent
            When verb = "RIGHTINDENT" Then ri = ri + indent
            When verb = "/RIGHTINDENT" Then ri = ri - indent
            When verb = "NL" | verb = "BR" Then Call FLUSH
            When verb = "LI" Then Call FLUSH
            When verb = "MENU" Then Call FLUSH
            When verb = "/MENU" Then Call FLUSH
            When verb = "P" Then Do
                'OUTPUT' " "
                Call FLUSH
                End  /*  When  ..  Do  */
 
            When verb = "ITALIC" | verb = "/ITALIC" ,
                | verb = "BOLD"  | verb = "/BOLD" ,
                | verb = "FIXED" | verb = "/FIXED" Then nop
 
            When verb = "TITLE" Then Do
                If data ^= "" Then 'CALLPIPE VAR DATA | SPEC /' ,
                    || meta || '/ 1 /=/ NEXT 1-* NEXT | *.OUTPUT.1:'
                meta = "TITLE"
                End  /*  When .. Do  */
            When verb = "/TITLE" Then Do
                If data ^= "" Then 'CALLPIPE VAR DATA | SPEC /' ,
                    || meta || '/ 1 /=/ NEXT 1-* NEXT | *.OUTPUT.1:'
                meta = ""
                data = ""
                End  /*  When .. Do  */
 
When  verb = "HTML"     | verb = "/HTML" ,
    | verb = "HEAD"     | verb = "/HEAD" ,
    | verb = "BODY"     | verb = "/BODY" ,
    | verb = "ADDRESS"  | verb = "/ADDRESS" ,
    | verb = "LINK"     | verb = "IMG" ,
    | verb = "H1"       | verb = "/H1" ,
    | verb = "H2"       | verb = "/H2" ,
    | verb = "H3"       | verb = "/H3" ,
    | verb = "UL"       | verb = "/UL" ,
    | verb = "TT"       | verb = "/TT" ,
    | verb = "I"        | verb = "/I" ,
    | verb = "A"        | verb = "/A" Then nop
 
            Otherwise ,
                Address "COMMAND" 'XMITMSG 3 VERB (ERRMSG'
 
            End  /*  Select  verb  */
 
        End  /*  If  ..  Do  */
 
    If Left(text,1) = '&' & Index(text,';') > 0 Then Do
        Parse Var text '&'token';'text
        Select  /*  token  */
            When token = "lt" Then text = '<' || text
            When token = "gt" Then text = '>' || text
            When token = "thorn" Then text = 'AE'x|| text
            Otherwise text = '?' || text
            End  /*  Select  token  */
        End  /*  If  ..  Do  */
 
    If ^hs Then text = Strip(text,'L')
    If meta ^= "" Then data = data || text
                  Else line = line || text
 
    'READTO'
 
    End  /*  Do  Forever  */
 
Call FLUSH
 
Exit
 
/* ------------------------------------------------------------------ */
FLUSH:
 
w = width - li
Do While Length(line) > w & Index(line,' ') > 0
    p = Lastpos(' ',line,w)
    part = Left(line,p-1)
    If center Then part = Center(part,width)
    If quote Then part = qs || part
    If excerpt Then part = xs || part
    If li > 0 Then part = Copies(' ',li) || part
    'OUTPUT' part
    line = Substr(line,p+1)
    End  /*  Do  While  */
 
If center Then line = Center(line,width)
If quote Then line = qs || line
If excerpt Then line = xs || line
If li > 0 Then line = Copies(' ',li) || line
If line = "" Then line = " "
 
'OUTPUT' line
line = ""
 
Return
 
