/*
 *        Name: DEBASE64 REXX
 *              a CMS Pipelines stage to convert Base 64
 *              encoding into the original binary stream
 *      Author: Rick Troth, Rice University, Information Systems
 *        Date: 1992-Jul-31, 1993-Apr-09
 */
 
/*  b64 = ""; Do i = 0 to 63; b64 = b64 || d2c(i); End  */
e64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
table = ""
Do i = 1 to 64
    table = table c2x(Substr(e64,i,1)) d2x(i-1,2)
    End
 
xlate = 'XLATE *-*' table ,             /*  translate  */
            '| SPEC 1-4 C2B' ,          /* convert to binary */
            '| SPEC  3.6  1' ,          /* combine 8 bits from 6 */
                   '11.6  7' ,
                   '19.6 13' ,
                   '27.6 19' ,
            '| SPEC  1.8 B2C 1' ,       /* convert to character */
                    '9.8 B2C 2' ,
                   '17.8 B2C 3'
 
'CALLPIPE (END !) *: | SPLIT |' ,       /*  remove blanks  */
    'SPLIT AT * | OUTSIDE /*/ /*/ |' ,  /*  ignore OOB data  */
    'FBLOCK 4 = |' ,                    /*  pad,  just in case  */
    'E: NLOCATE /=/ |' xlate '|' ,      /*  watch for padding  */
    'F: FANINANY | FBLOCK 4094 | *:' ,  /*  recombine streams  */
    '! E: | D: NLOCATE /==/ |' ,        /*  watch for double padding  */
        xlate '| SPEC 1.2 1 | F:' ,     /*  take two bytes  */
    '! D: |' xlate '| SPEC 1.1 1 | F:'  /*  take one byte  */
 
Exit rc
 
