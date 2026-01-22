## Prerequisite:
You need to install these PTFs:
- http://www-01.ibm.com/support/docview.wss?uid=isg1VM65202
- http://www-01.ibm.com/support/docview.wss?uid=isg1VM65257

The rexx are implemented to work with the new directory statements appeared
with the z/VM620 but they are not tested on this version.

The package "should" be unpacked and used on your new VM.

You must use VALID user withpass files.

IBM adds commentaries on the top of the user withpass files. DRCT-01 and
DRCT-02 remove them.

OLD and NEW parameters refer to the filenames of the user withpass files.
For example, if you migrate from a z/VM530 to a z/VM540, you can code
OLD="ZVM530" and NEW="ZVM540". ZVM530 WITHPASS A0 and ZVM540 WITHPASS A0 will
be used. Edit each file of the package to apply your own values.

Default member names for DIRECTORY and GLOBALDEFS are DIRECT and GLOBAL. You
have to check first you do not have any directory named with these defaults. If
you meet that case, you have to modify DRCT-01, DRCT-02 and DRCT-03. Do a
ALL/*COPY / xedit command and apply the name of your choice.

## DRCT-01 EXEC
The EXEC creates the "old" MACLIB. You can discard members you know you will
never need in your new VM. Retain the members you have discarded if you need to
regenerate this maclib later, for the day of your migration for example. It is
easy to create a small rexx with this kind of order:
"MAClib DELete libname membernames"

## DRCT-02 EXEC
The EXEC creates the "new" MACLIB.

## DRCT-03 EXEC
DRCT-03 creates the DRCT-04 EXEC A.
DRCT-03 creates the UNIQUE MACLIB where all unique directories from "old" and
"new" maclibs are merged. This maclib is only used to check and confirm a
normal situation. For example, if you have a user $ALLOC$ in z/VM530 and a user
$ALOC$ in z/VM540, they are unique but have the same function. You could want
to take some actions in such a case.

## DRCT-04 EXEC, DRCT-01 XEDIT and DRCT-02 XEDIT
Don't run this exec "as is" the first time, go in... You could prefer to cut it
into several pieces.
DRCT-04 EXEC treats the duplicates. You enter in xedit mode where you can see
the two same member names from the two maclibs. The "old" and the "new" members
appear one above the other. DRCT-01 XEDIT is a default profile. Copy/paste your
modifications manually. If you "quit" or "file", you come back to a file (which
one ?) in screen set to 1. You will rapidely remark it is confusing... PF03
avoids this: it activates the DRCT-02 xedit macro that does small controls for
you too. The macro doesn't allow you to alter the old member (you are not
supposed to). With no excessive development, it permits to control if the ALT
xedit value was changed or not. If you did, you probably thought you were
modifying the good file... To "file" your changes you have to move the cursor
in the old member and press PF03.

## DRCT-05 EXEC
DRCT-05 only builds the "new" USER INPUT file with your system defaults. So,
you can test your changes in your new environment. Tests after tests you will
no more bring changes into it. It is time to backup the "new" maclib.
The maclib now is THE maclib you will use each time you will need to merge it
with the "old" maclib, and later, THE maclib you will use the day of the
migration.

## DRCT-06 EXEC
DRCT-06 merges the "old" and the "new" MACLIBs to build a USER INPUT file.
For duplicate directories, the "new" one are selected. All the unique
directories are selected.

## DRCT-07 EXEC
Dirmaint is required. Do not run this exec before you understand what it does:
   - The exec sends a USER BACKUP file to your reader that can be reused if you
     meet problems.
   - DRCT-07 ACTIVATES the USER INPUT file.

## DRCT-08 EXEC
The exec compacts the "new" maclib.
