# zvm-community-tools
These are tools for z/VM, many based on Linux commands.

Some emulate commonly used Linux commands such as ``diff``, ``grep``, ``man``, ``rm``, ``wc`` and ``who``. Others are more specific to z/VM such as ``calcdasd``, ``copydisk``, ``cpformat`` and ``ssicmd``.  

The following EXECs for z/VM are in this directory: 

    +------------------+-------------------------------------------------+
    | File             | Description                                     |
    |------------------|-------------------------------------------------|
    | CALCDASD EXEC    | Calculate total DASD space and types            |
    | CALCOSA  EXEC    | Calculate free and used OSA and verify PCHIDs   |
    | CFM      EXEC    | Copy file with new file mode                    |
    | CFN      EXEC    | Copy file with new file name                    |
    | CFT      EXEC    | Copy file with new file type                    |
    | COPYDISK EXEC    | Copy disk with FLASHCOPY if not DDR             |
    | CPFORMAT EXEC    | Format one or more DASD and label               |
    | DIFF     EXEC    | Compare files line by line                      |
    | GREP     EXEC    | Search for patterns in files                    |
    | HEAD     EXEC    | Output the first part of files                  |
    | HISTORY  EXEC    | Display list of commands previously run         |
    | MAN      EXEC    | Give help on CMS/CP/XEDIT/TCPIP/REXX commands   |
    | MKVMARC  EXEC    | Create the VMARC file with all EXECs inside     |
    | QA       EXEC    | Run QUERY ACCESSED                              |
    | RFN      EXEC    | Rename file changing only file name             |
    | RFT      EXEC    | Rename file changing only file type             |
    | RM       EXEC    | Remove files allowing wildcards                 |
    | SPC      EXEC    | Spool console to reader then restart            |
    | SSICMD   EXEC    | Run CP commands on multiple SSI members         |
    | TAIL     EXEC    | Output the last part of files                   |
    | WC       EXEC    | Count lines, words and bytes in files           |
    | WHICH    EXEC    | Resolve CMS/CP/XEDIT/TCPIP/REXX commands        |
    | WHO      EXEC    | Show who is logged on and allow a pattern       |
    +------------------+-------------------------------------------------+
## Installation
You can install to z/VM or by using Linux as an intermediate step.

### Installation on z/VM
To install on z/VM, perform the following steps:

If you do not have the ``VMARC MODULE``:
- Download it from: ``https://www.vm.ibm.com/download/vmarc.module``
- Upload the file to CMS in BINARY (usually ``ftp``, then ``bin``, then ``put vmarc.module``)
- Run it through this pipeline:

```
PIPE < VMARC MODULE A | deblock cms | > VMARC MODULE A
```

Then:
- Download ``ZVMEXECS.VMARC`` (the link is above) to your workstation.
- Get it to z/VM in binary, either with FTP (using ``bin``, ``quote site fix 80``, then ``put ZVMTOOLS.VMARC``), or using another tool such as ``IND$FILE``.
- Unpack it: 

```
vmarc unpk zvmexecs.vmarc
```
All the files should now be accessible on your ``A`` disk.

## Installation through Linux
To install the tools using Linux, the VMARC file is not used.
Perform the following steps:

- Clone it from github:

```
$ git clone https://github.com/openmainframeproject/zvm-community-tools
```

- Change to the new directory and copy the tools to z/VM with ``ftp`` or ``IND$FILE``.
 

## REXX EXECs
Following are descriptions of each REXX EXEC.

### CALC EXEC
The ``CALC EXEC`` calculates a numerical expression. 

- Here is the help:
```
calc -h                                    
Name:  CALC - calculate a numerical expression  
Usage: CALC expression                          
Exmpl: CALC 5 + 6                               
```

- Here is an example of using it:
```
calc 21 * 5                                     
21 * 5 = 105                                    
```

### CALCDASD EXEC
The ``CALCDASD EXEC`` calculates the size of all disk space. 

- Here is the help:
```
calcdasd -h                                    
Name:  CALCDASD EXEC - compute total disk space
Usage: CALCDASD                                
```

- Here is an example of using it:

