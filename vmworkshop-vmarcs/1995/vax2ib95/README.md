# IBM TO/FROM VAX FORMAT CONVERSION ROUTINES

vig@cornellf 08/15/90

A set of subroutines callable from Fortran and C programs to convert arrays of floating point numbers between IBM and VAX data formats is available at the CNSF.

CFSV32 -- convert floating point single precision IBM data format to VAX 32 bit long format

CFDV64 -- convert floating point double precision IBM data format to VAX 64 bit long format

CFDV32 -- convert floating point double precision IBM data format to VAX 32 bit long format

CFV32S -- convert floating point VAX 32 bit long format to a single precision IBM data format

CFV64D -- convert floating point VAX 64 bit long format to a double precision IBM data format

CFV32D -- convert floating point VAX 32 bit long format to a double precision IBM data format

All routines are written in VS FORTRAN and thus are available for both CMS and AIX/370 systems. They could be compiled by either 'fortvs' command under VM/CMS or 'fvs' command under AIX/370.

Precision of the conversion is the best possible. When floating point formats differ in number of bits for mantissa, which affects data precision, the least mantissa bits are rounded.  When formats differ in number of bits for exponent, which affects the range of data, the biggest possible value or zero value is assigned if the old number can't be represented.

Routines convert data in memory and must be invoked with three arguments: input array name, output array name, and number of elements in each of two arrays.  When called from a C program, the last parameter must be passed by the pointer. The same variable name can be used for the first and the second arguments. This means that conversion can be done "in place" thus saving memory space, if necessary.

## EXAMPLE

```
call cfsv32(ibm, vax, n)

where:
    ibm    input array of IBM floating point numbers, REAL*4 values.
    n      number of elements in ibm to convert, integer.
    vax    output array of 32-bit VAX floating point numbers, single precision.
```
