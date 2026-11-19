/* Copyright 1994, Richard M. Troth, all rights reserved.    <plaintext>
 *
 *        Name: MIMEPART REXX
 *              process one part of a multipart MIME message
 *              (merge parent header; eliminated empty bodies)
 *      Author: Rick Troth, Rice University, Information Systems
 *        Date: 1993-May-20
 *
 *        Note: this stage reads the parent's header from its
 *              secondary input stream  (number 1; primary is #0)
 *              and prepends that to any header in the child part.
 *              One effect is multiple  Content-Type  header lines.
 *              This is okay because only the last  Content-Type
 *              is recognized  (unless you try to export these files
 *              to certain other MIME-capable mail readers).
 *
 *        Note: files created by this stage should be feed to MIMEREAD.
 */
 
Parse Arg fn q . '(' . ')' .
If fn = "" Then Exit -1
 
/*  clear the "content-type" by tacking on our own empty one  */
'CALLPIPE *.INPUT.1: | APPEND LITERAL Content-Type: | STEM HEAD.'
If rc ^= 0 Then i = 0
           Else i = head.0
 
tag = "N/A"
content = "MESSAGE"
 
Do Forever
 
    'PEEKTO LINE'
    /*  watch for end-of-file  */
    If rc ^= 0 Then Leave
 
    /*  eliminate TAB characters in the header  */
    line = Translate(line,' ','05'x)
 
    /*  watch for end-of-header  */
    If Strip(line) = "" Then Leave
 
    If Left(line,1) = ' ' Then val = val Strip(line)
    Else Do;  Parse Var line tag val;  Upper tag;  End
 
    If Right(tag,1) ^= ':' Then Leave
 
    If tag = "CONTENT-TYPE:" Then content = val
    /*  all other tags ignored  */
 
    i = i + 1
    head.i = line
    'READTO'        /*  consume this record  */
 
    End  /*  Do  While  */
 
If rc ^= 0 Then Exit rc * (rc ^= 12)
 
head.0 = i
 
/*  discard all blank lines after the header  */
Do Forever
    'PEEKTO LINE'
    If rc ^= 0 Then Leave
    If Strip(Translate(line,' ','05'x)) ^= "" Then Leave
    'READTO'        /*  consume this record  */
    End  /*  Do  Forever  */
If rc ^= 0 Then Exit rc * (rc ^= 12)
 
If content = "" Then content = "MESSAGE"
Parse Upper Value Strip(content) With content ';' .
Parse Var content major '/' minor
ft = major
If content = "MESSAGE/EXTERNAL-BODY" Then ft = "MSGFETCH"
 
If ^Datatype(q,'W') Then q = 0
If q = 0 Then 'ADDPIPE *.OUTPUT: | HOLE'
         Else 'ADDPIPE *.OUTPUT: | >' fn ft 'A'
'CALLPIPE STEM HEAD. | *:'
'OUTPUT' " "
If rc ^= 0 Then Exit rc
 
/*  a simple "short" doesn't always work here;  why?  */
'CALLPIPE *: | *:'
If rc ^= 0 Then Exit rc
 
'SEVER OUTPUT'
 
Exit
 
