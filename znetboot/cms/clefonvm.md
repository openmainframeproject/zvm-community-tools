# ClefOS-on-VM

## Installing ClefOS on z/VM

This document describes how to install ClefOS on z/VM using ZNETBOOT.
The target audience is those who are skilled at using and installing
Linux but not knowledgeable about z/VM or CMS. The purpose of this
document is to enable installation of ClefOS as quickly and painlessly
as possible by those who don't know CMS or z/VM.

While this document was written specifically for ClefOS,
it is applicable for NORD, SUSE, OpenSUSE, Debian, Fedora,
or any other Linux which can run on IBM Z architecture. In fact,
the ZNETBOOT utility could theoretically be used for installing
any operating system capable of running on IBM Z as long as
the OS kernel can be retrieved from the web.

## You Will Need

You will need a virtual machine. On z/VM, a virtual machine is also
referred to as a user, and a user is assigned to a specific virtual
machine. As a general purpose operating system, z/VM provides interactive
computing services by defining each user as a virtual machine, typically
running CMS. But being true virtual machines, "users" of z/VM can run
any operating system suitable for the IBM Z architecture.

On z/VM, users (virtual machines) are also commonly referred to
as "guests". The operating system you run in your virtual machine
is called a "guest operating system" and z/VM is the "host".

Your virtual machine should be defined for at least 1G of memory
(RAM, "storage") and have at least one disk of 5G or more (about 7000
"cylinders" of 3390 type disk). The example here has two disks, 1B0
and 1B1, both 10000 cylinders. The addresses and sizes of your disks
will vary, but are by convention a three or four hexadecimal digit
number (here, '180', as a leading zero is conventionally dropped).

Your virtual machine should also have a virtual NIC.
The z/VM sysadmin will determine whether your NIC is set for Layer 2
or Layer 3 (of the seven layer ISO networking stack) and you will
need to adjust the installation accordingly. The NIC will likely be
coupled to routed network to a virtual switch. (No changes needed
for virtual switch versus other connectivity modes.) In this example,
the virtual NIC is defined at 340. The address of your NIC will probably
be different.

If DHCP is available, it will provide IP address, routing,
and nameserver assignment. In that case, all one usually needs to know
is the network device name, and the system handles setting up network
connectivity. If DHCP is not present, one should gather the following
information:

1. Device name: (form: `enccw0.0.0340`):
1. IP v4:       (form: `192.168.0.100`):
1. Netmask:     (form: `255.255.255.0`):
1. IP gateway:  (form: `192.168.0.1`):
1. Nameserver:  (form: `8.8.8.8`):

Additionally, your virtual machine should have standard CMS requirements,
either an SFS space to serve as "filemode A" or (better) a 191 minidisk
to serve as your "A disk". You will of course need z/VM TCP/IP
connectivity. (When running CMS, you should be able to run standard
end-user internet tools and client utilities.)

CMS is a single-user operating system available on z/VM for
interactive work. When installing Linux, CMS acts as a self-sacrificing
[chained] loader: It provides the underpinnings to do the uploads
and run the ZNETBOOT utility. (see next) Once the kernel and other
requisite files have been fetched and arranged, control is handed off
to your virtual machine, which will perform the rough equivalent of a
`kexec()` function and then, CMS will step aside and vanish.
(thus: 'self-sacrificing')

## You Will Also Need

You will also need the ZNETBOOT tool, or at least two files from that
package. Specifically, you will need `ZNETBOOT EXEC` and `CURL REXX`.
(Filenames in CMS are two part, divided by blank space. Those files
would be `znetboot.exec` and `curl.rexx` on most other systems.
CMS is indifferent as to capitalization.)

Uploading via X3270 is explained. If you use some other means
than X3270 to connect with your z/VM host, your upload experience
will be different.

A third required file is `CLEFONVM ZNETBOOT` (aka `clefonvm.znetboot`),
which will hold bootstrap parameters unique to your virtual machine.
It must either be created with the CMS text editor `xedit` or must be
created on your desktop or laptop and then uploaded. There is an
example included with the ZNETBOOT package and on the web, but the
example will not work for your virtual machine because you will
minimally have different network addresses.

Note: if you're in the middle of installing Linux and get interrupted
you can safely `#cp logoff` from the virtual console (3270 session).

## Sign On

Using the local `x3270` command, connect to your z/VM host.
The z/VM logon screen will present three fields: `USERID`, `PASSWORD`,
and `COMMAND`. Ignore the last one, `COMMAND`. Type your virtual
machine name in the `USERID` field. Advance the cursor by pressing
\<Tab\>. Type your password in the `PASSWORD` field.
(The field has a display 'masking' for that class of a field,
so the plain text of the password will not be displayed.)

![logon.png](images/logon.png)

After you have typed your userid and password, press \<Enter\>.

Your virtual machine should boot CMS, quickly presenting a "Ready;"
prompt. (CMS does not take long to boot.)

![ready.png](images/ready.png)

Look at the lower right corner of your X3270 window for a status indicator.
If you see `VM READ`, then press \<Enter\> again (just one more time).
You should then see `RUNNING` in the status area.

## Upload ZNETBOOT

Retrieve the following files and upload them to z/VM.

