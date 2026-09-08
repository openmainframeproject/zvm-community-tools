# ibm-cray(3,L) - IBM-Cray data conversion

"", 3 June 1991


<a name="purpose-"></a>

# Purpose

Converts arrays of floating point numbers between IBM and Cray data formats.

<a name="library"></a>

# Library

faux, Cornell's Fortran Auxiliary Subroutine Library (libfaux.a)

<a name="syntax"></a>

# Syntax

```
call  cfdc(ibm, cray, n)

call  cfcd(cray, ibm, n)

where:
      ibm   Array of IBM floating point numbers, REAL*8 values.
      cray  Array of CRAY floating point numbers.
      n     Number of elements in arrays to convert, integer.
```

<a name="description"></a>

# Description

cfdc converts floating point double precision numbers to Cray floating point numbers

cfcd converts floating point Cray numbers to floating point double precision IBM numbers

Routines are written in VS FORTRAN and thus are available for both CMS and AIX/370 systems. They could be compiled by either 'fortvs' command under VM/CMS or 'fvs' command under AIX/370.

Precision of the conversion is the best possible. When floating point formats differ in number of bits for mantissa, which affects data precision, the least mantissa bits are rounded.  When formats differ in number of bits for exponent, which affects the range of data, the biggest possible value or zero value is assigned if the old number can't be represented.

Routines convert data in memory and must be invoked with three arguments: input array name, output array name, and number of elements in each of two arrays.  When called from a C program, the last parameter must be passed by the pointer. The same variable name can be used for the first and the second arguments. This means that conversion can be done "in place" thus saving memory space, if necessary.

The table below shows a summary of conversion time per element in microseconds of virtual cpu time on a 3090 J processor.  Each entry represents the average value of one thousand conversions of an array with a thousand elements.

```
----------------------------------
| Routine name | Time to convert |
----------------------------------
| cfdc         |     0.83        |
| cfcd         |     0.75        |
----------------------------------
```

<a name="notes"></a>

# Notes

1. Non-normalized numbers with zero exponents are kept  intact.

2. In IBM to CRAY conversion, precision in the mantissa could be lost by rounding off the least significant bits.  0 &lt;= |error| &lt;= .18E-14 (From 5 to 8 least significant bits out of 56 mantissa bits could be rounded.)

3. CRAY to IBM conversion does not incur the lost of mantissa accuracy.

4. CRAY values that don't fit IBM standard are converted to either the biggest IBM values (positive or negative) or to zero.
