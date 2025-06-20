/* Copyright 1994, Richard M. Troth                          <plaintext>
 *
 *        Name: WEBTEXT REXX
 *              VM TCP/IP Network Client and Server text converter
 *              Inspired by GOPCLITX, DROPDOTS, and others.
 *              To be renamed MAKETEXT because it's ubiquitous.
 *      Author: Rick Troth, Houston, Texas, USA
 *        Date: 1994-Feb-27, 1994-Oct-15
 *
 *    Replaces: A2E, E2A, TCPA2E, TCPE2A
 */
 
/* ----------------------------------------------------------------- ÆCS
 * ASCII to EBCDIC and vice-versa code conversion tables.
 * Tables included here are based on ASCII conforming to the ISO8859-1
 * Latin 1 character set and EBCDIC conforming to the IBM Code Page 37
 * Latin 1 character set (except for three pairs of characters in 037).
 */
 
Parse Upper Arg mode code .
If mode = "" Then mode = "LOCAL"
 
    i =      '000102030405060708090A0B0C0D0E0F'x
    i = i || '101112131415161718191A1B1C1D1E1F'x
    i = i || '202122232425262728292A2B2C2D2E2F'x
    i = i || '303132333435363738393A3B3C3D3E3F'x
    i = i || '404142434445464748494A4B4C4D4E4F'x
    i = i || '505152535455565758595A5B5C5D5E5F'x
    i = i || '606162636465666768696A6B6C6D6E6F'x
    i = i || '707172737475767778797A7B7C7D7E7F'x
    i = i || '808182838485868788898A8B8C8D8E8F'x
    i = i || '909192939495969798999A9B9C9D9E9F'x
    i = i || 'A0A1A2A3A4A5A6A7A8A9AAABACADAEAF'x
    i = i || 'B0B1B2B3B4B5B6B7B8B9BABBBCBDBEBF'x
    i = i || 'C0C1C2C3C4C5C6C7C8C9CACBCCCDCECF'x
    i = i || 'D0D1D2D3D4D5D6D7D8D9DADBDCDDDEDF'x
    i = i || 'E0E1E2E3E4E5E6E7E8E9EAEBECEDEEEF'x
    i = i || 'F0F1F2F3F4F5F6F7F8F9FAFBFCFDFEFF'x
 
If code ^= "" Then Do
    'CALLPIPE DISK' code 'TCPXLBIN | STEM XLT.'
    If rc ^= 0 | xlt.0 < 3 Then code = ""
    End  /*  If  ..  Do  */
 
Select  /*  mode  */
    When Abbrev("LOCAL",mode,3)    Then Call LOCAL
    When Abbrev("LCL",mode,3)      Then Call LOCAL
    When Abbrev("NETWORK",mode,3)  Then Call NETWORK
    When Abbrev("DOTTED",mode,3)   Then Call DOTTED
    Otherwise Do
        Address "COMMAND" 'XMITMSG 3 MODE (ERRMSG'
        rc = 24
        End  /*  Otherwise Do  */
    End  /*  Select  mode  */
 
Exit rc * (rc ^= 12)
 
 
/* --------------------------------------------------------------- LOCAL
 *       Input: raw ASCII text
 *      Output: plain (EBCDIC) text
 */
LOCAL:
 
'ADDPIPE *.OUTPUT: | STRIP TRAILING 0D | PAD 1 | *.OUTPUT:'
If rc ^= 0 Then Return
 
