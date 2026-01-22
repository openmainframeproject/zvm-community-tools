/*
 *        Name: ENBASE64 REXX
 *              a CMS Pipelines stage to convert the binary
 *              input stream into Base 64 encoding (see MIME)
 *      Author: Rick Troth, Rice University, I/S VM Systems Support
 *        Date: 1992-Jul-31
 */
 
'ADDPIPE *: | FBLOCK 3 00' ,            /* pad with NULLs */
           '| SPEC 1-3 C2B' ,           /* convert to binary */
           '| SPEC "00"  1  1.6  3' ,   /* select 6 bits from 8 */
                  '"00"  9  7.6 11' ,
                  '"00" 17 13.6 19' ,
                  '"00" 25 19.6 27' ,
           '| SPEC  1.8 B2C 1' ,        /* convert to character */
                   '9.8 B2C 2' ,
                  '17.8 B2C 3' ,
                  '25.8 B2C 4' ,
           '| FBLOCK 64' ,              /* reblock nicely */
           '| *.INPUT:'
 
b64 = ""; Do i = 0 to 63; b64 = b64 || d2c(i); End
e64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
 
'PEEKTO LINE'
Do While rc = 0
    /* translate binary 6-bit into plain text B64 set */
    'OUTPUT' Translate(line,e64,b64)
    'READTO'
    'PEEKTO LINE'
    End
 
Return
 
