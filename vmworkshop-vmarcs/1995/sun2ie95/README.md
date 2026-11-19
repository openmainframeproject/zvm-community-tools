# ibm-sun(3,L) - IBM-Sun data conversion

"", 3 June 1991


<a name="purpose"></a>

# Purpose

Converts SUN 386i workstation floating point data to a regular IEEE format for further use in computation.  Assumes the data have been transferred from the workstation in binary format using ftp.

<a name="library"></a>

# Library

faux, Cornell's Fortran Auxiliary Library (libfaux.a)

<a name="syntax"></a>

# Syntax

```
call drvsun(sund, ieee64, n)

  where:
       sund   -- SUN array of double words
       ieee64 -- array of regular IEEE double presision numbers
       n      -- number of double words to convert

call srvsun(suns, ieee32, m)

  where:
       suns   -- SUN array of single words
       ieee32 -- array of regular IEEE single presision numbers
       m      -- number of words to revolve.
```

<a name="description"></a>

# Description

Calling these routines you can convert (actually Revolve) bytes in double words of SUN 386i workstation data so that they are available for further use as regular IEEE format data.

The SUN 368i keeps every single data element (integer, logical, and real*4 in words and real*8 in double words) in bytes "from higher addresses to lower addresses" which is opposite to what other computers do.

<a name="notes"></a>

# Notes

1. Input and output data could be located at the same space.
2. Twice reversed data returns to its source.
