# SYSLOGS

```
SYSLOGS is the keeper of all system console logs which will
be compacted and archived to tape every Monday.

For a console to be included in the SYSLOGS archival tape,
spool a userid's console to SYSLOGS and make sure its
console is closed every day at midnight (ie update ALL@0000
EXEC on TIMERMNT).

TODISK EXEC

Nightly, SYSLOGS is autologged by TIMER and runs TODISK
EXEC. All reader files are placed on the 192-D disk with the
originating userid as the filename and the spool file
creation date (in YYMMDD format) as the filetype.

TIMER console files are scanned for idle users and those
lines are appended to the IDLE USERS file. This file is not
archived.

OPERATOR PROP logs are copied directly from OPERATOR 191 to
SYSLOGS 192 and scanned to generate MUSIC bad password
reports (PASSALL and PASSDATA YYMMDD). The OPERATOR 191
minidisk is then cleared.

TOVMARC EXEC

Mondays at 11am, SYSLOGS is autologged by TIMER and runs
TOVMARC EXEC to package system logs into daily files. It
first erases the previous week's VMARC files on the A-disk,
packs all files on the D-disk and then runs VMARC PACK for
every day except TODAY. Finally, all files on the D-disk are
erased except for TODAY's files.

TOTAPE EXEC

Simply takes all VMARC files and dumps them to tape using
VMFPLC2 and its  compression option. The current tape is
kept in Anne-Marie's box in the machine room, this procedure
is run manually after TOVMARC completes.

RTOTAPE EXEC

The next step towards automation. The 3494 is used to dump
VMARC files to tape using VMFPLC2 with the 3490C compression
option. The current tape is in the Robot, name is VMLGxx,
where xx = 01, 02, ..., 99. TIMER will start this job after
we have found a reliable way to share the drives between VM
and MVS.

TOVMARC TOTAPE

This file is updated by both TOVMARC and TOTAPE to ensure
the compacted data is written to tape before it is erased.
The second line contains the current VMLGxx tape number.

CHECKLOG EXEC

This utility was thrown together in record time to extract
records from huge console logs which cannot be edited. Usage
is:

  CHECKLOG userid yymmdd hh:mm:ss nbrlines



Naming convention

Console files are named ORIGINID YYMMDD

Archival files are named YYMMDD VMARC

Extracting a file from tape

vmfplc2 load 950130 vmarc (eot          find desired day and
load

vmarc list 950130 vmarc                 list contents of
archive

vmarc unpk 950130 vmarc a smtp * a      to extract only smtp
950130

or

vmarc unpk 950130 vmarc                 to unpack all files



The resulting file(s) will be in CMS packed format. XEDIT
handles packed files just fine but PRINT doesn't, so do:

copy smtp 950130 (unpack

print smtp 950130             beware! that might be a lot of output



                                Anne-Marie Marcoux        95/06/06
                                (514) 398-3708

                                marie@vm1.mcgill.ca

                                McGill University Computing Centre
                                805 Sherbrooke West, room 218
                                Montreal, Quebec, Canada
                                H3A 2K6
```
