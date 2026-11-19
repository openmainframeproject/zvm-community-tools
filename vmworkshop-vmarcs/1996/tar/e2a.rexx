/* ----------------------------------------------------------------- ÆCS
 * ASCII to EBCDIC and vice-versa code conversion tables.
 * Tables included here are based on ASCII conforming to the ISO8859-1
 * Latin 1 character set and EBCDIC conforming to the IBM Code Page 37
 * Latin 1 character set (except for three pairs of characters in 037).
 *
 *        Name: E2A REXX
 *              CMS Pipelines filter to translate EBCDIC to ASCII
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
 
/* ----------------------------------------------------------------- E2A
 * Translate EBCDIC to ASCII.
 */
Do Forever
    'PEEKTO LINE'
    If rc ^= 0 Then Leave
    'OUTPUT' Translate(line,a,i)
    If rc ^= 0 Then Leave
    'READTO'
    End  /*  Do  While  */
 
Exit rc * (rc ^= 12)
 