```
calcdasd                                             
Warning - non standard size: 31A2 has 18000 cylinders
Warning - non standard size: 3A97 has 18000 cylinders
Warning - non standard size: 3AA2 has 18000 cylinders
Number of 3390-1s    (1113 cylinders): 0             
Number of 3390-2s    (2226 cylinders): 0             
Number of 3390-3s    (3339 cylinders): 222           
Number of 3390-9s   (10017 cylinders): 76            
Number of 3390-27s  (30051 cylinders): 8             
Number of 3390-32Ks (32760 cylinders): 0             
Number of 3390-54s  (60102 cylinders): 0             
Number of 3390-64Ks (65520 cylinders): 0             
Number of 3390-As       (other sizes): 5             
                                                     
Total CP-Owned cylinders: 40068 (31.72 GiB)          
Total SYSTEM   cylinders: 1892676 (1498.22 GiB)      
```

### CALCOSA EXEC
The ``CALCOSA EXEC`` merges free and used OSAs by ``rdev`` and verifies the CHPIDs and PCHIDs. 

- Here is the help:
```
calcosa -h                                       
Name:  CALCOSA EXEC - compute OSA statistics     
Usage: CALCOSA [(v|verbose]                      
```
By including the ``(V`` verbose flag, free OSAs will be shown also.

- Here is an example of using it:

```
calcosa                                              
Rdev  UserID    Vdev  DevType  OSAtype  CHPID  PCHID   
----  ------    ----  -------  -------  -----  -----   
0340  DTCVSW1   0600  OSA      OSD      F0     NONE    
0341  DTCVSW1   0601  OSA      OSD      F0     NONE    
0342  DTCVSW1   0602  OSA      OSD      F0     NONE    
1340  DTCVSW2   0600  OSA      OSD      F1     NONE    
1341  DTCVSW2   0601  OSA      OSD      F1     NONE    
1342  DTCVSW2   0602  OSA      OSD      F1     NONE    
                                                       
Used OSAs:    6                                        
Free OSAs:    3                                        
           ----                                        
    Total:    9                                        
```

### CFM EXEC
The ``CFM EXEC`` copies a file just changing the file mode. 
- Here is the help:
```
cfm -h                                                       
Name:  CFM EXEC - Copy file changing only file mode          
Usage: CFM fn1 ft1 fm1 fm2 ['('options')']                   
Where: 'fn1 ft1 fm1' is the source file:                     
       'fm2' is the target file mode                         
       'options' add to COPY command such as 'REP' or 'OLDD' 
```

For example, if you want to copy the file ``COPYDISK EXEC A`` to your B disk, you can type ``cfm b copydisk exec a``, but if your in a ``FILELIST``, you can simply type ``cfm b`` next to it, as the ``FN FT FM`` will be automatically added to the end.

### CFN EXEC
The ``CFN EXEC`` copies a file just changing the file name.

- Here is the help:
```
cfn -h                                                       
Name:  CFN EXEC - Copy file changing only file name          
Usage: CFN fn2 fn1 ft1 fm1 ['('options')']                   
Where: 'fn2' is the target file name                         
       'fn1 ft1 fm1' is the source file:                     
       'options' add to COPY command such as 'REP' or 'OLDD' 
```

- Here is an example of using it from within FILELIST to copy an EXEC with a new file name of ``FOO``:

```
 MIKEMAC  FILELIST A0  V 169  Trunc=169 Size=50 Line=1 Col=1 Alt=0              
Cmd   Filename Filetype Fm Format Lrecl    Records     Blocks   Date     Time   
cfn foo LCOSA  EXEC     A1 V         73        233          3  2/08/25  5:48:42 
```


### CFT EXEC
The ``CFT EXEC`` copies a file just changing the file type.

- Here is the help:
```
cft -h                                                         
Name:  CFT EXEC - Copy file changing only file type            
Usage: CFT ft2 fn1 ft1 fm1 ['('options')']                     
Where: 'ft2' is the target file type                           
       'fn1 ft1 fm1' is the source file:                       
       'options' add to COPY command such as 'REP' or 'OLDD'   
```

### COPYDISK EXEC
The ``COPYDISK EXEC`` first tries to copy a disk with ``FLASHCOPY`` and if that fails, falls back to ``DDR``.

- Here is the help:
```
copydisk ?                                                   
Name:  COPYDISK EXEC - copy minidisk with FLASHCOPY or DDR   
Usage: COPYDISK source_vdev target_vdev                      
```

### CPFORMAT EXEC
The ``CPFORMAT EXEC`` formats one or more DASD volumes using ``CPFMTXA``.

- Here is the help:
```
cpformat ?                                                     
Name: CPFORMAT EXEC                                            
 Format and label DASD as page, perm, spool or temp disk space 
 The label written to each DASD is J<t><xxxx> where:           
 <t> is type - P (page), M (perm), S (spool) or T (Temp disk)  
 <xxxx> is the 4 digit address                                 
Syntax:                                                        
             <---------------<                                 
 >>--CPFORMAT--.-vdev--------.--AS---.-PERM-.---------><       
               '-vdev1-vdev2-'       '-PAGE-'                  
                                     '-SPOL-'                  
                                     '-TEMP-'                  
```

### DIFF EXEC
The ``DIFF EXEC`` compares two files and shows the results with color.

- Here is the help:
```
diff -h                                            
Name : DIFF EXEC - compare two files               
Usage: diff fn1 ft1 fm1 fn2 ft2 fm2 [( flags )]    
Where: 'fn1 ft1 fm1' is the first file to compare  
       'fn2 ft2 fm2' is the second file to compare 
Where: flags can be:                               
         S: silent - no output                     
         V: verbose                                
```

- Here is an example of using it:

```
diff MKARCZCT EXEC     A MKVMARC EXEC D                                      
2,3c2,3                                                                      
< /* MKARCZCT EXEC - Create a VMARC file of zvm-community-tools execs  */    
< /* Usage: MKARCZCT                                                   */    
---                                                                          
> /* MKVMARC EXEC - Create a VMARC file of all zvm-tools               */    
> /* Usage: MKVMARC                                                    */    
5,5c5,5                                                                      
< /* Src: https://github.com/openmainframeproject/zvm-community-tools  */    
---                                                                          
> /* Source: https://github.com/mike99mac/zvm-tools                    */    
7,7c7,7                                                                      
< vmarcFile = "ZVMEXECS VMARC A"       /* output file */                     
---                                                                          
> vmarcFile = "ZVMTOOLS VMARC A"       /* output file */                     
```

<h3 id="grep-exec">GREP EXEC</h3>
The ``GREP EXEC`` searches for patterns in files.

- Here is the help:
```
grep -h                                                  
Name:  GREP EXEC - search files for text patterns         
Usage: GREP [lnx-flags] 'pattern' FN FT [FM] [(flags)]    
Where: pattern is a single quote delimited search string  
       FN FT is the file name and type to search          
       FM is the file mode (default A)                    
Where: zvm (FLAGS or Linux -flags can be one or more of:  
         d: show debug messages                           
         i: ignore case                                   
         n: show line numbers                             
         t: turn trace on                                 
         v: inverse - show non-matches                    
Note : lnx-flags must be preceded with '-'                
                                                          
Special characters:                                       
   .  - Matches one character                             
   .* - Matches one or more characters                    
   ^  - Matches start of line                             
   $  - Matches end of line                               
```

Examples follow using two small files:

```
type a a a                                                       
                                                                 
this is the file A A A with a trailing ERROR                     
Now ERROR is in the middle                                       
Another error in lower case                                      
ERROR in A A A at the start of a line                            
                                                                 
type a b a                                                       
                                                                 
this is the file A B A                                           
only one ERROR in this file                                      
```

- Search one file for the string ``ERROR``:
                                                                 
```
grep ERROR a a a                                                 
this is the file A A A with a trailing ERROR                     
Now ERROR is in the middle                                       
ERROR in A A A at the start of a line                            
```

- Search for text with spaces, escaping the pattern with single quotes: 
                                                                 
```
grep 'ERROR in' a * a                       
A A A1:Now ERROR is in the middle           
A A A1:ERROR in A A A at the start of a line
A B A1:only one ERROR in this file          
```

- Search multiple files:

```
grep ERROR a * a                                                 
A A A1:this is the file A A A with a trailing ERROR              
A A A1:Now ERROR is in the middle                                
A A A1:ERROR in A A A at the start of a line                     
A B A1:only one ERROR in this file                               
```

- Search for text using wildcard for single and multiple characters:

```
grep ERR.R a a a                                               
this is the file A A A with a trailing ERROR                   
Now ERROR is in the middle                                     
ERROR in A A A at the start of a line                          

grep E.*R a a a                                                
this is the file A A A with a trailing ERROR                   
Now ERROR is in the middle                                     
ERROR in A A A at the start of a line                          
```

- Search for text at the start and end of lines:

```
grep ^ERROR a * a                                      
A A A1:ERROR in A A A at the start of a line           

grep ERROR$ a * a                                      
A A A1:this is the file A A A with a trailing ERROR    
```

- Include line numbers in the output:

```
grep ERROR a * a (n                                              
A A A1:1:this is the file A A A with a trailing ERROR            
A A A1:2:Now ERROR is in the middle                              
A A A1:4:ERROR in A A A at the start of a line                   
A B A1:2:only one ERROR in this file                             
```

- Search ignoring case:

```
grep ERROR a * a (i                                              
A A A1:this is the file A A A with a trailing ERROR              
A A A1:Now ERROR is in the middle                                
A A A1:Another error in lower case                               
A A A1:ERROR in A A A at the start of a line                     
A B A1:only one ERROR in this file             
```

- Inverse output - show all lines that *do not* match:

```
grep ERROR a * a (v               
A A A1:Another error in lower case
A B A1:this is the file A B A     
```

<h3 id="head-exec">HEAD EXEC</h3>

The ``HEAD EXEC`` output the first part of files.

- Here is the help:
```
head -h                                                  
Name:  HEAD EXEC - output the first part of files
Usage: HEAD [-<n>] fn ft [fm]                      
Where: 'fn ft' is the file name and type         
     : 'fm' is the file mode (default A)         
     : -<n> is number of lines to show (default 10) 
```

### HISTORY EXEC
The ``HISTORY EXEC`` displays all commands previously issued, or applies a filter to them.

- Here is the help:
```
history -h                                    
Name:  HISTORY EXEC - Show the command history
Usage: HISTORY [filter]                       
Where: 'filter' is an optional search filter  
```

Hooks must be added to trap logon and logoff time.  Perform the following steps:
- Call the MYLOGON EXEC at logon time from your PROFILE EXEC.
```
tail -3 profile exec                                                
                                                                     
'SYN SYN'                            /* set synonyms */              
'EXEC MYLOGON'                       /* save logon time to history */
'SP CONS START TO' userid()          /* spool console */            
```
- The HISTORY command is added to SYN SYNONYM so just ``HIS`` or ``HIST`` will give you your history.                                                                                                                                          
```
tail -1 syn synonym                                
HISTORY  HISTORY 3                   
```
- Create a ``LOG EXEC`` that sends the retrieve buffers to the file ``COMMAND HISTORY A``. You must remember to type just ``LOG`` to logoff so it is called.  If you type ``#CP LOGOFF`` it will not be called and you lose the command history for that session.  Here is a sample:
```
/*-------------------------------------------------------------------*/   
/* LOG EXEC - save command history, add timestamp then logoff        */   
/*-------------------------------------------------------------------*/   
parse arg args                                                            
                                                                          
/* add list of commands for this session to command history */            
'PIPE CP QUERY RETRIEVE BUFFERS',    /* get command history */            
'| NLOCATE "Position Contents"',     /* remove header */                  
'| SPECS 10-*',                      /* remove position column */         
'| TRANSLATE',                       /* fold to upper case */             
'|>> COMMAND HISTORY A'              /* append to history file */         
                                                                          
/* add logoff timestamp, then log off  */                                 
dashes = "--------------------"                                           
line = "#" dashes "LOGOFF:" DATE('N') TIME('N') dashes                    
'EXECIO 1 DISKW COMMAND HISTORY A (FINIS STRING' line                     
'CP LOGOFF' args                     /* logoff with any args */           
```

Examples:

- Run ``HISTORY`` command
```
history                                                                        
                                                                               
# --------------------- LOGON: 5 May 2025 12:58:48 ---------------------        
HISTORY                                                                        
Q T                                                                            
IND                                                                            
LOG HO                                                                          
# --------------------- LOGOFF: 5 May 2025 12:59:12 ---------------------      
# --------------------- LOGON: 5 May 2025 12:59:19 ---------------------        
HISTORY                                                                        
```
                                                                               
- Run ``HISTORY`` searching for "LOG"                                        
```
history log                                                                    
# --------------------- LOGON: 5 May 2025 12:58:48 ---------------------        
LOG HO                                                                          
# --------------------- LOGOFF: 5 May 2025 12:59:12 ---------------------      
# --------------------- LOGON: 5 May 2025 12:59:19 ---------------------        
HISTORY LOG    
```

### MAN EXEC
The ``MAN EXEC`` calls help for the requested command.  

- Here is the help:
```
man -h                                                             
Name:  MAN EXEC - give help on command, details on QUERY and SET   
Usage: MAN command                                                 
     | MAN Query subcmd                                            
     | MAN SET   subcmd                                            
Where: command can be CMS, CP, XEDIT, TCPIP or REXX                
       subcmd  can be CMS, CP or XEDIT Query or SET subcommands    
```

For example, ``man q da`` takes you to the ``CP QUERY DASD`` help screen, and ``man substr`` takes you to the ``XEDIT SUBSTR`` help screen.

### MKZVMARC EXEC
The ``MKZVMARC EXEC`` creates the z/VM file ``ZVMTOOLS VMARC`` from all of these REXX EXECs.

Here is an example of using it:
```
mkvmarc                                                                         
Erasing old file: ZVMTOOLS VMARC A                                              
CALC     EXEC     A1. Bytes in=       735, bytes out=       640 (    87%).      
CALCDASD EXEC     A1. Bytes in=      4581, bytes out=      2560 (    55%).      
CALCOSA  EXEC     A1. Bytes in=     10372, bytes out=      4240 (    40%).      
CFM      EXEC     A1. Bytes in=      1254, bytes out=       880 (    70%).      
CFN      EXEC     A1. Bytes in=      1252, bytes out=       880 (    70%).      
CFT      EXEC     A1. Bytes in=      1298, bytes out=       960 (    73%).      
COPYDISK EXEC     A1. Bytes in=      1765, bytes out=      1200 (    67%).      
CPFORMAT EXEC     A1. Bytes in=      7773, bytes out=      3840 (    49%).      
DIFF     EXEC     A1. Bytes in=      6250, bytes out=      3040 (    48%).      
GREP     EXEC     A1. Bytes in=     12292, bytes out=      4880 (    39%).      
HEAD     EXEC     A1. Bytes in=      3996, bytes out=      2080 (    52%).      
HISTORY  EXEC     A1. Bytes in=      4273, bytes out=      2240 (    52%).      
MAN      EXEC     A1. Bytes in=      1812, bytes out=      1200 (    66%).      
MKVMARC  EXEC     A1. Bytes in=      1274, bytes out=      1040 (    81%).      
QA       EXEC     A1. Bytes in=       371, bytes out=       320 (    86%).      
RFN      EXEC     A1. Bytes in=      1088, bytes out=       800 (    73%).      
RFT      EXEC     A1. Bytes in=      1090, bytes out=       800 (    73%).      
RM       EXEC     A1. Bytes in=      1548, bytes out=      1120 (    72%).      
SPC      EXEC     A1. Bytes in=      1089, bytes out=       720 (    66%).      
SSICMD   EXEC     A1. Bytes in=      1291, bytes out=      1040 (    80%).      
TAIL     EXEC     A1. Bytes in=      1217, bytes out=       800 (    65%).      
WC       EXEC     A1. Bytes in=      4337, bytes out=      2240 (    51%).      
WCZVMTLS EXEC     A1. Bytes in=       428, bytes out=       400 (    93%).      
WHICH    EXEC     A1. Bytes in=     20735, bytes out=     10480 (    50%).      
WHO      EXEC     A1. Bytes in=      3301, bytes out=      1840 (    55%).      
Created file: ZVMTOOLS VMARC A 
```

### QA EXEC
The ``QA EXEC`` simply calls ``QUERY ACCESSED`` to save keystrokes. 

### RFN EXEC
The ``RFN EXEC`` renames a file only changing the file name. 

- Here is the help:
```
rfn -h                                                   
Name:  RFN EXEC - Rename file changing only file name    
Usage: RFN fn2 fn1 ft1 fm1                               
Where: 'fn2' is the new file name                        
       'fn1 ft1 fm1' is the source file                  
```

If you want to rename the file name of a file to ``RFNOLD`` in FILELIST, you would simply type ``RFN RFNOLD`` in front of the file.

### RFT EXEC
The ``RFT EXEC`` renames a file only changing the file type.

- Here is the help:
```
rft -h                                                 
Name:  RFT EXEC - Rename file changing only file type  
Usage: RFN ft2 fn1 ft1 fm1                             
Where: 'ft2' is the new file type                      
     : 'fn1 ft1 fm1' is the source file                
```

### RM EXEC
The ``RM EXEC`` allows wild cards when erasing files.

- Here is the help:
```
rm -h                                           
Name: RM EXEC - erase one or more files         
Usage: rm fn [ft [fm]]                          
Where: fn, ft or fm can be '*' for all files    
```

### SPC EXEC
The ``SPC EXEC`` closes your console and sends it to the reader with a unique timestamp. 

- Here is the help:

```
rm -h                                           
Name: RM EXEC - erase one or more files         
Usage: rm fn [ft [fm]]                          
Where: fn, ft or fm can be '*' for all files    
```

- Here is an example of using it, and receiving the file from the reader:

```
spc                                                                             
RDR FILE 0244 SENT FROM MIKEMAC  CON WAS 0244 RECS 0018 CPY  001 T NOHOLD NOKEEP
rec 244                                                                         
DMSRDC738I Record length is 132 bytes                                           
CON85431 20250208 A1 created                                                    
File CON85431 20250208 A1 received from MIKEMAC at SNAVM4 
```

### SSICMD EXEC
The ``SSICMD EXEC`` runs a CP command on all members of a z/VM SSI cluster. 

- Here is the help:
```
ssicmd -h                                                 
Name: SSICMD EXEC - Issue a CP command on all SSI members 
Usage: SSICMD <CPcmd>                                     
```

<h3 id="tail-exec">TAIL EXEC</h3>

The ``TAIL EXEC`` output the last part of files.

- Here is the help:
```
tail -h                                                  
Name:  TAIL EXEC - output the last part of files
Usage: TAIL [-<n>] fn ft [fm]                      
Where: 'fn ft' is the file name and type         
     : 'fm' is the file mode (default A)         
     : -<n> is number of lines to show (default 10) 
```

### WC EXEC
The ``WC EXEC`` counts lines, words and bytes in one or more files. 

- Here is the help:
```
ssicmd ?                                                      
Name: SSICMD EXEC - Issue a CP command on all SSI members     
Usage: SSICMD <CPcmd>                                         
```

### WHICH EXEC
The ``WHICH EXEC`` resolves and fully qualifies CMS, CP and XEDIT commands.

- Here is the help:
```
which -h                                                                  
Name:  WHICH EXEC - list type of command, details on QUERY and SET        
Usage: WHICH command [(FLAGS)]                                            
     | WHICH Query subcommand ['('FLAGS')']                               
     | WHICH SET   subcommand ['('FLAGS')']                               
Where: FLAGS can be:                                                      
             D: debug                                                     
             H: create help command                                       
             S: silent - negative verbosity                               
             T: trace                                                     
             V: verbose - return expanded command                         
```

Here are some examples of using it. The ``QUERY`` and ``SET`` commands allow for a second argument.  

```
which q disk            
QUERY DISK is a CMS command   

which q da              
QUERY DASD is a CP command    

which q scale           
QUERY SCALE is a XEDIT command
``` 

### WHO EXEC
The ``WHO EXEC`` takes the output of ``QUERY NAMES``, sorts it and shows it one virtual machine per line.  It also allows for a search pattern. 

- Here is an example of using it:

```
who SSL          
SSLDCSSM - DSC   
SSL00001 - DSC   
SSL00002 - DSC   
SSL00003 - DSC   
SSL00004 - DSC   
SSL00005 - DSC   
```

