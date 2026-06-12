# znetboot

ZNETBOOT makes it easy to bring up Linux on z/VM.
Just enter the command `znetboot` from the CMS "Ready;" prompt.

ZNETBOOT is intended to reduce the number of manual steps required
to boot Linux on a VM/CMS system. It should make things much easier
for non-VM and non-mainframe users. After nearly two decades of Linux
on z/VM, mainframe Linux should be at least this easy.

## running znetboot

ZNETBOOT reads an installation file and retrieves the kernel
and initrd indicated. Other statements in the installation file
are passed to the kernel as boot parameters. For example ...

    # the following are used by ZNETBOOT EXEC
    ZNETBOOT_KERNEL=http://znetboot.casita.net/nord/image
    ZNETBOOT_INITRD=http://znetboot.casita.net/nord/ramdisk.gz

    # the following are used by the bootstrap and vary from Linux to Linux
    HOSTNAME=mynord.mydomain.com
    IPADDR=192.168.0.64
    GATEWAY=192.168.0.1

Then enter `znetboot` from the CMS "Ready;" prompt. Next stop, Linux.

## working znetboot distributions

Installers for the following Linux distributions are known to work with ZNETBOOT:

* ClefOS
* Alpine
* Debian
* Fedora
* Ubuntu
* NORD  

Support for the following Linux distributions are wanted:

* SUSE (and/or OpenSUSE)
* CentOS
* Slack/390
* Gentoo
* Red Hat


