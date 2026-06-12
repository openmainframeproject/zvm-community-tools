# ZNETBOOT Design

ZNETBOOT is a CMS application.
There is no specific equivalent for other environments.

There *may* be a ZNETBOOT work-alike for Linux-on-z/VM ... someday.

## CMS Pipelines

ZNETBOOT uses CMS Pipelines to streamline all of its operation.

## cURL

ZNETBOOT uses a `curl` stage to handle the network side of its work.
The reason for using `curl` is that the pipelines for fetching
and punching can be similar to counterpart pipelines on other platforms.

The `curl` stage used is taken from CMS Make
and in turn depends on CMS Pipelines for the majority of its operation.
As of this writing, TLS/SSL support (for HTTPS URLs) is not available
owing to the lack of SSL/TLS support in CMS Pipelines. As soon as
CMS Pipelines can do TLS/SSL, this `curl` will follow shortly.

## FILELIST

CMS components are listed in ZNETBOOT FILELIST.
As a project, ZNETBOOT uses stock CMS methods whenever possible
so ZNETBOOT FILELIST is a plain text file containing the standard
filename, filetype, and filemode of each component file.
ZNETBOOT FILELIST can be used directly by the `filelist` utility in CMS.

## VMARC

ZNETBOOT is packaged for CMS in two forms: a VMARC file and a TAR file.
VMARC is a common utility in the z/VM world. ZNETBOOT VMARC can be
uploaded to any VM/CMS system and "exploded" by the VMARC utility.

To create the VMARC package, ZNETBOOT FILELIST is fed to `vmarc`
in such a way that all files listed go directly into the archive.

## TAR

ZNETBOOT is packaged for CMS in two forms: a VMARC file and a TAR file.
TAR is widely used on many platforms. CMS TAR creates a POSIX-compatible
archive which can be used (essentially) anywhere. Web sites where
ZNETBOOT is available typically have both `znetboot.tar` and
`znetboot.tar.gz`.

To create the TAR package, ZNETBOOT FILELIST is fed to `tar`
in such a way that all files listed go directly into the archive.

## additional files

There are other files which are part of the ZNETBOOT project
but which are not part of the ZNETBOOT package. This file is one.

More files from the project may be added to the package,
but uniqueness in CMS name space is important. Files from the project
shall be added to the package by inclusion in ZNETBOOT FILELIST
and must therefore have a filename/filetype which is unique and
meaningful in CMS. (Because ZNETBOOT is a CMS utility.)


