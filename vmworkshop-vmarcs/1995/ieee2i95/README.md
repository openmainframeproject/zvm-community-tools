# IBM TO/FROM IEEE FORMAT CONVERSION ROUTINES

Original: 09/13/89
Last version: 08/08/90
vig@eagle.cnsf.cornell.edu

A set of subroutines callable from Fortran and C programs to convert arrays of floating point numbers between IBM and IEEE formats is available for our users at the CNSF.

CFSI32 -- convert floating point single precision IBM data format to IEEE 32 bit long format

CFDI64 -- convert floating point double precision IBM data format to IEEE 64 bit long format

CFDI32 -- convert floating point double precision IBM data format to IEEE 32 bit long format

CFI32S -- convert floating point IEEE 32 bit long format to a single precision IBM data format

CFI64D -- convert floating point IEEE 64 bit long format to a double  precision IBM data format

CFI32D -- convert floating point IEEE 32 bit long format to a double precision IBM data format

All routines are written in VS FORTRAN and thus are available for both CMS and AIX/370 systems. They could be compiled by either 'fortvs' command under VM/CMS or 'fvs' command under AIX/370.  Versions of these same routines written in System/370 Assembly language are also available under both CMS ('hasm' command to compile) and AIX conventions ('as' command to compile) which ensure efficient object code. Versions in C are available for portability with other systems.

Object code (TEXT) of routines is kept in FORTAUX TXTLIB library for VM/CMS and in usr/local/pp/lib/libfaux.a for AIX/370.  Both include codes of routines originally written in System/370 Assembly.

Precision of the conversion is the best possible. When floating point formats differ in number of bits for mantissa, which affects data precision, the least mantissa bits are rounded (as oppose to truncated). When formats differ in number of bits for exponent, which affects the range of data, the biggest possible value or zero value is assigned if the old number can't be represented.

Routines convert data in memory and must be invoked with three arguments: input array name, output array name, and number of elements in each of two arrays.  When called from a C program, the last parameter must be passed by the pointer. The same variable name can be used for the first and the second arguments. This means that conversion can be done "in place" thus saving memory space, if necessary.

## EXAMPLE
```
call cfsi32(ibm, ieee, n)

where
      ibm    input array of IBM floating point numbers, REAL*4 values.
      n      number of elements in ibm to convert, integer.
      ieee   output array of 32-bit IEEE floating point numbers, single precision.
```

## NOTES

  1. IBM values that do not "fit" to IEEE standard are converted to
     either infinite IEEE values (positive or negative)  or to zero.

  2. Non-normalized with zero exponent IBM values are not converted.

  3. Using CFSI32, CFI32D, CFI64D  does not incur the loss of mantissa accuracy.

     Precision in the mantissa could be lost by rounding off from 0 to 3 least significant bits when using CFDI64 and/or CFI32S.

     Precision in the mantissa could be lost by rounding off from from 29 to 32 least significant bits when using CFDI32.

Details specific to each routine could be found in comments at the top of its source.

The table below shows a summary of conversion time per element in microseconds of virtual CPU time on a 3090 J processor under VM/CMS. Each entry represents the average value of one thousand conversions of an array with a thousand elements.

```
 ---------------------------------------------------------------------
 | Program name | Assembly version  | VS FORTRAN version | C version |
 ---------------------------------------------------------------------
 | cfi32s       |     0.67          |     2.26           |    1.02   |
 | cfsi32       |     0.78          |     1.56           |    1.29   |
 | cfi32d       |     0.64          |     2.97           |    1.25   |
 | cfdi32       |     0.98          |     4.09           |    1.53   |
 | cfi64d       |     0.73          |     3.29           |    3.28   |
 | cfdi64       |     0.80          |     3.83           |    3.82   |
 ---------------------------------------------------------------------
```
