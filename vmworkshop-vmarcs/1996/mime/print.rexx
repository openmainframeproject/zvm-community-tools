/*
 *        Name: PRINT REXX
 *              a disposable filter for printing from
 *              Pipelines-based applications such as CMS Gopher.
 *              (disposable in that you can replace it with your own)
 *      Author: Rick Troth, Rice University, Information Systems
 *              Thanks to Jim Colten for two better versions of
 *              "STANDARD".
 *        Date: Spring 1992, 1993-Jan-07
 *
 *        Note: Address() returns garbage in a pipelines stage
 */
 
dev = "00E"
linecount = 55
upcase = 0
 
Parse       Arg name '(' opts ')' .
Parse Upper Var name fn ft fm .
fn = Left(fn,8); ft = Left(ft,8)
 
fml = Length(fm)
Select  /*  fml  */
    When fml = 1 Then If Datatype(Left(fm1,1),'N') Then fm = ""
    When fml = 2 Then Do
        If Datatype(Left(fm,1),'N') Then fm = ""
        If ^Datatype(Right(fm,1),'N') Then fm = ""
        End  /*  When  ..  Do  */
    Otherwise fm = ""
    End  /*  Select  fm  */
 
If Words(name) = 2 | Words(name) = 3 Then
    name = Left(fn,8) Left(ft,8) Left(fm,2)
 
'CALLPIPE COMMAND QUERY CMSLEVEL | CHOP , | VAR CMSLEVEL'
'CALLPIPE CP      QUERY CPLEVEL  | CHOP , | VAR CPLEVEL'
title = "File:" Left(fn,8) Left(ft,8) Left(fm,2) ,
        "     " cmslevel "--" cplevel
 
cc = (ft = "LISTING"  | ft = "LIST3800" | ,
      ft = "LISTCPDS" | ft = "LIST3820" | ft = "LIST38PP")
 
Do While opts ^= ""
    Parse Var opts op opts; Upper op
    Select  /*  op  */
        When Abbrev("LINECOUNT",op,2) Then Do
            Parse Var opts linecount opts
            If linecount = "" Then linecount = 55
            End  /*  When  ..  Do  */
        When Abbrev("UPCASE",op,2)  Then upcase = 1
        When Abbrev("CC",op,2)      Then cc = 1
        When Abbrev("NOCC",op,4)    Then cc = 0
        When Abbrev("TITLE",op,1)   Then Do
            title = opts
            opts = ""
            End  /*  When  ..  Do  */
        Otherwise Say "Unrecognized option" op
        End  /*  Select  op  */
    End  /*  Do  While  */
 
If cc Then 'CALLPIPE *: | ASATOMC | URO' dev
/*    Else Call STANDARD      */
Else Do Forever
    'PEEKTO'
    If rc ^= 0 Then Leave
    'CALLPIPE *: | TAKE' linecount ,
        '| SPEC .09. X2C 1  1-* NEXT' ,
        '| PREFACE LITERAL' '19'x || title ,
        '| PREFACE LITERAL' '89'x ,
        '| URO' dev
    If rc ^= 0 Then Leave
    End  /*  Else  ..  Do  Forever  */
prc = rc * (rc ^= 12)
 
/*  use  CP CLOSE,  so the user can  SPOOL dev CONT  if he wants to  */
If fn = "" Then Parse Value Diag(08,'CLOSE' dev) With rs
           Else Parse Value Diag(08,'CLOSE' dev 'NAME' fn ft) With rs
 
If rs ^= "" Then
    'CALLPIPE VAR RS | SPLIT AT STRING "' || '15'x || '" | *:'
 
Return prc
 
 
 
/* ------------------------------------------------------------ STANDARD
 *  Here is a version of STANDARD that loops once per page rather than
 *  once per record.  It should work with most versions of Pipelines.
 */
STANDARD:
header = '19'x || title
'PEEKTO'
Do While rc = 0
    'CALLPIPE *: | TAKE' linecount ,
        '| SPEC .09. X2C 1  1-* NEXT' ,
        '| PREFACE VAR HEADER' ,
        '| PREFACE LITERAL' '89'x ,
        '| URO' dev
    'PEEKTO'
    End  /*  Do  Forever*/
Return
 
 
 
/* ------------------------------------------------------------ PRINTASA
 */
PRINTASA:
 
'ADDPIPE *.OUTPUT: | URO' dev
 
'PEEKTO LINE'
Do While rc = 0
    Parse Var line 1 byte 2 line
    line = byte || line
    'OUTPUT' line
    'READTO'
    'PEEKTO LINE'
    End  /*  Do  While  */
 
