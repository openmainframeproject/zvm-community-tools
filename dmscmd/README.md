# DMSCMD
DMSCMD provides CMS "command editing": re-executing a previous command by typing = and hitting enter; or ? to retrieve it, /x/y to change x to y and re-execute, + to add a token, - to remove a token, & to "hold" it: execute it (without the ampersand) and redisplay it on the command line. These can also be combined, e.g.:
```
copyfile x x a y y a (append
```
change "x x" to "x y", remove 'append', and replace it with 'replace', then add 'type':
```
/x/y/-type
```
If the string to be changed by a / includes a /, a period followed by a delimiter character can be specified, e.g.:
```
.,/,!,
```
to change a slash to an exclamation point. The delimiter must not be a valid character in a CMS fileid.

Whenever DMSCMD re-executes a command, it types it on the screen:
```
type a a a
this is file a
Ready(phsiii@VSIVC1); T=0.01/0.01 15:12:19
-b
==> type a a b
DMSOPN069E Filemode B not accessed
```
Note the "==>" showing what command was re-executed. This is actually just showing that the command came from the stack, which can be useful if something leaves junk in the stack:
```
somecmd   <==this is a poorly behaved command that leaves two lines stacked
R;
==> somejunkline
Unknown CP/CMS command
==> someotherjunkline
Unknown CP/CMS command
```
## Building DMSCMD
To build ``DMSCMD``, perform the following steps:
- Download it and copy it to your A disk as text (ASCII).
- Rename it to EXEC: 
```
==> rename dmscmd mailable a = exec =
```
- Do this (perhaps split these out to describe each step?):
```
* Apply updates and assemble the module: should produce no errors
vmfhlasm dmscmd dmsvm
* Load it into the transient area
load dmscmd (origin trans
* Genmod it with SYSTEM because it mucks with ADMSCRD in NUCON
genmod dmscmd (system
```

## Using DMSCMD
To use ``DMSCMD``, perform the following steps:

```
==> dmscmd <history <n>>
```

There is no limit on "n" because memory will limit it long before anything else. Default is 25.

## Using the "n" saved commands
The nucleus extension USERWORD points to the DSECT named ``HISTORY`` at the bottom of DMSCMD. This is a pretty simple DSECT, comprising a few fullwords and then a list of the commands. 

The only tricky part is that this is a "ring": the first command goes in the first slot, the second after that, etc. There's a "cursor" that points to the NEXT empty slot. So once all the buffers are filled, the cursor points to the first command in the ring. Before that, the cursor will point to a bunch of nulls. So when traversing the list, fetch the fullword at the cursor; if it's nulls, start at the "top", at the first buffer.

The QHISTORY EXEC in the package just extracts and displays the commands. The idea is that someone will create HISTORY EXEC that extracts them, puts them into an XEDIT-driven dialog, and lets you edit and re-execute the command of your choice.
