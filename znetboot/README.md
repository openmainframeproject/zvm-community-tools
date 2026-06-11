# znetboot

ZNETBOOT makes it easy to bring up Linux on z/VM. <br/>
Just enter the command `znetboot` from the CMS "Ready;" prompt.

ZNETBOOT is intended to reduce the number of manual steps required
to boot Linux on a VM/CMS system. It should make things much easier
for non-VM and non-mainframe users. After nearly two decades of Linux
on z/VM, mainframe Linux should be at least this easy.

## Official Repository

What you find here under the z/VM Community Tools repository
is a copy of the official distribution.

https://github.com/trothr/znetboot/

## Runs on CMS

This release of ZNETBOOT only runs on CMS. <br/>
If successful, it immediately re-IPLs (reboots) your virtual machine
to the installer described in the installation file.

The filetype of the installation file is always `ZNETBOOT`.

## Running ZNETBOOT

The syntax of the `znetboot` command is ...

    znetboot instfile

 ... where `instfile ZNETBOOT` must exist on an access CMS minidisk
or SFS directory. If you do not specify a filename, the username
of your virtual machine is taken as the default filename.

ZNETBOOT reads the installation file and retrieves the kernel and initrd
indicated in that file. Other statements in the installation file are
passed to the kernel as boot parameters. For example ...

    # the following are used by ZNETBOOT EXEC
    ZNETBOOT_KERNEL=http://znetboot.casita.net/nord/image
    ZNETBOOT_INITRD=http://znetboot.casita.net/nord/ramdisk.gz

    # the following are used by the bootstrap and vary from Linux to Linux
    HOSTNAME=mynord.mydomain.com
    IPADDR=192.168.0.64
    GATEWAY=192.168.0.1

Then enter `znetboot` from the CMS "Ready;" prompt. <br/>
Next stop, Linux.

## Working ZNETBOOT Distributions

Installers for the following Linux distributions
are known to work with ZNETBOOT:

* ClefOS
* Alpine
* Debian
* Fedora
* Ubuntu
* NORD  


