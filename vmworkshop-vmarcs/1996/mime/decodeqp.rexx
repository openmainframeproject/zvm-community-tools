/*
 *        Name: DECODEQP REXX
 *              Quoted printable decoder stage.
 *      Author: Rick Troth, Rice University, Information Systems
 *        Date: 1993-Jul-10, and prior
 */
 
/*  Quoted printable encoding presumes ASCII.  */
'ADDPIPE *: | E2A | SPEC 1-* 1 x0D0A NEXT' ,
    '| SPLIT BEFORE' '003D00'x '| *.INPUT:'
 
/*  ASCII hexadecimal digits  */
xa = '30313233343536373839414243444546'x
/*  EBCDIC hexadecimal digits  */
xe = 'F0F1F2F3F4F5F6F7F8F9C1C2C3C4C5C6'x
 
Do Forever
 
    'PEEKTO RECORD'
    If rc ^= 0 Then Leave
 
    If Left(record,1) = '3D'x Then Select
        When Length(record) = 1 Then Do
            'READTO'
            'PEEKTO RECORD'
            If rc = 0 Then 'OUTPUT' record
            End  /*  When  ..  Do  */
        When Length(record) = 2 Then    /*  skip the quote char  */
            'OUTPUT' Substr(record,2)
        When Substr(record,2,2) = '0D0A'x Then  /*  skip the NL  */
            'OUTPUT' Substr(record,4)
        When Verify(Substr(record,2,2),xa) = 0 Then Do
            'OUTPUT' x2c(Translate(Substr(record,2,2),xe,xa))
            'OUTPUT' Substr(record,4)
            End  /*  When  ..  Do  */
        Otherwise
            'OUTPUT' Substr(record,2)
        End  /*  Select  */
    Else 'OUTPUT' record
 
    'READTO'
 
    End  /*  Do  Forever  */
 
Exit rc * (rc ^= 12)
 
