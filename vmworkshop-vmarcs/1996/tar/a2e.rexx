/* ----------------------------------------------------------------- ÆCS
 * ASCII to EBCDIC and vice-versa code conversion tables.
 * Tables included here are based on ASCII conforming to the ISO8859-1
 * Latin 1 character set and EBCDIC conforming to the IBM Code Page 37
 * Latin 1 character set (except for three pairs of characters in 037).
 *
 *        Name: A2E REXX
 *              CMS Pipelines filter to translate ASCII to EBCDIC
 *      Author: Rick Troth, Houston, Texas, USA 
 *        Date: 1992-Feb-27 for the filter, earlier for the table
 *
 * 1993-Aug-28: Thanks to Melinda Varian for helping me to
 *              correct some pipelining errors in this gem.
 *
 *        Note: These tables are provided in source form so that you
 *              may modify them locally.  I recommend that you not
 *              modify them just to make things look right on your
 *              screen.  If you have an older terminal and there are
 *              not more than a dozen code-points that are wrong,
 *              then you're better off using CODEPAGE EXEC to set the
 *              CMS INPUT/OUTPUT translate tables.   GOPHER EXEC
 *              *does respect*  CMS' translate tables.
 */
 
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
 
/* ----------------------------------------------------------------- A2E
 * Translate ASCII to EBCDIC.
 */
Do Forever
    'PEEKTO LINE'
    If rc ^= 0 Then Leave
    'OUTPUT' Translate(line,e,i)
    If rc ^= 0 Then Leave
    'READTO'
    End  /*  Do  While  */
 
Exit rc * (rc ^= 12)
 