Return
 
 
 
/*
 
OVersize
    allows you to print:
 
    *  files that have records larger than the carriage size of the
       virtual printer, and
 
    *  files that have a SPECIAL status of YES.
 
    When the OVERSIZE option is used, the CC option will be set as
    a default.  This default setting of CC can be overridden by
    specifying either the NOCC or the HEX option with the OVersize
    option.
 
     If the file has a SPECIAL status of YES (and NOCC is not specified),
     any records with a carriage control character of x'5A' will be
     printed if all of the following conditions are true:
        - the record length is not greater than 32767 bytes.
        - a printer subsystem that handles the x'5A' carriage controller
          (such as the 3820 or 3800-3/8) is utilized.
        - a software package that handles such characters (such as PSF)
          is utilized.
     Otherwise, these records will not be printed.
 
     Other records that are larger than the virtual printer's carriage
     size are printed, but are truncated to the carriage size (or
     carriage size + 1 if CC is specified).
 
     (The SPECIAL status indicates whether or not the file contains records
     with X'5A' carriage control characters.  See the CP QUERY command to
     determine SPECIAL status of a file.)
 
    The OVERSIZE (and CC) option is assumed if the filetype is
    LISTCPDS, LIST3820, or LIST38PP.  If OVERSIZE is not specified and
    the file you want to print is larger than the virtual printer's
    carriage size, the message "Records exceeds allowable maximum"
    is displayed.
 
CC (HEADer)
    interprets the first character of each record as a carriage
    control character.  If the filetype is LISTING, LIST3800, or
    LISTCPDS, the CC option is assumed.  If CC is in effect, the PRINT
    command neither performs page ejects nor counts the number of
    lines per page; these functions are controlled by the carriage
    control characters in the file.  The LINECOUN option has no effect
    if CC is in effect.
 
    HEADER creates a shortened header page with only the filename,
    filetype, and filemode at the top of the page that follows the
    standard header page.  The records in the file being printed begin
    on a new page following both header pages.  The HEADER option can
    only be used in conjunction with the CC option.  If the CC option
    is not specified HEADER has no effect.
 
TRC
    interprets the first data byte in each record as a TRC (Table Ref-
    erence Character) byte.  The value of the TRC byte determines
    which translate table the 3800 printer selects to print a record.
    The value of the TRC byte corresponds to the order in which you
    have loaded WCGMs (via the CHARS keyword of the SETPRT command).
    Valid values for TRC are 0, 1, 2, and 3.  If an invalid value is
    found, a TRC byte of 0 is assumed.  If the filetype is LIST3800,
    TRC is assumed.
 
NOTRC
    does not interpret the first data byte in each record as a TRC
    byte.  NOTRC is the default.
 
MEMber    <*         >
          <membername>
    prints the members of macro or text libraries. This option may be
    specified if the file is a simulated partitioned data set
    (filetype MACLIB, TXTLIB, or LOADLIB).  If an asterisk (*) is
    entered, all individual members of that library are printed. If a
    membername is specified, only that member is printed.
 
HEX
    prints the file in graphic hexadecimal format.  If HEX is speci-
    fied, the options CC and UPCASE are ignored, even if specified,
    and even if the filetype is LISTING, LIST3800, LISTCPDS, LIST3820,
    or LIST38PP.  If both the OVersize and HEX options are specified,
    the NOCC option will be in effect.
 
 */
 
 
 
/* -- Here is a version of STANDARD that does not loop, requires
      pipes mod level 6 (for sync) */
STANDARD2:
header = '19'x || title
 
  'CALLPIPE (end \)',
    '| literal' '89'x,                /* page eject record?          */
    '| append var header',            /* page header record          */
    '| spec 1-* 1',                   /* simulate BLOCK LINEND by    */
    '       .15. x2c next',           /*   adding linend chars & join*/
    '| join *',                       /*     both recs into 1 rec    */
    '| dup *',                        /* make an endless supply      */
    ,
    '| a: sync',                      /* 2 streams marching together */
    '| b: faninany',                  /* combine the streams         */
    ,
    '| deblock linend',               /* deblock into separate recs  */
    '| uro' dev,                      /* print it                    */
    ,
    '\ *:',                           /* incoming records            */
    '| spec .09. x2c 1',              /* add charriage control and   */
    '       1-* next',                /*  simulate BLOCK LINEND by   */
    '       .15. x2c next',           /*    adding linend chars &    */
    '| join' linecount-1,     /* join all recs for a page into 1 rec */
    '| a:',                           /* send through sync           */
    '| b:'        /* sync sends them back, now send them to faninany */
 
Return
 
