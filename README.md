![zz/VM Community Tools/VM Community Tools Logo](https://raw.githubusercontent.com/openmainframeproject/artwork/5b27f85f886da75ddf53511eb5289c53c972415c/projects/zvm-community-tools/horizontal/color/zvm-community-tools-horizontal-color.svg)

# z/VM Community Tools

This is the z/VM Community Tools github repository.  Its goal is to list all the Free and Open Source Software for IBM's z/VM operating system.
If you'd like to help, email Mike Mac at mike99mac@gmail.com.

## Install

Each subdirectory has its own install process:  
- ``execs/`` - Download the ``https://github.com/openmainframeproject/zvm-community-tools/blob/main/execs/zvmtools.vmarc`` file and copy it to z/VM in binary, and unpack it.
- ``dmscmd/`` - Follow the instructions here: https://github.com/openmainframeproject/zvm-community-tools/tree/main/dmscmd#building-dmscmd 
- ``zlma`` - Use the ``instzlma`` bash script 
- ``ztrust/`` - Follow the instructions here: https://github.com/openmainframeproject/zvm-community-tools/tree/main/ztrust

## Build

Each subdirectory has its own build process, if any:  
- ``execs`` - Because REXX EXECs are interpreted, there is no build process necessary.  There is a VMARC file that can be copied and expanded to put all EXECs onto one minidisk.

- ``zlma`` - There is an install script ``instzlma`` that is described in detail.

## Discussion

You can connect with the community in a variety of ways...

- [IBMVM Mailing list](http://listserv.uark.edu/cgi-bin/wa?A0=IBMVM)
- [z/VM Community Tools channel on Open Mainframe Project Slack](https://openmainframeproject.slack.com/archives/C035HAMNUU9)
- [z/VM Community Tools category on Open Mainframe Project Community Forums](https://community.openmainframeproject.org/)

## Contributing
Anyone can contribute to the z/VM Community Tools project - learn more at [CONTRIBUTING.md](CONTRIBUTING.md)

## Governance
z/VM Community Tools is a project hosted by the [Open Mainframe Project](https://openmainframeproject.org). This project has established it's own processes for managing day-to-day processes in the project at [GOVERNANCE.md](GOVERNANCE.md).


## Reporting Issues
To report a problem, you can open an [issue](https://github.com/openmainframeproject/z/VM Community Tools/issues) in repository against a specific workflow. If the issue is sensitive in nature or a security related issue, please do not report in the issue tracker but instead email z/VM Community Tools-private@lists.openmainframeproject.org.

# Other Sources of Community Tools

This section consolidates information scattered across IBM download libraries, GitHub repositories, VM Workshop presentations, independent developer projects, and historical VM community archives.

**Important:** Not every freely downloadable utility is open source. Each entry should be classified according to its actual source availability and license.

## Table of Contents

- [1. Open Mainframe Project](#1-open-mainframe-project)
- [2. IBM z/VM Download Library](#2-ibm-zvm-download-library)
- [3. Independent GitHub Projects](#3-independent-github-projects)
- [4. Linux-on-Z Tools](#4-linux-on-z-tools)
- [5. VM Workshop](#5-vm-workshop)
- [6. Other Information Sources](#6-other-information-sources)
- [7. Historical VM Community Resources](#7-historical-vm-community-resources)

---

## 1. Open Mainframe Project

### z/VM Community Tools

- **Repository:** https://github.com/openmainframeproject/zvm-community-tools
- **Website:** https://www.zvmcommunitytools.org/

This describes the content on this Github repo:

| Component | Description |
|---|---|
| EXECs | CMS REXX EXEC utilities, including WHICH and MAN |
| DMSCMD | Additional commands and history functionality for Directory Maintenance |
| ZLMA | z/VM and Linux Modern Administration |
| ZTRUST | PGP keys and trust-related facilities |
| ZNETBOOT | Network boot facilities |
| CPHOST | CP host-related utilities |
| TSC | Additional community tooling |
| Scripts | Supporting automation and scripts |
| AUTO.VMLINK | VMLINK-related automation |

See the repository README for current components, installation procedures, and documentation.

### Open Mainframe Project Landscape

- **Repository:** https://github.com/openmainframeproject/omp-landscape
- **Landscape source:** https://github.com/openmainframeproject/omp-landscape/blob/main/landscape.yml

The Open Mainframe Project Landscape provides a structured inventory of projects in the mainframe ecosystem, including Linux on IBM Z and z/VM-related projects.

It is a useful discovery mechanism for identifying projects that may not be listed in the z/VM Community Tools repository.

---

## 2. IBM z/VM Download Library

- **Main download page:** https://www.ibm.com/support/pages/zvm/download/
- **Package index:** https://www.ibm.com/support/pages/zvm/download/packages/
- **Developer pages:** https://www.ibm.com/support/pages/zvm/devpages/
- **Technical information:** https://www.ibm.com/support/pages/zvm/techinfo/

The IBM download library is the traditional central location for z/VM contributed software.

It includes utilities developed by IBM employees, customers, independent developers, and other members of the VM community.

**Licensing note:** The IBM download library is a distribution repository, not a guarantee that every package is open source. Check the licensing terms and source availability of individual packages.

---

## 3. Independent GitHub Projects

Many useful z/VM tools are maintained independently of the Open Mainframe Project and IBM download library.

### Feilong

- **Repository:** https://github.com/openmainframeproject/feilong
- **Documentation:** https://cloudlib4zvm.readthedocs.io/
- **License:** Apache 2.0

An open-source REST API and SDK for provisioning and managing z/VM guests, images, networks, and volumes.

Feilong integrates with cloud management platforms and infrastructure automation tools.

### IBM zvm_ansible

- **Repository:** https://github.com/IBM/zvm_ansible
- **Collection:** https://github.com/IBM/zvm_ansible_collection

Ansible automation for z/VM using SMAPI and the Feilong ecosystem.

Provides automation for operations such as:

- Creating and managing virtual machines.
- Cloning virtual machines.
- Starting and stopping guests.
- Managing minidisks.
- Configuring networking.
- Automating guest provisioning.

### Terraform Provider for z/VM

- **Repository:** https://github.com/mfcloud/terraform-provider-zvmsdk

Terraform integration with the z/VM SDK/Feilong ecosystem.

Provides an infrastructure-as-code approach to managing z/VM resources.

### Development and Editor Support

Open Mainframe Project editor packages include:

| Project | Description | Repository |
|---|---|---|
| z/VM REXX language support | REXX syntax highlighting | https://github.com/openmainframeproject/atompkg-language-zvm-rexx |
| z/VM assembler support | Assembler syntax highlighting | https://github.com/openmainframeproject/atompkg-languages-zvm |
| CMS NAMES support | CMS NAMES syntax highlighting | https://github.com/openmainframeproject/atompkg-language-zvm-names |
| SCRIPT/BookMaster support | GML syntax highlighting | https://github.com/openmainframeproject/atompkg-language-zvm-gml |

Some of these projects are older and should be considered historical development aids until their current maintenance status is verified.

---

## 4. Linux-on-Z Tools

A separate category includes tools that run inside Linux guests or Linux management servers but provide useful z/VM functionality.

### IBM s390-tools

- **Repository:** https://github.com/ibm-s390-linux/s390-tools

A collection of Linux utilities for IBM Z and LinuxONE.

Relevant utilities include:

| Tool | Description |
|---|---|
| cmsfs-fuse | Mount and access CMS minidisks from Linux |
| hyptop | Monitor z/VM and LPAR hypervisor activity |
| hmcdrvfs | Access files on HMC-attached media |
| qethqoat | Inspect OSA address information |

These are open-source Linux tools, not CMS EXECs or CP extensions.

They are nevertheless valuable components of a broader z/VM ecosystem catalog.

---

## 5. VM Workshop

- **Website:** https://www.vmworkshop.org/
- **Tools page:** https://www.vmworkshop.org/tools.shtml
- **2026 presentations:** https://www.vmworkshop.org/2026pres.shtml

VM Workshop is an important resource for the z/VM community.

It brings together VM customers, independent software vendors, business partners, and IBM developers.

Its archives contain presentations, technical papers, demonstrations, and links to software that may not be available through IBM's download library or GitHub.

---

## 6. Other Information Sources

The following resources provide additional opportunities to discover z/VM software, utilities, documentation, and technical information.

| Source | Description |
|---|---|
| https://www.ibm.com/support/pages/zvm/devpages/ | IBM z/VM developer pages and independent developer resources |
| https://www.ibm.com/support/pages/zvm/techinfo/ | IBM technical information |
| https://github.com/openmainframeproject/omp-landscape | Open Mainframe Project landscape |
| https://github.com/topics/zvm | GitHub z/VM repositories |
| https://github.com/topics/rexx | GitHub REXX projects |
| https://www.vmworkshop.org/ | VM Workshop presentations and archives |

---

## 7. Historical VM Community Resources

A significant amount of z/VM software predates GitHub and modern source-code hosting.

Historical archives are worth exploring because they contain utilities and contributions that may no longer be actively maintained but remain useful.

### VMSHARE

- **Archive:** https://vm.marist.edu/~vmshare/

VMSHARE was a major VM software-sharing resource for 22 years before closing in August 1998.

Its archives are worth investigating for historical CMS utilities, REXX EXECs, XEDIT macros, and other contributed software.

### IBM VM Mailing Lists

- **IBM list information:** https://www.ibm.com/support/pages/zvm/techinfo/listserv.html

Relevant mailing lists include:

| Mailing List | Subject |
|---|---|
| IBMVM | General z/VM discussions |
| VM-UTIL | VM utilities |
| CMSPIP-L | CMS Pipelines |
| SFS-L | CMS Shared File System |
| IBMTCP-L | VM TCP/IP |

Mailing list archives can reveal software announcements, shared code, technical discussions, and solutions that are difficult to find through conventional searches.

The IBMVM archive dates back to January 1994.

---

### Suggested Classification

Use three classifications to distinguish licensing and distribution status:

- **Open Source:** Source code is available under an identifiable open-source license.
- **Community Contributed:** Available for download, but licensing or source availability needs verification.
- **Commercial / Proprietary:** Useful in the z/VM ecosystem but not open source.

### Execution Environment

It is also important to distinguish where software runs:

1. **CP:** Runs as part of, or interacts directly with, the z/VM Control Program.
2. **CMS:** Runs in a CMS virtual machine.
3. **Linux Guest:** Runs inside Linux under z/VM.
4. **External Management:** Runs on an external Linux or other management system and manages z/VM through APIs or network interfaces.

---

## 10. Future Expansion

This catalog should be maintained as a community resource rather than a static list.

Potential future additions include:

- Automated discovery of GitHub repositories.
- Importing the IBM z/VM download package index.
- Reviewing VM Workshop presentation archives.
- Extracting software references from historical mailing lists.
- Identifying duplicate utilities distributed through multiple locations.
- Recording supported z/VM releases and maintenance status.
- Verifying software licenses and source availability.
- Identifying abandoned projects that may benefit from community maintenance.

The ultimate objective is to provide a single, searchable directory of software and technical resources available to the z/VM community, including both modern open-source projects and valuable historical contributions.

# z/VM Community Tools Catalog

This catalog combines the package entries from the IBM z/VM Download Packages page supplied as HTML with the community and independent projects listed in the `Other Sources of Community Tools` section of the Open Mainframe Project README.

- **IBM package entries extracted:** 504
- **IBM page last updated:** 26 October 2026 (as shown in the supplied HTML)
- **Additional community/project entries:** 28
- IBM URLs use the package index's `#search=` filter so each link opens the catalog filtered to that package.
- IBM descriptions are copied from the page's Abstract column; no descriptions have been invented.

## IBM z/VM Download Packages

| Name | Description | Source | URL |
| :--- | :--- | :--- | :--- |
| **ADDON** | CMS/GUI appl to add/change wakeup commands in RxServer based servers V1.4 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=ADDON |
| **B2H** | B2H: Convert Bookmaster, GML, Script/VS and "flat" files to HTML (Internet) Release 4.7 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=B2H |
| **BENCH** | Check how much resources a command uses; compare alternatives. V1.2 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=BENCH |
| **BFSLIST** | List a BFS filespace in a FILELIST/DIRLIST like way Version 3.2 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=BFSLIST |
| **BOX2BMS** | Draw box diagrams for BookMaster documents | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=BOX2BMS |
| **CGI4RTM** | CGIs on zLinux for RTM, VM TCP/IP, ACCOUNT command ; V1.10 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CGI4RTM |
| **CALCENT** | Calculate LPAR entitlement table from a MONWRITE file | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CALCENT |
| **CALWEEK** | Print OV/VM calendar information in various formats, including "daytimer". | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CALWEEK |
| **CGIs on zLinux for RTM, VM TCP/IP, ACCOUNT command ; V1.10** *(CGIs on zLinux)* | CGIs on zLinux for RTM, VM TCP/IP, ACCOUNT command ; V1.10 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CGI4RTM |
| **CHARLOTT** | Charlotte - fullscreen, textual World Wide Web browser for CMS | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CHARLOTT |
| **CHKAPARS** | CHKAPARS EXEC - Evaluates system APAR data for a selected z/VM component or all such components | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CHKAPARS |
| **CHKRECLM** | Tool to check the impact of a memory reclamation similar to the VIR2REAL tool. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CHKRECLM |
| **CHKSERV** | A CMS/GUI application to manage lots of RXSERVER based servers V0.7 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CHKSERV |
| **CHUG** | Script-driven test tool with HTML output and near-total control of test UserID. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CHUG |
| **CHUGDEMO** | Demonstration files for the CHUG tool; input and resulting HTML output. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CHUGDEMO |
| **CLONE620** | Create an IPLable copy (CLONE) of the running ZVM 6.2 system. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CLONE620 |
| **CLONEBKP** | Create an IPLable copy (CLONE) of the running ZVM system. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CLONEBKP |
| **CMS2CDL** | Convert a CMS formatted disk into Linux CDL format | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CMS2CDL |
| **CMSDDR** | Enhanced DDR program to simulate DDR tapes via CMS files | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CMSDDR |
| **CMSFMT** | DVF Aids for CMS Application Multitasking | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CMSFMT |
| **CMS Make** | Make-like build automation for CMS | Github | https://github.com/trothtech/cmsmake |
| **CMS TAR** | TAR archive utility for CMS | Github | https://github.com/trothtech/cmstar |
| **CMDTABLE** | Generate files listing all defined CP commands and diagnoses with the privilege classes. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CMDTABLE |
| **COLSIMPL** | COLS insert and COLS delete SIMPLE Xedit macros. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=COLSIMPL |
| **COMPARE** | Comparing files with XEDIT, Comparing minidisks (or FILELISTs). V1.9b | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=COMPARE |
| **CONCLOSE** | An exec to close all or selected consoles/prints at midnight V1.0 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CONCLOSE |
| **CONFROOM** | Schedule conference rooms and equipment across an entire site. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CONFROOM |
| **CP1STLVL** | CP exit allowing 2nd-level user to invoke 1st-level commands | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CP1STLVL |
| **CP3KVMXT** | v2.9l Create an input file for zPCR or zCP3000 from monitor data. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CP3KVMXT |
| **CP4ZVM72** | Tool check for service on a z/VM 7.1 system that is not in base of z/VM 7.2 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CP4ZVM72 |
| **CPHOST** | CP1STLVL*2: CP exit allowing 2nd-level user to invoke 1st-level cmds V1.4 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CPHOST |
| **CPLINKPW** | Avoid CP READ when LINKing to a minidisk | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CPLINKPW |
| **CPQUERY** | CMS GUI exec, issues CP Query commands and manages NSS V4.0.4 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CPQUERY |
| **CPUMF** | Report on D5 R13 MRPRCMFC CPU Measurement Facility counters. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CPUMF |
| **CUA2001** | Support development of Common User Access (CUA) panels for 3270 terminals | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=CUA2001 |
| **D0R16TOP** | Draws machine topology from a MONWRITE File | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=D0R16TOP |
| **D1R31** | Report on D1 R31 CP Service Configuration record. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=D1R31 |
| **D26C** | C language access to diagnose x'26C' (Info on Guest LANs, VSwitches etc.) | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=D26C |
| **D3R2EC** | Extract encrypted counter metrics from Domain 3, Record 2. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=D3R2EC |
| **D5R13CRY** | Report on D5 R13 MRPRCMFC CPU Measurement Facility CPACF counters. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=D5R13CRY |
| **DIRENT** | Extracts entries from the object directory. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DIRENT |
| **DIREXEC** | Execute or execload execs from non-accessed SFS directories. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DIREXEC |
| **DISASM** | z/Architecture machine-instruction disassembler | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DISASM |
| **DLIST** | A full-screen display of disks accessed by any CMS or GCS machine. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DLIST |
| **DMDQPIN** | Tool to display outstanding pages in vacating zones during memory reclamation. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DMDQPIN |
| **DMT-XX** | Directory Migration Tools | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DMT-XX |
| **DRM** | An XEDIT based interface to manage the CP Directory Version 5.2.1 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DRM |
| **DRMGUI** | A CMS/GUI interface to defragment VM disks Version 1.2.1 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DRMGUI |
| **DRPC** | Add-on to make DDR work with CMS PIPES | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DRPC |
| **DR_DRCT** | Directory fix-it tools: Move/expand DRCT area; find CMS minidisks; more. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DR_DRCT |
| **DUMPEDIT** | Replacement for DUMPLOAD allowing you to select which pages to load. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DUMPEDIT |
| **DYNAMO** | Linux DCSS management tool | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=DYNAMO |
| **ECHO** | Empty Rexx/Sockets-based, multi-client TCP server | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=ECHO |
| **EDCKD** | A tool to display and/or alter records on any CKD DASD. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=EDCKD |
| **EDFBA** | Displays and/or alters blocks on FBA DASD. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=EDFBA |
| **EDEVPATH** | FCP path management tool for EDEVs | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=EDEVPATH |
| **ERALIAS** | An exec to remove ERASEd ALIASes from the SFS catalog. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=ERALIAS |
| **EXECs** | REXX EXEC utilities, including WHICH and MAN | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools/tree/main/execs |
| **FCXTREND** | Pruning aid for IBM Performance Toolkit's FCXTREND files | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=FCXTREND |
| **FCXRENAM** | Sample FCXRENAM EXEC for Perfkit to automatically archive performance logs. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=FCXRENAM |
| **FCOPY** | * FCOPY - High speed CMS file copy routine with PACKLIB support | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=FCOPY |
| **FERRET** | FERRET - A program to search CMS files for character strings | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=FERRET |
| **FIXZMAN** | CMS program to consolidate a SMAPI zManager NOTEBOOK configuration file | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=FIXZMAN |
| **FILELIST** | Improvements to FILELIST, RDRLIST and EXECUTE Version 2.4.9a | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=FILELIST |
| **FILEMGR** | Organizes CMS files into folders, provides hiding options and expiration dates. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=FILEMGR |
| **FTPREXX** | FTP client and socksified tcpclient Pipeline stages, both originally from Steve Hayes | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=FTPREXX |
| **GD-XEDIT** | Various XEDIT Goodies from Kris Buelens V 1.5 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=GD-XEDIT |
| **GET370AC** | Check all logged on users for the 370ACCOM setting | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=GET370AC |
| **GETSTHYI** | GETSTHYI - issue STHYI function code 0 and format response. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=GETSTHYI |
| **GUICACHE** | CMS/GUI exec to view at 3990 cache statistics V1.0 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=GUICACHE |
| **GUIWDOC** | HTML documentation for GUIWIRE V1.2 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=GUIWDOC |
| **GUIWIRE** | CMS/GUI application to build other REXX CMS/GUI applications V4.5.1 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=GUIWIRE |
| **H2S** | H2S - Converts HTML to Script/VS (DCF) for fine printing with AFP or PostScript | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=H2S |
| **HELP** | Improvements to HELP: help with wildcards, more colors, better RRT V1.5 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=HELP |
| **HELPDESK** | Database of OV/VM Q&A's for help desk personnel, can add your own Q&A, too. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=HELPDESK |
| **HEXDUMP** | Browse data from any source in hexadecimal. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=HEXDUMP |
| **HISTORY** | The HISTORY command displays the contents of the CMS command history fil | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=HISTORY |
| **HOMUNC** | Platform for a self-aware operating system. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=HOMUNC |
| **HPALIAS** | Formatter for D6 R28 HyperPAV Alias Records | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=HPALIAS |
| **IMAP** | Internet Message Access Protocol server for TCP/IP | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=IMAP |
| **INSTPROD** | Automated install of IBM products for z/VM including Operations Manager, Backup and Restore Manager, Tape Manager, zSecure, and OMEGAMON XE. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=INSTPROD |
| **IOS3270** | Runtime files for IOS3270 (Display I/O facility) | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=IOS3270 |
| **KM** | This package is a CSL interface to the KMx cipher instructions; with Rexx Pipes stages showing their use. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=KM |
| **LCLQRY** | Local CP-exits providing queries to display your AUTOLOGGER or ALTUSER st | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LCLQRY |
| **LEXX** | LEXX, The Live Parsing Editor | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXX |
| **LEXXPLXX** | LEXXPLXX, LEXX Parsers for PL/I, PL/X, Modula-2 and Pascal | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXPLXX |
| **LIBRCMS** | VSE/ESA Librarian Server for CMS users | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LIBRCMS |
| **LINMON** | MONWRITE Collector | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LINMON |
| **LISTSG** | A series of FILELIST-like tools V1.8 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LISTSG |
| **LIVE** | Sample web access to SMAPI functionality | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LIVE |
| **LXC** | Run CMS commands from a TCP connected system (V1.4.2) | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LXC |
| **LXCMS** | Linux access to CMS resources | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=LXCMS |
| **MAILIT** | MAILIT is a general purpose VM e-mail sender program. V3.4.c | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=MAILIT |
| **MAPALLOC** | Displays the allocation map on a CP-owned volume. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=MAPALLOC |
| **MDSK** | A few Minidisk related tools & DEFINE MDISK aids V0.9 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=MDSK |
| **MONCLEAN** | Clean up MONWRITE disk of Monwrite files. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=MONCLEAN |
| **MONRIP** | Extract time-range of data from a MONWRITE file. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=MONRIP |
| **MONVIEW** | Tools to look at raw z/VM monitor data captured by Monwrite. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=MONVIEW |
| **MONWATCH** | Feed CP Monitor records to a user-written Pipelines stage | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=MONWATCH |
| **MULTISRV** | Multiple protocol server for TCP/IP | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=MULTISRV |
| **NETLIST** | A FILELIST for RSCS Network Files and Links Version 2.9 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=NETLIST |
| **NONAMES** | Avoid NAMEFIND lookup for SFS administrative commands | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=NONAMES |
| **OTTOSCR** | Screen scroller for Fullscreen CMS | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=OTTOSCR |
| **OVASST** | Consolidated end user tailoring of OfficeVision/VM functions. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=OVASST |
| **PCR** | The PCR utility enables CMS commands, subcommands, and Rexx functions/subroutines to be written in PL/I. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PCR |
| **PF10PF11** | PF10 and PF11 XEDIT macros allow to move from left to right, based on the position of the cursor in the delimited area defined by the SET Verify XEDIT command. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PF10PF11 |
| **PICKPIPE** | Choose between default VM, Marist, and test runtime versions of Pipelines | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PICKPIPE |
| **PIGS** | An exec that can be used to determine who is using too much spool space. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PIGS |
| **PIPEDDR** | Dump/Restore a disk to a file, ftp server, or over TCP/IP to a remote system. Supports compression, digest verification, and secure connections. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPEDDR |
| **PIPESERV** | A Pipeline Server. A driver for service machines. Version 1.2.4. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPESERV |
| **PRFCOPY** | The most complete "cut&paste" for XEDIT V4.2.f | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFCOPY |
| **PRFIT** | Wrapper to invoke PERFKIT BATCH | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFIT |
| **PRFRUN** | A server to automate VMPRF & MONWRITE. Also remote cmds V3.3.a | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFRUN |
| **PRFVIEW** | Have a decent view on VMPRF listings: we use CMSGUI Version 2.2 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFVIEW |
| **PRFGUI** | A CMSGUI interface for VMPRF Trend & Summary files Version 1.13 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFGUI |
| **PTKGUI** | A CMSGUI interface for PTK Summary files Version 1.0.a | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PTKGUI |
| **PTKTOOLS** | PTKTOOLS contains some simple PERFKIT related execs + ctl files V1.2 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PTKTOOLS |
| **PTKVIEW** | Have a decent view on VMPTK listings: we use CMSGUI Version 1.0.a | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PTKVIEW |
| **PUTFILES** | PUTFILES is the converse of GETFILES Pipelines stage V2.2 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PUTFILES |
| **PWCHECK** | HTTP Basic Authentication Exit for ISFC Collection | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=PWCHECK |
| **Q_SMAPI** | SMAPI - Query Dir. Manager Level & Query API Func. Level API clients | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=Q_SMAPI |
| **QDASD** | Display information about DASD devices in table form. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=QDASD |
| **QDEVS** | QDEVS displays devices owned by the system or a virtual machine. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=QDEVS |
| **QDIR** | Make your interactions with DIRMAINT much quicker and easier. Instantly review a USER/IDENTITY/PROFILE by displaying it on screen. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=QDIR |
| **QDISK** | A quadri-modal repackaging of XASTOR, QDISK, DLIST and QDEVS V1.5.2 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=QDISK |
| **QRYWWPNS** | Find out which FCP & WWPNs can reach a given LUN Version 1.0 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=QRYWWPNS |
| **QSSIMEM** | SMAPI routine to return SSI Member of an active virtual machine | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=QSSIMEM |
| **R4MON** | Report on VM66095 EDEV FCP chpid and device records. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=R4MON |
| **RACHELP** | Create normal CMS Help files for RACF from RACF help facility files. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RACHELP |
| **RELODOM** | Displays the relocation domains in a member of an SSI. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RELODOM |
| **RENSSI** | Rename a member of an SSI | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RENSSI |
| **RETBUF** | Fullscreen CP retrieve buffer selection panel. Version 2.1.2. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RETBUF |
| **REXXG** | EXECs and XEDIT macros for the REXX programmer Version 1.1 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=REXXG |
| **REXXIUCV** | IUCV interface for REXX | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=REXXIUCV |
| **RRTGEN** | Generate Rail Road Track syntax diagrams from user written SYNTAX files. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RRTGEN |
| **RSCSOP** | RSCSOP is a service machine to provide dynamic AUTH control over printers. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RSCSOP |
| **RSK-GA** | RSK Extras (GA level) | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RSK-GA |
| **RSKFIX** | Reusable Server Kernel (RSK) fix pack | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RSKFIX |
| **RUNREXX** | A framework to develop crossplatform Rexx programs using the eclipse framework | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RUNREXX |
| **RXSERVER** | A kernel to build REXX WAKEUP servers, such as VMUTIL. V6.7 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=RXSERVER |
| **SCIF** | Easier "talking" to SCIFfed users (avoid the CP SEND command) V1.4 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SCIF |
| **SCKSMAPI** | Socket access to SMAPI functions | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SCKSMAPI |
| **SCKXPIPE** | Socket access to XPIPES functions | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SCKXPIPE |
| **SDOENA54** | Enabling Aid files for z/VM 5.4.0 SDO configuration. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SDOENA54 |
| **SEARCH** | Search Engine for VM-Hosted Web Sites | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SEARCH |
| **SELFLGR** | Relocate a connected user to another SSI member | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SELFLGR |
| **SERVEPDF** | View a PDF file from the CMS session in the web browser | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SERVEPDF |
| **SESTOOLS** | SESTOOLS has tools to make working with VM/SES easier V1.3 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SESTOOLS |
| **SETDATE** | SETDATE EXEC - Set the date of last update on CMS or SFS files. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SETDATE |
| **SETVMDBK** | Dynamically change user options in VMDBK (eg MAINTCCW) V1.3 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SETVMDBK |
| **SFCOUNTR** | SFCOUNTR makes a list of users with more than a requested number of spool files. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SFCOUNTR |
| **SFSKTOOL** | Various tools related to SFS management. V1.0 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SFSKTOOL |
| **SFSULIST** | SFSUserList lets you handle SFS users in a FILELIST like way V1.13 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SFSULIST |
| **SHAREDQS** | Shared CMS Queues over DCSS | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SHAREDQS |
| **SHUTTRAP** | CMS program to detect and react to CP SHUTDOWN signals | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SHUTTRAP |
| **SMAPIREX** | Rexx routine to simplify the invocation of smapi | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SMAPIREX |
| **SMARTX** | An XEDIT-based front-end for RTM/ESA and VM/RTM (known as SMART) V6.3.f | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SMARTX |
| **SMTMET** | Extract SMT Metrics from Domain 0, Record 2. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SMTMET |
| **SPFPACK** | SPFPACK determines which spool files have data on a particular spool pack. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SPFPACK |
| **SPOOLAID** | Full-screen browser for spool file internals | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLAID |
| **SPOOLCHN** | System Programmer/System Operator Extended Spool Query Commands | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLCHN |
| **SPOOLKIT** | Show SPOOL utilization details and allow viewing/manipulating SPOOL files (replaces SFLIST package) | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLKIT |
| **SPOOLPIG** | Display the largest spool files and users of the spool on a system. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLPIG |
| **SQLITE** | SQLite is a C-language library that implements a small, self-contained, high-reliability, full-featured, SQL database engine, ported to CMS. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SQLITE |
| **SRCHLIST** | An XEDIT macro that can search through files from FILELIST or MACLIST | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SRCHLIST |
| **SRMTIDLE** | Sets value of CP dispatcher "test-idle" timer | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SRMTIDLE |
| **SSIQSERV** | Issue Q CPSERVICE on all SSI members and show differences in the active fixes. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SSIQSERV |
| **SYSLOGD** | SYSLOGD daemon for CMS | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=SYSLOGD |
| **TAB2GC** | Draw charts entirely on CMS | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TAB2GC |
| **TCVM1** | Advanced REXX Telecourse (an HTML selfstudy course) V1.3 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TCVM1 |
| **TCVM2** | CMS Pipelines Telecourse (an HTML selfstudy course) V1.3 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TCVM2 |
| **TIMEBOMB** | Set, snooze or cancel the CP timebomb (diagnose 288) feature from CMS. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TIMEBOMB |
| **TIMESERV** | VM/TimeServ - An SNTP Version 4 Time Server for VM/ESA and z/VM | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TIMESERV |
| **TLD** | TCP/IP line driver for CMS distributed queues. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TLD |
| **TOOLS** | User interface program for managing and updating TOOLSRUN maintained disks. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLS |
| **TOOLSRUN** | TOOLSRUN Distributed Master/Shadow Disks and Conference Manager | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLSRUN |
| **TRACEXEC** | An interactive debugger for REXX execs; a tool for analyzing EXEC applications. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/down |
| **TRF2TCPD** | Convert VM TCP/IP Packet Trace to Linux tcpdump format | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TRF2TCPD |
| **TRSOURCE** | TOOLSRUN Package, additional source files | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TRSOURCE |
| **TSLAMON** | REXX to exploit CP monitor data in real time eg user %CPU, %WAIT V1.1 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TSLAMON |
| **TZDATES** | Generation of the TIMEZONE_BOUNDARY statements to use in the SYSTEM CONFIG. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=TZDATES |
| **VIFWWW** | Web commander for z/VM System Administration Facility V2.10 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=VIFWWW |
| **VIR2REAL** | Compute the Virtual to Real storage (memory) ratio of running users in a VM LPAR. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=VIR2REAL |
| **VMADMANY** | VMADMIN client anywhere | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=VMADMANY |
| **VMMENU** | Easy selection menu presentation for CMS V2.0 | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=VMMENU |

| **VMLINK** | CMS file and software linking automation | Github | https://github.com/trothtech/vmlink |

| **VMLOGS** | Create an automatic managed repository for Consoles and data files. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=VMLOGS |
| **VMREVIEW** | EXEC to check the major changes to a z/VM system if migrating to z/VM 6.4.0. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=VMREVIEW |
| **VMSERVE** | A Disconnected Virtual Machine manager for VM that handles reader files, messages and time-of-day events. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=VMSERVE |
| **X_SMAPI** | SMAPI - Image_Disk_Delete_DM & Image_Volume_Space_Remove_DM API clients | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=X_SMAPI |
| **XASTOR** | A multi-functioned, programmable, full-screen storage display | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=XASTOR |
| **XBROWSE** | XBROWSE is a compiled REXX replacement for PEEK and BROWSE (in module form) | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=XBROWSE |
| **XFILE** | Displays files being XEDITed by other users. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=XFILE |
| **XMLPARSE** | Parse XML document into a tree structure easily processed in REXX | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=XMLPARSE |
| **XMM** | XMIT message management utility | Github | https://github.com/trothtech/xmm |
| **XPIPES** | cross-machine pipelines | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=XPIPES |
| **ZNETBOOT** | Network booting tools | Github | https://github.com/trothtech/znetboot |
| **zPXE** | PXE-like network boot functionality for z/VM guests | Github | https://github.com/beaker-project/zpxe |
| **ZXCATIVP** | Preparation script for the Installation Verification Program for xCAT and OpenStack on z/VM. | z/VM Downloads | https://www.ibm.com/support/pages/zvm/download/packages/#search=ZXCATIVP |

## Other Community Tools and Projects

| Name | Description | Source | URL |
|---|---|---|---|
| EXECs | CMS REXX EXEC utilities, including WHICH and MAN | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools/tree/main/execs |
| DMSCMD | Additional commands and history functionality for Directory Maintenance | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools/tree/main/dmscmd |
| ZLMA | z/VM and Linux Modern Administration | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools/tree/main/zlma |
| ZTRUST | PGP keys and trust-related facilities | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools/tree/main/ztrust |
| CPHOST | CP host-related utilities | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools/tree/main/cphost |
| TSC | Additional community tooling | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools/tree/main/tsc |
| Scripts | Supporting automation and scripts | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools/tree/main/scripts |
| AUTO.VMLINK | VMLINK-related automation | z/VM Community Tools | https://github.com/openmainframeproject/zvm-community-tools |
| Feilong | Open-source REST API and SDK for provisioning and managing z/VM guests, images, networks, and volumes | Independent GitHub | https://github.com/openmainframeproject/feilong |
| IBM zvm_ansible | Ansible automation for z/VM using SMAPI and the Feilong ecosystem | Independent GitHub | https://github.com/IBM/zvm_ansible |
| IBM zvm_ansible_collection | Ansible collection for z/VM automation | Independent GitHub | https://github.com/IBM/zvm_ansible_collection |
| Terraform Provider for z/VM | Terraform integration with the z/VM SDK/Feilong ecosystem | Independent GitHub | https://github.com/mfcloud/terraform-provider-zvmsdk |
| VMLINK | CMS file and software linking automation | Independent GitHub | https://github.com/trothtech/vmlink |
| zPXE | PXE-like network boot functionality for z/VM guests | Independent GitHub | https://github.com/beaker-project/zpxe |
| CMS TAR | TAR archive utility for CMS | Independent GitHub | https://github.com/trothtech/cmstar |
| z/VM REXX language support | REXX syntax highlighting | Open Mainframe Project | https://github.com/openmainframeproject/atompkg-language-zvm-rexx |
| z/VM assembler support | Assembler syntax highlighting | Open Mainframe Project | https://github.com/openmainframeproject/atompkg-languages-zvm |
| CMS NAMES support | CMS NAMES syntax highlighting | Open Mainframe Project | https://github.com/openmainframeproject/atompkg-language-zvm-names |
| SCRIPT/BookMaster support | GML syntax highlighting | Open Mainframe Project | https://github.com/openmainframeproject/atompkg-language-zvm-gml |
| cmsfs-fuse | Mount and access CMS minidisks from Linux | IBM s390-tools | https://github.com/ibm-s390-linux/s390-tools |
| hyptop | Monitor z/VM and LPAR hypervisor activity | IBM s390-tools | https://github.com/ibm-s390-linux/s390-tools |
| hmcdrvfs | Access files on HMC-attached media | IBM s390-tools | https://github.com/ibm-s390-linux/s390-tools |
| qethqoat | Inspect OSA address information | IBM s390-tools | https://github.com/ibm-s390-linux/s390-tools |

## Source Notes

- IBM package data: [IBM z/VM Download Packages](https://www.ibm.com/support/pages/zvm/download/packages/).
- Community/project data: [Open Mainframe Project z/VM Community Tools README](https://github.com/openmainframeproject/zvm-community-tools#other-sources-of-community-tools).
- The README describes the IBM examples as representative rather than exhaustive; the IBM section above is populated from the supplied complete package-page HTML.
- A package being listed in IBM's download library does not by itself establish that it is open source. Check each package's license and source availability.
