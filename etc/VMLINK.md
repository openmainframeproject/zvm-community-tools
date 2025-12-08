# VMLINK

VMLINK Automounter for Linux on z/VM

VMLINK extends the namespace of a virtual machine to include 
devices of (specifically disks owned by) other virtual machines.

## VMLINK Automounter

Consider automounter point `/vmlink`, similar to `/misc` and `/net`.
Under `/vmlink`, one can have target directories ("keys" in automounter
speak) named *vmid.addr* where "vmid" is the owning virtual machine
and "addr" is the address of a disk on that virtual machine.

## cd /vmlink/yourvm.yourdisk

The VMLINK automounter script uses the key, here `yourvm.yourdisk`,
to "link" (at the z/VM layer) your disk, bring it online,
and then mount it at the named location under the automounter point.

## VMLINK Concept

VMLINK automates referencing disks of other virtual machines on demand.
The "client" or guest (virtual machine) initiates the connection.
Host administrative action is required for authorizing such references.
Host administration is *not* required for activating such references once authorized.

In other words, your virtual machine must be granted the right
to use another disk, but once authorized you do not have to engage
the administrator to use a disk for which you are authorized.
(The VM admin does not have to perform the "attach", which we call "link".)

## VMLINK Project

Rushal Verma developed the VMLINK automounter script
as an intern project under the Linux Foundation.

On CMS, `vmlink` is a command. <br/>
On Linux, `/vmlink` is an automounter point.


