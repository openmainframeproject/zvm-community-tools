# CMS Commands

This document discusses CMS commands available on z/VM.

CMS is the "Conversational Monitor System",
a single user operating system exclusive to the z/VM environment.
(CMS cannot run without "CP", the z/VM hypervisor.)

CMS provides a very efficient interactive environment.
For ZNETBOOT, CMS provides the essential functions needed
to retrieve Linux kernels and supporting files from the network,
arrange them in proper order, and then direct CP to boot Linux.

You cannot issue CMS commands when running Linux.
You cannot have Linux running when CMS is booted.
They are distinct operating systems.

Whether running CMS or Linux, you still have CP, the Control Program.
CP commands on z/VM are common between CMS and Linux. To further
confuse matters, CMS passes commands it does not recognize to CP
with the result that many users do not know if a z/VM command is a
CP command (also available to Linux) or a CMS command (not available
in Linux).

Some common CMS commands follow.

## znetboot

`znetboot` is the central command of this project.
It attempts to download and boot Linux (or any operating system)
using a kernel and related files retrieved from the network.

`znetboot` takes an optional argument, the name of a configuration file.
If you wanted to boot Linux according to the "`clefonvm`" configuration
then you would enter

    znetboot clefonvm

`znetboot` is NOT a standard CMS utility.

## filelist

`filelist` is a standard CMS utility presenting a list of your files.

`filelist` is a full-screen utility, commandeering your 3270 session
and obviating the usual z/VM screen layout.

`filelist` can be abbreviated `fl`.

Within most CMS full-screen utilities, \<PF3\> exits to the command line.

## listfile

`listfile` is a standard CMS utility for listing files interactively.
It is the operational equivalent of the `ls` command in Unix nd Linux.

Files in CMS are multi-token. There is a filename and a filetype.
There is also a filemode which combines a drive letter or directory
letter with a numeric modifier. The letter is strictly related to where
the disk or directory is accessed, sort of like where a filesystem is
mounted in Linux and Unix. The number can affect the behavior of the
system when handling the file. Discussion of filemode numbers is beyond
the scope of this document.

`listfile` can be abbreviated `list`.

An example use of `listfile` is the listing of your ZNETBOOT files.

    list * znetboot

or

    list * znetboot a

Either form lists all files on your "A disk" with a filetype of ZNETBOOT.

## rdrlist

`rdrlist` is a standard CMS utility presenting your "reader list".

The display of `rdrlist` is similar to that of `filelist`,
but the files it displays exist in spool space, not on disk.
z/VM spool space is vital to the operation of `znetboot`
and you may have "spool files" of interest which can be managed
from the `rdrlist` utility.

`rdrlist` can be abbreviated `rl`.

Within most CMS full-screen utilities, \<PF3\> exits to the command line.

## help

`help` provides helpful information as the verb implies.

CMS `help` is extensive, if daunting.
It is conceptually just like the Unix `man` command
but is a full-screen utility like `filelist` and `rdrlist`.

Within most CMS full-screen utilities, \<PF3\> exits to the command line.



