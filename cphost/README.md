# CPHOST

CPHOST adds a command to second-level z/VM systems
enabling them to issue CP commands to the first-level z/VM host system.

This repository is a collection of files from two packages from the
VM Downloads page. The `cp1stl` and `cphost` sub-directories contain
the textual portions of those packages.

Note: these sources are all
Copyright International Business Machines Corporation
and are provided here with permission from the original authors.

## z/VM Downloads

The authoritative source for many z/VM packages is hosted by
the IBM z/VM lab.

https://www.vm.ibm.com/download/

The two packages on which this collection is based are `CPHOST` and
`CP1STLVL`. VMARC files of these are in the `arc` sub-directory here.
Their source and textual content are in the `cphost` and `cp1st`
directories. These are for reference and attribution.

https://www.vm.ibm.com/download/packages/cphost.vmarc

https://www.vm.ibm.com/download/packages/cp1stlvl.vmarc

There is also a shrinking collection of z/VM developer pages.

https://www.vm.ibm.com/devpages/

## Building with `make`

This collection is designed to build the `cphost` command
using `make`. It builds cleanly using `make` under the OpenVM shell.
There is CPHBUILD EXEC included for "just do it" from plain CMS.

Apologies to the original authors: I'm a fan of `make`.

## Credits

IBM staffers who contributed to the work:

* Kris Buelens
* Shimon Lebowitz
* Tim Greer

A similar tool for use on z/OS (MVS) was provided by Jim Elliott