If code = "" Then Do  /*  use the standard table  */
    e =      '00010203372D2E2F1605250B0C0D0E0F'x
    e = e || '101112133C3D322618193F271C1D1E1F'x
    e = e || '405A7F7B5B6C507D4D5D5C4E6B604B61'x
    e = e || 'F0F1F2F3F4F5F6F7F8F97A5E4C7E6E6F'x
    e = e || '7CC1C2C3C4C5C6C7C8C9D1D2D3D4D5D6'x
    e = e || 'D7D8D9E2E3E4E5E6E7E8E9ADE0BD5F6D'x
    e = e || '79818283848586878889919293949596'x
    e = e || '979899A2A3A4A5A6A7A8A9C04FD0A107'x
    e = e || '202122232415061728292A2B2C090A1B'x
    e = e || '30311A333435360838393A3B04143EFF'x
    e = e || '41AA4AB19FB26AB5BBB49A8AB0CAAFBC'x
    e = e || '908FEAFABEA0B6B39DDA9B8BB7B8B9AB'x
    e = e || '6465626663679E687471727378757677'x
    e = e || 'AC69EDEEEBEFECBF80FDFEFBFCBAAE59'x
    e = e || '4445424643479C485451525358555657'x
    e = e || '8C49CDCECBCFCCE170DDDEDBDC8D8EDF'x
    End  /*  If  ..  Do  */
Else e = xlt.2
 
buff = ""
Do Forever
 
    'PEEKTO DATA'
    If rc ^= 0 Then Leave
 
    buff = buff || data
    Do While Index(buff,'0A'x) > 0
        Parse Var buff line '0A'x buff
        'OUTPUT' Translate(line,e,i)
        If rc ^= 0 Then Leave
        End  /*  Do  While  */
    If rc ^= 0 Then Leave
 
    'READTO'
    If rc ^= 0 Then Leave
 
    End  /*  Do  Forever  */
 
If buff ^= "" Then 'OUTPUT' Translate(buff,e,i)
 
Return
 
 
/* ------------------------------------------------------------- NETWORK
 *       Input: plain (EBCDIC) text
 *      Output: raw ASCII byte stream
 */
NETWORK:
 
'ADDPIPE *.OUTPUT: | SPEC 1-* 1 x0D0A NEXT | *.OUTPUT:'
If rc ^= 0 Then Return
 
If code = "" Then Do  /*  use the standard table  */
    a =      '000102039C09867F978D8E0B0C0D0E0F'x
    a = a || '101112139D8508871819928F1C1D1E1F'x
    a = a || '80818283840A171B88898A8B8C050607'x
    a = a || '909116939495960498999A9B14159E1A'x
    a = a || '20A0E2E4E0E1E3E5E7F1A22E3C282B7C'x
    a = a || '26E9EAEBE8EDEEEFECDF21242A293B5E'x
    a = a || '2D2FC2C4C0C1C3C5C7D1A62C255F3E3F'x
    a = a || 'F8C9CACBC8CDCECFCC603A2340273D22'x
    a = a || 'D8616263646566676869ABBBF0FDFEB1'x
    a = a || 'B06A6B6C6D6E6F707172AABAE6B8C6A4'x
    a = a || 'B57E737475767778797AA1BFD05BDEAE'x
    a = a || 'ACA3A5B7A9A7B6BCBDBEDDA8AF5DB4D7'x
    a = a || '7B414243444546474849ADF4F6F2F3F5'x
    a = a || '7D4A4B4C4D4E4F505152B9FBFCF9FAFF'x
    a = a || '5CF7535455565758595AB2D4D6D2D3D5'x
    a = a || '30313233343536373839B3DBDCD9DA9F'x
    End  /*  If  ..  Do  */
Else a = xlt.3
 
Do Forever
 
    'PEEKTO LINE'
    If rc ^= 0 Then Leave
 
    'OUTPUT' Translate(line,a,i)
    If rc ^= 0 Then Leave
 
    'READTO'
    If rc ^= 0 Then Leave
 
    End  /*  Do  Forever  */
 
Return
 
 
/* -------------------------------------------------------------- DOTTED
 *       Input: plain (EBCDIC) text
 *      Output: ASCII byte stream terminated by CR/LF/./CR/LF
 */
DOTTED:
 
Call NETWORK
 
'OUTPUT' Translate('.',a,i)
 
Return
 
 
/*
 * variables:
 *              xlt.0   should be "3",  meaning three records read
 *              xlt.1   should be a comment
 *              xlt.2   should be our ASCII ---> EBCDIC table
 *              xlt.3   should be our EBCDIC ---> ASCII table
 *              i       is set to the dummy input table
 */
 
