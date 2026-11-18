# CP Commands

This document discusses
z/VM "Control Program" commands for use with Linux.

Linux on z/VM can issue "CP commands" by way of the `vmcp` utility.
The number and nature of all CP commands is far beyond scope
of this document, so only the most relevant for Linux are listed.

Some CP commands are distruptive, rebooting your virtual machine
or placing it into a state needing manual attention. Some CP commands
are harmless. Query commands are generally all safe.

CP commands can be abbreviated.
The hypervisor will recognize the shortest unique value
of any command and its arguments.

## `vmcp` versus `#cp`

From a privileged shell, you can issue CP commands using the `vmcp`
command. From the virtual console of a 3270 session, you can issue
CP commands using the `#cp` prefix. (3270 console input is otherwise
delivered to Linux for processing.) In this document, CP commands are
presented both ways.

Keep in mind that the shell treats any word starting with "`#`"
as a comment. If you enter the "`#cp`" form of these commands
from a shell, nothing will happen. (Also see advanced tricks below.)

Some common CP commands of use with Linux follow. 

## query virtual storage

Use the `q v stor` command to show the memory presently defined for
your virtual machine. The size can be changed. (see next)

    vmcp q v stor
    #cp q v stor

## define storage

Use the `define storage` command to change the size of
your virtual machines memory (internal storage, RAM).

    vmcp def stor 1G
    #cp def stor 1G

This command may reset your virtual machine so should be issued
when you have access to the virtual console or should be stacked with
an IPL command.

## query virtual all

Use the `q v all` command to show all devices associated with
your virtual machine. The devices themselves may be virtual or real.

    vmcp q v all
    #cp q v all

The output of `q v all` shows all virtual devices of your virtual machine.
Some of those devices will be bootable, including bootable disks
but also tape drives or your virtual card reader.

## query userid

In case you lose track of which virtual machine you're on, use the
`q userid` command to interrogate CP for your virtual machine name.

    vmcp q userid
    #cp q userid

## query terminal

Use the `q term` command to show z/VM session terminal settiings,
including 3270-specific settings.

    vmcp q term
    #cp q term

`vmcp q term` is not very informative when you are connected
to Linux using SSH because the z/VM terminal session settings
have no effect on your SSH session or pseudo-terminal TTY.

See below for discussion of the `terminal` command 
(not prefixed with `query`).

## query names

z/VM is a community system. Find out the names of other virtual
machines on the same z/VM host with the `q names` command.

    vmcp q names
    #cp q names

## message

Use the `message` command to send an interactive message to another
virtual machine. `message` can be abbreviated `msg` or just `m`.

    vmcp msg otherguy want to go get lunch?
    #cp msg otherguy want to go get lunch?

If the receiving virtual machine is connected, your message might be
presented on its virtual console (in the output area). If the target
virtual machine is not connected and it has no listener then you'll get

    HCPMFS057I OTHERGUY not receiving; disconnected

Sending interactive messages to other virtual machines is unique to z/VM
and not found with other hypervisors. The feature is inherently related
to the z/VM idea of a user being a virtual machine and a virtual machine
being a user.

## ipl

Use the `ipl` command (Initial Program Load) to boot your virtual machine. 

    vmcp ipl 1b0 clear
    #cp ipl 1b0 clear

This command WILL reset your virtual machine so should be issued
when you have access to the virtual console if there is any likelihood
that it will fail to work as expected. 

In this example `1B0` is the address of a bootable disk
and `clear` means to also reset memory before performing the load.

`clear` is optional. The kernel will likely clear memory on its own.
Many use `clear` when booting from a device as a matter of hygiene.

On z/VM one can boot from a "named saved system" (NSS).
This is akin to the direct kernel load function of other hypervisors.
An example is:

    vmcp ipl linux
    #cp ipl linux

In this example, if there is no NSS named LINUX, then the command
results in an error and your virtual machine continues to run whatever
kernel it was running when the command was issued.

You cannot add the `clear` option when booting a named system.

You can invoke a CMS environment by IPLing CMS.

    vmcp ipl cms
    #cp ipl cms

CMS is an efficient environment standard with z/VM which is actually
an operating system in its own right. CMS cannot be used simultaneously
with Linux. Recommend you only do this when you have access to the
virtual console because CMS is only useable from there.
This command WILL reset your virtual machine.

## disconnect

Use the `disconnect` command to release your virtual console
without logging off (and destroying your virtual machine).
This is essential at some point if you have been working from
a 3270 session because the session will eventually break due to
network interruptions or other disruptions, but you'll no doubt
want your Linux virtual machine to continue running.

    vmcp disc
    #cp disc

You can reconnect by logging back onto z/VM.
When you logon to z/VM, your virtual machine is instantiated.
If it was already instantiated, you are reconnected to its virtual console.

## logoff

Use the `logoff` command to de-instantiate your virtual machine.
It is equivalent to a `virsh destroy` except that you're destroying
your own virtual machine. (there is no "target domain" argument)

Note: if you're in the middle of installing Linux and get interrupted
you can safely `#cp logoff` from the virtual console (3270 session).

Your virtual machine ceases to exist, though its disks and configuration
remain intact. ("destroy" is such a harsh word)

    vmcp logoff
    #cp logoff

"Immediately terminate the [virtual machine].
This doesn't give the [guest] OS any chance to react, and it's
the equivalent of ripping the power cord out on a physical machine."

The `logoff` command will usually also terminate your 3270 session.

Recommend you NOT use `logoff` without first shutting down Linux.
(Which means that the `vmcp logoff` variant is of questionable value.)
It has the same effect as pulling the plug on a physical computer.
Filesystems will be left in an unknown state.

## indicate

Use the `indicate` command to indicate system or virtual machine status.

    vmcp ind
    #cp ind

`indicate` without arguments displays very simplistic z/VM status,
such as (physical) processor utilization, host system paging, etc.

    vmcp ind user
    #cp ind user

`indicate user` displays the status of your virtual machine
(the status of the "user" from z/VM's perspective),
such as (virtual) processor consumption, working set size, etc.

## terminal

Use the `term` command to modify z/VM virtual console settings.

The complete list of z/VM terminal settings is beyond the scope
of this document.

You can change the output hold and scroll settings,
the "`more`" values, with the command

    vmcp term more 10 10
    #cp term more 10 10

This affects how long z/VM will pause output before it clears the screen 
and displays further output. The first "10" is the number of seconds
to wait before audible alert (beep). The second "1" is the number of
additinal seconds to wait before z/VM will proceed.

If you anticipate a lot of output, like when booting Linux,
you might enter the command

    vmcp term more 1 1
    #cp term more 1 1

If you really don't want to wait AT ALL for output to be held

    vmcp term 0 0
    #cp term 0 0

By default, z/VM uses very different reserved characters
for terminal entry. "#" as seeen in `#cp` is actually line end.
Escape is double quote ("). These can be changed



