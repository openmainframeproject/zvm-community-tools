# ZNETBOOT

ZNETBOOT makes it easy to bring up Linux on z/VM.
Just enter the command 'znetboot' from the CMS `Ready;` prompt.

ZNETBOOT exists purely to simplify installing Linux on z/VM.
The typical recipe involves retrieving a kernel and installation image,
stacking them along with a boot parameters file into your virtual reader.
Often a supplemental configuration file is needed. ZNETBOOT automates
the retrieving and arranging of all these files.

## ZNETBOOT EXEC

`ZNETBOOT EXEC` is the command.
It uses `CURL REXX` to fetch files from the network.
These two things comprise the essence of ZNETBOOT.

## ZNETBOOT Config File

ZNETBOOT uses a configuration file to know what to do.
This file is nothing but a Linux boot parameters file,
with the addition of URLs for the kernel and initial ramdisk image.

You can create this file on your desktop or laptop and then
upload it to VM/CMS or you can use `XEDIT` and create it right there
in your virtual machine.

The filetype, in CMS terms, must be "ZNETBOOT".
On other platforms, the right part of the name of the file
must be ".znetboot".

The filename (left part) can be anything you like.
By default, if you do not indicate a filename on the `znetboot` command,
ZNETBOOT will look for a file with a filename matching your VMID.
If your virtual machine is "BOB" and you don't tell ZNETBOOT what file
to use, it will look for `BOB ZNETBOOT`. Otherwise, the name is arbitrary.

## ZNETBOOT as a VM/CMS Package

`ZNETBOOT EXEC` and `CURL REXX` are available individually
or contained in `ZNETBOOT VMARC` or `ZNETBOOT TAR`.

z/VM admins would do well to install ZNETBOOT on a common disk
on their systems so any CMS user will have ready access.

The CMS package is defined by ...

http://www.casita.net/pub/znetboot/znetboot.filelist

and is available as ...

http://www.casita.net/pub/znetboot/znetboot.vmarc

or

http://www.casita.net/pub/znetboot/znetboot.tar.gz

There is also a help file. Enter 'help cms znetboot'
after the VMARC (or TAR) bundle has been exploded.

## ZNETBOOT as a GitHub Project

In addition to all the files found in the CMS package,
the GitHub project hosts markdown files ...

    README.md
    CMS_Commands.md
    Community.md
    CP_Commands.md
    Glossary.md
    X3270.md

The only reason these files are not included in the CMS package
is to avoid limitations in traditional CMS filesystems. Everything
essential to the package is included in the VMARC and TAR files.

The GitHub project is found at ...

https://github.com/trothr/znetboot/

##

See also: `ZNETBOOT LICENSE` (`znetboot.license`)
for intellectual property rights (IPR) and related information.
Capitalization and other indicia may be obscured due to
technical limitations of the supporting systems used.

If you have questions about this package, send e-mail to:

    Rick Troth <rmt@casita.net>

Copyright © 2018, Richard M. Troth, all rights reserved.                                                                                                                                                                                                       
