## ORIGINAL README
```
Copyright 1993, 1996, Richard M. Troth, all rights reserved.

This is the README file for MAILCONVERT.
See the supplied HELP file for command syntax.

TRANSFER YOUR UNIX MAILBOX/NOTEBOOK FILES IN BINARY.

Strict interpretation of RFC 822 defines the break between the header
and the body of each mail message as  CRLFCRLF,  *not* a blank line.
This means that that blank line between header and body must not have
any TABs or SPACEs in it.   The CMS minidisk filesystem does not provide
for truly empty lines;  empty lines in CMS (on minidisks) have at least
a space character.   (Pipelines and SFS, however, do allow null records)

Pine is not happy with UNIX mbox output from MAILCONVERT.
If someone can figure out exactly what Pine is displeased about,
please send mail to  troth@compassnet.com.
```