* http://www.casita.net/pub/znetboot/znetboot.exec
* http://www.casita.net/pub/znetboot/curl.rexx
* http://www.casita.net/pub/znetboot/clefonvm.znetboot

You can use any web retrieval tool or method to make local copies
of these files. The 'wget' command line tool will do nicely.
In the latter case, it may make sense to make a local directory
to store such:

    $ mkdir s390x

and then move into it:

    $ cd s390x

Then retrieve each of the three files:

    $ wget http://www.casita.net/pub/znetboot/znetboot.exec
    $ wget http://www.casita.net/pub/znetboot/curl.rexx
    $ wget http://www.casita.net/pub/znetboot/clefonvm.znetboot

`clefonvm.znetboot` is a template file, and will need to be tailored
to the specifics assigned by your provider for your virtual machine.
Use your favorite plain text editor and amend the IP address, netmask,
network, and DNS server accordingly. Some of the statements,
for example ...

    IPADDR=192.168.0.100     <<< your IP address goes here
    NETMASK=255.255.255.0    <<< your IPv4 netmask goes here
    GATEWAY=192.168.0.1      <<< your IPv4 gateway goes here

... and so forth. Save your changes to that file, then upload all three
files to your virtual machine.

Note that the installer often requires more boot parameters
than can fit on a standard boot parm line, so you may need to
prefix statements with `ZNETBOOT_TOFILE=`. This will direct
ZNETBOOT to store those statements in an auxiliary CMS file.
(More on that some other time.)

These are all plain text files, not binary.

To upload, use the X3270 file transfer dialogue.
Hold down the left mouse button to bring up the "File" menu.
Slide down to "File Transfer ...".

Within the "File Transfer" dialogue, select "Send to host",
"Host is VM/CMS", and "Transfer as ASCII file". Then click
"Transfer File".

![filetrans.png](images/filetrans.png)

Files in CMS are identified with a filename, a blank,
and then a filetype. Therefore `znetboot.exec` must be named
`znetboot exec` on the "Host File Name" line. (This field is not
case sensitive, so feel free to enter it as lower case.)
Similarly for `curl.rexx` and `clefonvm.znetboot`

## Run ZNETBOOT

When you have finished uploading the files, enter the following command:

    znetboot clefonvm

ZNETBOOT will read your CLEFONVM ZNETBOOT file and begin trying to
download the kernel and initrd (and as optionally specified in the
kernel command line, a remote 'kickstart.cfg' file)

![znetboot.png](images/znetboot.png)

Depending on network connectivity between your z/VM host and the
repository, the CMS `pipe` commands may take a while to run. Give it time.

ZNETBOOT will cache and queue-up the Linux files in your virtual reader
and then once all are present, tell z/VM to boot from the reader
(similar to booting from a tape drive). You should see dozens,
even hundreds, of lines of Linux console output. z/VM will pause
the output one screen at a time. (Be patient. There is a way
to speed that up, but it is much easier just to let it ride.)

Once the installer has been brought up, you should see "Please ssh" ...

![anaconda.png](images/anaconda.png)

You should now do just that,
use SSH to connect and finish the installation.

## Install ClefOS

Congratulations!

At this point you are finished with the X3270 part of the task.
The rest should be very familiar.

You **may** disconnect from the virtual console. This is optional.
You can remain connected, but if you disconnect then z/VM will continue
to run your virtual machine without any chance of network interruptions
triggering unwanted console signals. Enter the command:

    #cp disconn

The hash/pound-sign is not a typo. The command is `#cp disconn` and
press \<Enter\>. (It's optional. You don't strictly have to disconnect.)

Whether you disconnect the virtual console or not,
use `ssh` to connect and drive the rest of the installation.
This part will be very familiar to experienced Linux users.

## Reboot

The ClefOS installer will automatically reboot after normal completion.
You do not need to be attached to your virtual console for this to happen.
As a bonus for remaining connected, if you did stay connected,
then you will again see many screens of Linux console boot message
output scroll by.

If your networking parameters are correct and the installation
worked correctly, you can now open a separate terminal, and use an
SSH client to connect your shiny new ClefOS mainframe virtual machine.
If not previously set during the installation, please immediately set
a `root` account password now.

## Hardening

Always set a unique and strong root password.

If an end user account is set up, a strong password there too.

Apply updates immediately:

    yum clean all
    yum -y updates

Add SElinux policy and netwrok descrption convenience packages:

    yum install policycoreutils net-tools

Trigger an SElinux relabel:

    touch /.autorelabel

The presence of this file will trigger SElinux relabel next boot.

## Reboot again

SElinux relabel will take effect.

Optionally set up "keyed SSH access":

    $ umask 077
    $ mkdir .ssh
    $ cd .ssh
    $ touch authorized_keys
    $ vi authorized_keys

Assuming the PUBLIC half of the key is on the clipboard,
the key sequence:

    A <paste> :w!:q!

and then see that it was cleanly saved:

    $ wc -l authorized_keys
    ## should return 1 line

    $ cat authorized_keys
    ## should contain that PUBLIC key

## done

Recovery is sometimes possible;
other times it seems more expedient to re-install to fix a typo.


