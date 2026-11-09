![zz/VM Community Tools/VM Community Tools Logo](https://raw.githubusercontent.com/openmainframeproject/artwork/5b27f85f886da75ddf53511eb5289c53c972415c/projects/zvm-community-tools/horizontal/color/zvm-community-tools-horizontal-color.svg)

# z/VM Community Tools

This is the z/VM Community Tools github repository.  Its goal is to:
1.  Store and maintain a set of z/VM Free and Open Source Software
1.  List **all** z/VM Free and Open Source Software 

If you'd like to help, email Mike MacIsaac at mike99mac@gmail.com

## Table of Contents

- [Overview](#overview-section)
- [Open Mainframe Project](#ibm-zvm-download-library-section)
- [IBM z/VM Download Library](ibm-zvm-download-library-section)
- [Independent GitHub Projects](#independent-github-projects-section)
- [Linux-on-Z Tools](#linux-on-z-tools-section)
- [VM Workshop](#vm-workshop-section)
- [Other Information Sources](#other-information-sources-section)
- [Historical VM Community Resources](#historical-vm-community-resources-section)
- [Complete table of z/VM Open Source pacakges](#complete-table-section)

---

# <a id="overview-section">1. Overview</a>
This section is an overview of this git repository.

## Install

Each subdirectory has its own install process:  
- ``execs/`` - Download the ``https://github.com/openmainframeproject/zvm-community-tools/blob/main/execs/zvmtools.vmarc`` file, copy it to z/VM in binary, and unpack it with the ``VMARC UNPK`` command.
- ``dmscmd/`` - Follow the instructions here: https://github.com/openmainframeproject/zvm-community-tools/tree/main/dmscmd#building-dmscmd 
- ``zlma`` - There is an install script ``instzlma`` that is described in detail.

## Build

Each subdirectory has its own build process, if any:  
- ``execs`` - Because REXX EXECs are interpreted, there is no build process necessary.  There is a VMARC file that can be copied and expanded to put all EXECs onto one minidisk.

TODO: describe other packages with build steps 

## Discussion

You can connect with the community in a variety of ways. Here are some discussion forums: 

- [IBMVM Mailing list](http://listserv.uark.edu/cgi-bin/wa?A0=IBMVM)
- [z/VM Community Tools channel on Open Mainframe Project Slack](https://openmainframeproject.slack.com/archives/C035HAMNUU9)
- [z/VM Community Tools category on Open Mainframe Project Community Forums](https://community.openmainframeproject.org/)

## Contributing

Anyone can contribute to the z/VM Community Tools project - see: [CONTRIBUTING.md](CONTRIBUTING.md)

## Governance

z/VM Community Tools is a project hosted by the [Open Mainframe Project](https://openmainframeproject.org). This project has established it's own processes for managing day-to-day processes in the project at [GOVERNANCE.md](GOVERNANCE.md).

# <a id="open-mainframe-project-section">2. Open Mainframe Project</a>
This section describes tools hosted under the Open Mainframe Project ecosystem, including, but not limited to this repository.

- **This repository:** https://github.com/openmainframeproject/zvm-community-tools

This repository includes these packages:

| Directory | Description |
|---|---|
| [cphost](https://github.com/openmainframeproject/zvm-community-tools/tree/main/cphost) | allows a second-level z/VM guest issue CP commands at the first-level z/VM |
| [dmscmd](https://github.com/openmainframeproject/zvm-community-tools/tree/main/dmscmd) | Provides CMS "command editing": re-executing a previous command by typing = and hitting enter; or ? to retrieve it |
| [execs](https://github.com/openmainframeproject/zvm-community-tools/tree/main/execs) | REXX EXECs, many mimicing Linux commands such as ``grep``, ``man`` and ``which`` |
| [ipgate-v6](https://github.com/openmainframeproject/zvm-community-tools/tree/main/ipgate-v6) | Provides IPv6 gateway configuration, routing, and network management components |
| [zlma](https://github.com/openmainframeproject/zvm-community-tools/tree/main/zlma) | z/VM and Linux Modern Administration provides a Web interface from Linux for systems administration tasks |
| [znetboot](https://github.com/openmainframeproject/zvm-community-tools/tree/main/znetboot) | Network boot facilities |
| AUTO.VMLINK | VMLINK-related automation |

See the repository README for current components, installation procedures, and documentation.

# <a id="ibm-zvm-download-library-section">3. IBM z/VM Download Library</a>
References and links pointing to official IBM z/VM downloadable packages and utilities.

- **Main download page:** https://www.ibm.com/support/pages/zvm/download/
- **Package index:** https://www.ibm.com/support/pages/zvm/download/packages/
- **Developer pages:** https://www.ibm.com/support/pages/zvm/devpages/
- **Technical information:** https://www.ibm.com/support/pages/zvm/techinfo/

The IBM download library is the traditional central location for z/VM contributed software.

It includes utilities developed by IBM employees, customers, independent developers, and other members of the VM community.

**Licensing note:** The IBM download library is a distribution repository, not a guarantee that every package is open source. Check the licensing terms and source availability of individual packages.

---

# <a id="independent-github-projects-section">4. Independent GitHub Projects</a>

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

# <a id="linux-on-z-tools-section">5. Linux-on-Z Tools</a>
Tools specifically designed to support Linux workloads running on IBM Z mainframes.

A separate category includes tools that run inside Linux guests or Linux management servers but provide useful z/VM functionality.

## IBM s390-tools

- **Repository:** https://github.com/ibm-s390-linux/s390-tools

A collection of Linux utilities for IBM Z and LinuxONE. It is usually incorporated into zLinux distributions, so installing it separately is not needed.

Relevant utilities include:

| Tool | Description |
|---|---|
| cmsfs-fuse | Mount and access CMS minidisks from Linux |
| hyptop | Monitor z/VM and LPAR hypervisor activity |
| hmcdrvfs | Access files on HMC-attached media |
| qethqoat | Inspect OSA address information |

---

# <a id="vm-workshop-section">6. VM Workshop</a>
Resources, presentations, and code shared during annual VM Workshop events.

- **Website:** https://www.vmworkshop.org/
- **Tools page:** https://www.vmworkshop.org/tools.shtml
- **Past tapes:** https://www.vmworkshop.org/pastTape.shtml
- **2026 presentations:** https://www.vmworkshop.org/2026pres.shtml

VM Workshop is an important resource for the z/VM community.
It brings together VM customers, independent software vendors, business partners, and IBM developers.

Its archives contain presentations, technical papers, demonstrations, and links to software that may not be available through IBM's download library or GitHub.

---

# <a id="other-information-sources-section">7. Other Information Sources</a>
External documentation, mailing lists, and reference materials.

The following resources provide additional opportunities to discover z/VM software, utilities, documentation, and technical information.

| Source | Description |
|---|---|
| https://www.ibm.com/support/pages/zvm/devpages/ | IBM z/VM developer pages and independent developer resources |
| https://www.ibm.com/support/pages/zvm/techinfo/ | IBM technical information |
| https://github.com/topics/zvm | GitHub z/VM repositories |
| https://github.com/topics/rexx | GitHub REXX projects |
| https://www.vmworkshop.org/ | VM Workshop presentations and archives |

---

# <a id="historical-vm-community-resources-section">8. Historical VM Community Resources</a>
Archives and legacy code from historical VM community repositories. Most of these tools have probably not been maintained for years, but they still may be useful

| Name | Source | Description |
|---|---|---|
| VMSES Packages | https://download.sinenomine.net/vmses/ | VMSES packages from Sine Nomine Associates | 
| VMSHARE | https://vm.marist.edu/~vmshare/ | VMSHARE was a major VM software-sharing resource for 22 years before closing in August 1998.  Its archives are worth investigating for historical CMS utilities, REXX EXECs, XEDIT macros, and other contributed software. |
| VM Workshop tools | https://www.vmworkshop.org/tools.shtml | 

## IBM VM Mailing Lists

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

# <a id="complete-table-section">9. Complete table of all z/VM Open Source packages</a>

This catalog combines the package entries from the IBM z/VM Download Packages page supplied as HTML with the community and independent projects listed in the `Other Sources of Community Tools` section of the Open Mainframe Project README.

| Name | Description | Source |
| :--- | :--- | :--- |
YOOOO
| **$SUBSET** | An elegant entry and exit to/from CMS SUBSET. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=$SUBSET) |
| **ADDNAME** | Add entry to NAMES while in PEEK or NOTEBOOK | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ADDNAME) |
| **ADDON** | CMS/GUI appl to add/change wakeup commands in RxServer based servers V1.4 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ADDON) |
| **ANALYSE** | Draw flow lines and structure for 370 assembler programmes | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ANALYSE) |
| **ASKPMAN** | To display Full screen in CUA standard with REXX | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ASKPMAN) |
| **B2H** | B2H: Convert Bookmaster, GML, Script/VS and "flat" files to HTML (Internet) Release 4.7 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=B2H) |
| **BENCH** | Check how much resources a command uses; compare alternatives. V1.2 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=BENCH) |
| **BFSLIST** | List a BFS filespace in a FILELIST/DIRLIST like way Version 3.2 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=BFSLIST) |
| **BLOCK** | Perform XEDIT operations on a Block/box of data | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=BLOCK) |
| **BOX2BMS** | Draw box diagrams for BookMaster documents | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=BOX2BMS) |
| **CALCENT** | Calculate LPAR entitlement table from a MONWRITE file | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CALCENT) |
| **CALWEEK** | Print OV/VM calendar information in various formats, including "daytimer". | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CALWEEK) |
| **CASEWRD** | Change the case of a word in XEDIT | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CASEWRD) |
| **CCC** | Cut and Paste for VM! Contains CCC and FFF | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CCC) |
| **CC** | Compares TOD clocks of two VM systems. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CC) |
| **CGI4RTM** | CGIs on zLinux for RTM, VM TCP/IP, ACCOUNT command ; V1.10 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CGI4RTM) |
| **CGLOBALS** | Incl. GLOBAL TXTLIBs & LOADLIBs in a C/370 load module. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CGLOBALS)
| **CHARLOTT** | Charlotte - fullscreen, textual World Wide Web browser for CMS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHARLOTT) |
| **CHAT** | Network chatting tool demonstrating various CMS APIs. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHAT) |
| **CHECKREF** | Checks BookMaster symbols and cross-references | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHECKREF) |
| **CHGPROFX** | Alternate CHARGE Profile System | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHGPROFX) |
| **CHKAPARS** | CHKAPARS EXEC - Evaluates system APAR data for a selected z/VM component or all such components | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHKAPARS) |
| **CHKDEV** | CHKDEV/GDDMTERM - Terminal Recognition and GDDM Setup | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHKDEV) |
| **CHKPACK** | Check a PACKAGE file against TOOLS disk. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHKPACK) |
| **CHKRECLM** | Tool to check the impact of a memory reclamation similar to the VIR2REAL tool. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHKRECLM) |
| **CHKSERV** | A CMS/GUI application to manage lots of RXSERVER based servers V0.7 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHKSERV) |
| **CHUGDEMO** | Demonstration files for the CHUG tool; input and resulting HTML output. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHUGDEMO) |
| **CHUG** | Script-driven test tool with HTML output and near-total control of test UserID. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CHUG) |
| **CKDDRTAP** | Checks the contents of a DDR tape. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CKDDRTAP) |
| **CKDSVRST** | Multi-purpose DASD backup/restore program also NON-CMS. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CKDSVRST)
| **CLCDAT** | Add or subtract days from a date in SCRIPT or BookMaster | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CLCDAT) |
| **CLONE620** | Create an IPLable copy (CLONE) of the running ZVM 6.2 system. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CLONE620) |
| **CLONEBKP** | Create an IPLable copy (CLONE) of the running ZVM system. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CLONEBKP) |
| **CMDTABLE** | Generate files listing all defined CP commands and diagnoses with the privilege classes. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CMDTABLE) |
| **CMR** | A Generic Conversation Management Routine | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CMR) |
| **CMS2CDL** | Convert a CMS formatted disk into Linux CDL format | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CMS2CDL) |
| **CMSDDR** | Enhanced DDR program to simulate DDR tapes via CMS files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CMSDDR) |
| **CMSFMT** | DVF Aids for CMS Application Multitasking | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CMSFMT) |
| **CMSFS Util** | CMS EDF FS tool no mount needed | [Github](https://github.com/trothtech/cmsfs) |
| **CMS Make** | Make-like build automation for CMS | [Github](https://github.com/trothtech/cmsmake) |
| **CMS NAMES support** | CMS NAMES syntax highlighting | [GitHub](https://github.com/openmainframeproject/atompkg-language-zvm-names) |
| **CMS TAR** | TAR archive utility for CMS | [Github](https://github.com/trothtech/cmstar) |
| **CODE** | Front end to CIPHER product. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CODE) |
| **COLRXTND** | Extension to the COLORS package. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=COLRXTND) |
| **COLSIMPL** | COLS insert and COLS delete SIMPLE Xedit macros. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=COLSIMPL) |
| **COMMENTR** | XEDIT Macros for Adding Line and Block Comments to Files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=COMMENTR) |
| **COMPARE** | Comparing files with XEDIT, Comparing minidisks (or FILELISTs). V1.9b | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=COMPARE) |
| **COMPUTE** | REXX mathematics for each record in a pipeline. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=COMPUTE) |
| **CONCH** | Shell for CMS. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CONCH) |
| **CONCLOSE** | An exec to close all or selected consoles/prints at midnight V1.0 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CONCLOSE) |
| **CONINT** | CMS task switching by Console Interrupt at any time | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CONINT) |
| **CONS** | Console Spooling made simple. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CONS) |
| **COUNTER** | A CGI script to produce a graphical web page counter | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=COUNTER) |
| **CP1STLVL** | CP exit allowing 2nd-level user to invoke 1st-level commands | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CP1STLVL) |
| **CP3KVMXT** | v2.9l Create an input file for zPCR or zCP3000 from monitor data. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CP3KVMXT) |
| **CP4ZVM72** | Tool check for service on a z/VM 7.1 system that is not in base of z/VM 7.2 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CP4ZVM72) |
| **CPDUMPTL** | CP Dump Tool, a dump scanning program for VM/ESA CP dumps | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CPDUMPTL) |
| **CPGRAB** | Innocuous CP exit demonstration, easily modified to grab/release locks. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CPGRAB) |
| **CPHOST** | CP exit allowing 2nd-level user to invoke 1st-level cmds V1.4 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CPHOST) |
| **CPICSAMP** | Sample programs for CMS CPI Communications. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CPICSAMP) |
| **CP_IP** | CP_IP - CP mod to add IP address awareness to CP | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CP_IP) |
| **CPLINKPW** | Avoid CP READ when LINKing to a minidisk | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CPLINKPW) |
| **CPQUERY** | CMS GUI exec, issues CP Query commands and manages NSS V4.0.4 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CPQUERY) |
| **CPUMF** | Report on D5 R13 MRPRCMFC CPU Measurement Facility counters. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CPUMF) |
| **CQ** | Query Status of Local or Remote Network Users | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CQ) |
| **CRDELCMP** | Compare 2 source files and create optimum update file. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CRDELCMP) |
| **CUA2001** | Support development of Common User Access (CUA) panels for 3270 terminals | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CUA2001) |
| **CUTPASTE** | XEDIT macros CUT and PASTE to easily move and copy text | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=CUTPASTE) |
| **D0R16TOP** | Draws machine topology from a MONWRITE File | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=D0R16TOP) |
| **D1R31** | Report on D1 R31 CP Service Configuration record. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=D1R31) |
| **D26C** | C language access to diagnose x'26C' (Info on Guest LANs, VSwitches etc.) | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=D26C) |
| **D3R2EC** | Extract encrypted counter metrics from Domain 3, Record 2. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=D3R2EC) |
| **D5R13CRY** | Report on D5 R13 MRPRCMFC CPU Measurement Facility CPACF counters. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=D5R13CRY) |
| **DAILY** | DAILY Package | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DAILY) |
| **DATECNVT** | DATECNVT EXEC - Converts/validates date input to another date format. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DATECNVT) |
| **DCLGEN** | Create host variable declaration for an SQL Table | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DCLGEN) |
| **DELMACS** | Set of macros to selectively delete data | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DELMACS) |
| **DEPT** | Do various things with DEPARTMENT LISTS. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DEPT) |
| **DESCRIBE** | Describe the contents of files in a FILELIST/FILELELS display. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DESCRIBE) |
| **DIAG00E4** | Diagnose E4 CSL routine. Get minidisk info, create overlay. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DIAG00E4) |
| **DIRENT** | Extracts entries from the object directory. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DIRENT) |
| **DIREXEC** | Execute or execload execs from non-accessed SFS directories. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DIREXEC) |
| **DIRLIST** | Dirlist update to add FILEPOOL and SUBDIR tag support with NICK option | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DIRLIST) |
| **DISASM** | z/Architecture machine-instruction disassembler | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DISASM) |
| **DISKPUT** | Frontend EXEC for NAMEFIND and PROFS name files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DISKPUT) |
| **DLIST** | A full-screen display of disks accessed by any CMS or GCS machine. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DLIST) |
| **DMDQPIN** | Tool to display outstanding pages in vacating zones during memory reclamation. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DMDQPIN) |
| **DMGR** | Dialog Manager for EnterpriseWeb/VM | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DMGR) |
| **DMSCMD** | Additional commands and history functionality for Directory Maintenance | [z/VM Community Tools](https://github.com/openmainframeproject/zvm-community-tools/tree/main/dmscmd) |
| **DMSG** | Display a message on 3480 operator panel | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DMSG) |
| **DMSXMS** | Modified Sort module for Xedit | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DMSXMS) |
| **DMT-XX** | Directory Migration Tools | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DMT-XX) |
| **DR_DRCT** | Directory fix-it tools: Move/expand DRCT area; find CMS minidisks; more. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DR_DRCT) |
| **DRM** | An XEDIT based interface to manage the CP Directory Version 5.2.1 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DRM) |
| **DRMGUI** | A CMS/GUI interface to defragment VM disks Version 1.2.1 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DRMGUI) |
| **DRPC** | Add-on to make DDR work with CMS PIPES | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DRPC) |
| **DTSCAN** | Storage scan tool | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DTSCAN) |
| **DUMPEDIT** | Replacement for DUMPLOAD allowing you to select which pages to load. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DUMPEDIT) |
| **DUPL** | Establish 3990 duplex pair | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DUPL) |
| **DYNAMO** | Linux DCSS management tool | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=DYNAMO) |
| **ECHO** | Empty Rexx/Sockets-based, multi-client TCP server | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ECHO) |
| **EDCKD** | A tool to display and/or alter records on any CKD DASD. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EDCKD) |
| **EDEVPATH** | FCP path management tool for EDEVs | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EDEVPATH) |
| **EDFBA** | Displays and/or alters blocks on FBA DASD. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EDFBA) |
| **EDSAY** | Used to print messages with the editor in control or on screen | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EDSAY) |
| **ELAPSE** | Date functions on a given date or absolute day number. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ELAPSE) |
| **EMAIL** | Pipelines SMTP Protocol EMAIL Stage | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EMAIL) |
| **ENAMER** | Enhanced reNAMER, especially for FULIST/FILELIST/FILELELS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ENAMER) |
| **ERALIAS** | An exec to remove ERASEd ALIASes from the SFS catalog. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ERALIAS) |
| **EWEBSTAT** | Status Display for EnterpriseWeb/VM (Shadow VM | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EWEBSTAT) |
| **EXCIT** | Extract citations in context from BookMaster files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EXCIT) |
| **execs** | REXX EXEC utilities, including WHICH and MAN | [z/VM Community Tools](https://github.com/openmainframeproject/zvm-community-tools/tree/main/execs) |
| **EXECUTE2** | Modified EXECUTE to support DESCRIBE PACKAGE. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EXECUTE2) |
| **EXPLAIN** | EXPLAIN | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EXPLAIN) |
| **EXTMSG** | XEDIT screen builder VERSION 2. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EXTMSG) |
| **EZMENU** | EZMENU an IOSMENU compatible tool to write Menu | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=EZMENU) |
| **FCOPY** | High speed CMS file copy routine with PACKLIB support | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FCOPY) |
| **FCXRENAM** | Sample FCXRENAM EXEC for Perfkit to automatically archive performance logs. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FCXRENAM) |
| **FCXTREND** | Pruning aid for Performance Toolkit's FCXTREND files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FCXTREND) |
| **feilong** | An open-source REST API and SDK for provisioning and managing z/VM guests, images, networks, and volumes. | [Github](https://github.com/openmainframeproject/feilong) |
| **FERRET** | FERRET - A program to search CMS files for character strings | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FERRET) |
| **FILECALC** | A free-form calculator for use from within Xedit | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FILECALC) |
| **FILEDATE** | FILEDATE | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FILEDATE) |
| **FILELIST** | Improvements to FILELIST, RDRLIST and EXECUTE Version 2.4.9a | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FILELIST) |
| **FILELSND** | Send a DOCUMENT as a FILE, a FILE as a DOCUMENT. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FILELSND) |
| **FILEMGR** | Organizes CMS files into folders, provides hiding options and expiration dates. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FILEMGR) |
| **FILEMOVE** | Move files between VM minidisks. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FILEMOVE) |
| **FILESIZE** | Determine the size of a CMS file | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FILESIZE) |
| **FIXDATE** | A front-end to call DMSPLU with more liberty in date format | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FIXDATE) |
| **FIXZMAN** | CMS program to consolidate a SMAPI zManager NOTEBOOK configuration file | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FIXZMAN) |
| **FLSORT** | Display a SORT window in FILELIST/RDRLIST. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FLSORT) |
| **FMTDISK** | Erase/Format/Scratch disk tracks | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FMTDISK) |
| **FOLLOWUP** | Followup for OfficeVision/VM | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FOLLOWUP) |
| **FORAMENU** | Simple Front End to FORUM/CFORUM files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FORAMENU) |
| **FORATREE** | Show a "tree" of appends in a FORUM type file. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FORATREE) |
| **FPUBLIC** | Identify SFS Files and Directories with PUBLIC Access | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FPUBLIC) |
| **FRENFONT** | OB10, OR10, SR12, GT20 & GT24 FONTS WITH FRENCH ACCENTS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FRENFONT) |
| **FRIDAYRM** | TOTALS reminder mechanism, use in PROFILE EXEC. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FRIDAYRM) |
| **fsiucv** | A character device driver that enables you to perform IUCV functions using open/close/read/write/ioctl as opposed to a network driver (AF_IUCV) | [Github](https://github.com/nealef/fsiucv) |
| **FSX** | A Full Screen Controller for Use with REXX | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FSX) |
| **FTPREXX** | FTP client and socksified tcpclient Pipeline stages, both originally from Steve Hayes | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=FTPREXX) |
| **GD-XEDIT** | Various XEDIT Goodies from Kris Buelens V 1.5 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GD-XEDIT) |
| **GET370AC** | Check all logged on users for the 370ACCOM setting | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GET370AC) |
| **GETBACK** | Recover a wrongly erased file. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GETBACK) |
| **GETFILE** | Remotely-initiated uploading of PC file to VM user | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GETFILE) |
| **GETSTHYI** | GETSTHYI - issue STHYI function code 0 and format response. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GETSTHYI) |
 | [Github](https://github.com/nealef/syslog_vm) |
| **GMLLABEL** | Create address labels by using GML tags | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GMLLABEL) |
| **GOPHER** | A gopher client for CMS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GOPHER) |
| **GREPX** | A text search utility that uses nested expression as arguments. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GREPX) |
| **GUI-APPL** | A pointer to a collection of CMS/GUI applications in REXX. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUI-APPL) |
| **GUIBLD95** | Windows 95 GUI Builder for Writing CMS GUI Applications | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUIBLD95) |
| **GUIBUILD** | GUI Builder for Writing CMS GUI Applications | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUIBUILD) |
| **GUICACHE** | CMS/GUI exec to view at 3990 cache statistics V1.0 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUICACHE) |
| **GUIONE** | Make your own CMS/GUI performance monitor (includes GBOS2) V1.1 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUIONE) |
| **GUISET** | Tailor XEDIT settings via a CMS GUI application | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUISET) |
| **GUISKEL** | A framework to build REXX CMS/GUI applications much easier. V3 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUISKEL) |
| **GUITELL** | A CMS GUI front-end for TELL Version 1.2b | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUITELL) |
| **GUITWO** | Improve GUIONE, the sample CMS/GUI performance monitor in REXX V1.0 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUITWO) |
| **GUIWDOC** | HTML documentation for GUIWIRE V1.2 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUIWDOC) |
| **GUIWIRE** | CMS/GUI application to build other REXX CMS/GUI applications V4.5.1 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=GUIWIRE) |
| **H2S** | H2S - Converts HTML to Script/VS (DCF) for fine printing with AFP or PostScript | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=H2S) |
| **HASHWF** | A General HASH function (S/370 and other systems) | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HASHWF) |
| **HELPDESK** | Database of OV/VM Q&A's for help desk personnel, can add your own Q&A, too. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HELPDESK) |
| **HELP** | Improvements to HELP: help with wildcards, more colors, better RRT V1.5 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HELP) |
| **HELPWIND** | Present help information in a 'window'. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HELPWIND) |
| **HENSLER** | Fran Hensler's z/VM and VSE download page - many different packages | [VM Workshop](https://vmworkshop.org/HENSLER/) |
| **HEXDUMP** | Browse data from any source in hexadecimal. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HEXDUMP) |
| **HISTORY** | The HISTORY command displays the contents of the CMS command history fil | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HISTORY) |
| **HOMUNC** | Platform for a self-aware operating system. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HOMUNC) |
| **HPALIAS** | Formatter for D6 R28 HyperPAV Alias Records | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HPALIAS) |
| **HSX** | HSX - Adds Compressed File Support to any CMS program | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=HSX) |
| **IAMMGR** | IAM Manager - an IAM SAFE front-end | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IAMMGR) |
| **IBMVMGAT** | IBMVMGAT TOOLS documents and TOOLS Catalog | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IBMVMGAT) |
| **IBM zvm_ansible** | Ansible automation for z/VM using SMAPI and the Feilong ecosystem | [GitHub](https://github.com/IBM/zvm_ansible) |
| **IBM zvm_ansible_collection** | Ansible collection for z/VM automation | [GitHub](https://github.com/IBM/zvm_ansible_collection) |
| **ICKGENSA** | Generate ICKDSF to work with SAPL (Stand-alone program loader | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ICKGENSA) |
| **IDLEDISC** | Disconnect VMID if there is no I/O for a specified period. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IDLEDISC) |
| **ILEXITS** | Sample User Exits for INFOLIST PACKAGE | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ILEXITS) |
| **IMAP** | Internet Message Access Protocol server for TCP/IP | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IMAP) |
| **IMDOC** | Imbed an OV/VM document into an XEDIT session. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IMDOC) |
| **INFO** | Action Tables | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=INFO) |
| **INFOLIST** | The CMS File Manager. Replaces FILELIST, RDRLIST, MACLIST | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=INFOLIST) |
| **INHEX** | Encoder for SMTP Submissions to the VM Download Library | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=INHEX) |
| **INSTPROD** | Automated install of IBM products for z/VM including Operations Manager, Backup and Restore Manager, Tape Manager, zSecure, and OMEGAMON XE. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=INSTPROD) |
| **IOS3270** | Runtime files for IOS3270 (Display I/O facility | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IOS3270) |
| **IOS3270** | Runtime files for IOS3270 (Display I/O facility) | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IOS3270) |
| **IOX** | REXX/EXEC2 file I/O utility | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IOX) |
| **IPCSAMP** | Sample programs for CMS distributed queues. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IPCSAMP) |
| **ipgate-v6** | Provides IPv6 gateway configuration, routing, and network management components | [z/VM Community Tools](https://github.com/openmainframeproject/zvm-community-tools/tree/main/ipgate-v6) |
| **IPLER** | IPL a CMS/GCS corresponding to 190/595 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IPLER) |
| **ITEMACTN** | Perform various actions on file 'items'. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ITEMACTN) |
| **ITEMLOOK** | Search 'item' files, OFSLOGfl, NOTEBOOK etc. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ITEMLOOK) |
| **IXFTOCMS** | Convert IXF Exported file from/to VMAS or QMF from/to CMS file. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=IXFTOCMS) |
| **JNOTEPLS** | Tools and new functions for OVVM R2 note editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=JNOTEPLS) |
| **KM** | A CSL interface to the KMx cipher instructions; with Rexx Pipes stages showing their use | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=KM) |
| **LASTCMDX** | LASTCMDS - VM/XA-ESA Display another user's retrieve buffer. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LASTCMDX) |
| **LCLQRY** | Local CP-exits providing queries to display your AUTOLOGGER or ALTUSER st | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LCLQRY) |
| **LEXXASM$** | Assembler parser for the LEXX editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXASM$) |
| **LEXXC$$** | Alternate LEXX C parser | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXC$$) |
| **LEXXCFDA** | LEXX - "Commands From Data Area" facility | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXCFDA) |
| **LEXXCOB$** | LEXX COBOL parser | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXCOB$) |
| **LEXXFOR$** | FORTRAN parser for the LEXX editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXFOR$) |
| **LEXX** | LEXX, The Live Parsing Editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXX) |
| **LEXXPLXX** | LEXXPLXX, LEXX Parsers for PL/I, PL/X, Modula-2 and Pascal | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXPLXX) |
| **LEXXRX$$** | RX$$ - Alternate REXX parser for the LEXX editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXRX$$) |
| **LEXXTEX$** | A LaTeX/TeX Parser for the LEXX Editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LEXXTEX$) |
| **libascii** | Helps you port ASCII-based C applications to the EBCDIC-based z/VM OpenExtensions | [Github](https://github.com/nealef/libascii) |
| **LIBICA** | Crypto library for s390x | [Github](https://github.com/opencryptoki/libica) |
| **LIBRCMS** | VSE/ESA Librarian Server for CMS users | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LIBRCMS) |
| **libzfcphbaapi** | Shared library providing zfcp-specific parts for an implementation of FC-HBA | [Github](https://github.com/ibm-s390-linux/libzfcphbaapi) |
| **LINMON** | MONWRITE Collector | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LINMON) |
| **LISTSG** | A series of FILELIST-like tools V1.8 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LISTSG) |
| **LIVE** | Sample web access to SMAPI functionality | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LIVE) |
| **LNK** | Flexible LINK/ACCESS, cmd, RELEASE/DETACH (and more! | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LNK) |
| **LOGICAL** | Logical Segments for OV/VM and other tools | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LOGICAL) |
| **LOOK4** | Another, small tool to scan files for a char string. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LOOK4) |
| **LOOKALL** | Probably the best XEDIT-based search engine you will find. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LOOKALL) |
| **LOOK** | FAST, INTELLIGENT search of NOTEBOOK/OFSLOGfl/FORUM. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LOOK) |
| **LOWERGAT** | Convert files to lower case with smarts | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LOWERGAT) |
| **LP3820** | Convert AFP (LIST3820) files to personal printers | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LP3820) |
| **LP-PACK** | Inter-related PACKAGEs supported by LP. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LP-PACK) |
| **LPREXX** | Misc. REXX routines from LP. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LPREXX) |
| **LPXEDIT** | Misc. XEDIT macros from LP. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LPXEDIT) |
| **LXCMS** | Linux access to CMS resources | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LXCMS) |
| **LXC** | Run CMS commands from a TCP connected system (V1.4.2) | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LXC) |
| **LXFINDT** | LXFINDT - LEXX FIND Token command | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LXFINDT) |
| **LXJCL$** | MVS JCL parser for the LEXX editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LXJCL$) |
| **LXPRMPT** | LEXX editor PROMPT command | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=LXPRMPT) |
| **MAILDOCS** | Mass MAIL or DELETE of OV/VM documents. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MAILDOCS) |
| **MAILGATE** | Package to enable SMTP gateway functions on a pre-VM/ESA 2.3.0 system. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MAILGATE) |
| **MAILIT** | MAILIT is a general purpose VM e-mail sender program. V3.4.c | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MAILIT) |
| **MAKEDIST** | Creates Distributions Lists by Manager. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MAKEDIST) |
| **MANYSCR** | Split the XEDIT screen into many pieces | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MANYSCR) |
| **MAPALLOC** | Displays the allocation map on a CP-owned volume. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MAPALLOC) |
| **MAPNUCX** | Maps nucleus extensions in other CMS machines. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MAPNUCX) |
| **MDDIR** | Group minidisk files into directories. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MDDIR) |
| **MDSK** | A few Minidisk related tools & DEFINE MDISK aids V0.9 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MDSK) |
| **MENULIST** | Display a Filelist of MENUSYS menu files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MENULIST) |
| **MENUSYS** | XEDIT Screen Management System for PFKey panels. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MENUSYS) |
| **META** | 'META XEDIT' -- Provide access to PF13 thru PF24 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=META) |
| **MEXAMPLE** | Some examples of using the MENUSYS PACKAGE. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MEXAMPLE) |
| **MONCLEAN** | Clean up MONWRITE disk of Monwrite files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MONCLEAN) |
| **MONRIP** | Extract time-range of data from a MONWRITE file. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MONRIP) |
| **MONTH** | Create a calendar display, this month or any month. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MONTH) |
| **MONVIEW** | Tools to look at raw z/VM monitor data captured by Monwrite. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MONVIEW) |
| **MONWATCH** | Feed CP Monitor records to a user-written Pipelines stage | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MONWATCH) |
| **MOUNTPW** | Send user ID, passwords, accounting info to VM/ESA V2 R3.0 NFS server. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MOUNTPW) |
| **MOVESEG** | MOVESEG moves VM/ESA DCSS from spool to disk and back | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MOVESEG) |
| **MPWFL320** | Send user ID, passwords, accounting info to VM/ESA V2 R4.0 NFS server. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MPWFL320) |
| **MSEARCH** | Multiple target, XEDIT based search. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MSEARCH) |
| **MTREXX** | MTREXX - CMS MT ThreadCreate function for REXX | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MTREXX) |
| **MULTISRV** | Multiple protocol server for TCP/IP | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MULTISRV) |
| **MYLOGGER** | Replacement logger for EnterpriseWeb/VM | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MYLOGGER) |
| **MYTEL** | PERSONAL PHONE DIRECTORY SEARCH and UPDATE | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=MYTEL) |
| **N2D** | OVMLP macros and other OV/VM add-on goodies. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=N2D) |
| **N3820** | Neat Printing on 3820 (For Plain Text & Listing | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=N3820) |
| **NAM2PROF** | Convert CMS NAMES file to OV/VM file(s). | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NAM2PROF) |
| **NAMECHEK** | Verify the Contents of a CMS NAMES File Against Callup | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NAMECHEK) |
| **NBK** | Work Group Notes | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NBK) |
| **NETDPIPE** | Pipe stage to handle NETDATA stream; Pipeline SENDFILE/RECEIVE | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NETDPIPE) |
| **NETLIST** | A FILELIST for RSCS Network Files and Links Version 2.9 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NETLIST) |
| **NONAMES** | Avoid NAMEFIND lookup for SFS administrative commands | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NONAMES) |
| **nord** | a minimalist Linux system that can run on s390x | [Github](https://github.com/trothtech/nord) |
| **NOREAD** | Prevent VM READ Situation | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NOREAD) |
| **NOTEBOOK** | A Notebook Management Facility | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NOTEBOOK) |
| **NOTENAME** | Xedit Macro to Add Names and Security Class to CMS Notes | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NOTENAME) |
| **NOTEXTND** | NOTEXTND - Supporting package to the FILELSND PACKAGE. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NOTEXTND) |
| **NS_VM** | Capacity Estimator for VM/ESA's IBM Network Station Support | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NS_VM) |
| **NUCXLIST** | NUCXMAP Editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NUCXLIST) |
| **NUM2TEXT** | Function to format numbers in thousands and written amount | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=NUM2TEXT) |
| **OBFUSCAT** | Prevent direct links by randomly changing file and HTML link names in SFS. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=OBFUSCAT) |
| **OFSCURSX** | Use OV 1.4 OFSCURSX exit to call web browser when URL is selected | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=OFSCURSX) |
| **OFSMIME** | Mime add-on for OfficeVision/VM. Sends and receives attachments. V2.1.1 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=OFSMIME) |
| **OFSNAMES** | Making OV/VM nicknames & distribution lists available to CMS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=OFSNAMES) |
| **ONLINE** | Receive or Copy files to any disk with renaming of old files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ONLINE) |
| **ON** | Shows who's on and who's not and sometimes where | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ON) |
| **OpenAFS** | A distributed filesystem product, pioneered at Carnegie Mellon University  | [Sine Nomine Associates](https://download.sinenomine.net/openafs/) |
| **openssl** | A robust, full-featured Toolkit for TLS (formerly SSL), Datagram TLS (DTLS), and QUIC protocols| [Github](https://github.com/nealef/openssl) |
| **OTTOSCR** | Screen scroller for Fullscreen CMS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=OTTOSCR) |
| **OVASST** | Consolidated end user tailoring of OfficeVision/VM functions. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=OVASST) |
| **OVMJAVA** | Call JDK tools from the CMS command line, without using the VM Shell | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=OVMJAVA) |
| **OVTOCMS** | OfficeVision/VM to CMS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=OVTOCMS) |
| **PAGES** | Count pages in LIST3820 or LIST38PP file | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PAGES) |
| **PCALLC** | Support for calling C/370 from VS/Pascal | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PCALLC) |
| **PCR** | The PCR utility enables CMS commands, subcommands, and Rexx functions/subroutines to be written in PL/I. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PCR) |
| **PEEKMENU** | Super Menu for PEEK. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PEEKMENU) |
| **PEEKXTND** | PEEKXTND - Supporting package to the FILELSND PACKAGE. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PEEKXTND) |
| **PF10PF11** | PF10 and PF11 XEDIT macros allow to move from left to right, based on the position of the cursor in the delimited area defined by the SET Verify XEDIT command. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PF10PF11) |
| **PHONEM** | Telephone Message | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PHONEM) |
| **PICDIR** | The Picture Directory | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PICDIR) |
| **PICKPIPE** | Choose between default VM, Marist, and test runtime versions of Pipelines | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PICKPIPE) |
| **PIGS** | An exec that can be used to determine who is using too much spool space. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIGS) |
| **PIPEDDR** | Dump/Restore a disk to a file, ftp server, or over TCP/IP to a remote system. Supports compression, digest verification, and secure connections. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPEDDR) |
| **PIPEDOCS** | VERY FAST/FUZZY PIPELINES SEARCH OF THE OV/VM DataBase. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPEDOCS) |
| **PIPEFILE** | Modern Pipelines file I/O using DMSREAD/DMSWRITE; SFS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPEFILE) |
| **PIPEFIND** | VERY FAST/FUZZY PIPELINES SEARCH OF FILES. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPEFIND) |
| **PIPEFUZZ** | PIPELINES FUZZY SEARCH FILTER. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPEFUZZ) |
| **PIPELIST** | Build a dynamic FileList using PIPELINES. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPELIST) |
| **PIPESCAN** | PIPE-based SCANFILE alternative. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPESCAN) |
| **PIPESERV** | A Pipeline Server. A driver for service machines. Version 1.2.4. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPESERV) |
| **PIPXEDIT** | Use Pipeline stages to manipulate lines in XEDIT session. Version 1.1.1. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PIPXEDIT) |
| **PLIMOL** | PL/I Merge Object List | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PLIMOL) |
| **PMWTOXXX** | Convert PW/PMW data to Bookmaster schedule or calendar | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PMWTOXXX) |
| **PNM** | Personal Net Machine | [z/VM Downloads](https://www.ibm.com)
| **POSIX Pipelines** | Works like CMS Pipelines | [Github](https://github.com/trothtech/xfl) |
| **PRFCOPY** | The most complete "cut&paste" for XEDIT V4.2.f | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFCOPY) |
| **PRFGUI** | A CMSGUI interface for VMPRF Trend & Summary files Version 1.13 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFGUI) |
| **PRFIT** | Wrapper to invoke PERFKIT BATCH | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFIT) |
| **PRFRUN** | A server to automate VMPRF & MONWRITE. Also remote cmds V3.3.a | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFRUN) |
| **PRFVIEW** | Have a decent view on VMPRF listings: we use CMSGUI Version 2.2 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PRFVIEW) |
| **PRTAPA** | EASY VM PRINTS on 3820/3812 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PRTAPA) |
| **PS2PSEG** | Converts EPS to PSEG3820, PSEG4250 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PS2PSEG) |
| **PTKGUI** | A CMSGUI interface for PTK Summary files Version 1.0.a | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PTKGUI) |
| **PTKTOOLS** | PTKTOOLS contains some simple PERFKIT related execs + ctl files V1.2 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PTKTOOLS) |
| **PTKUTIL** | No description provided | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PTKUTIL) |
| **PTKVIEW** | Have a decent view on VMPTK listings: we use CMSGUI Version 1.0.a | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PTKVIEW) |
| **PUTCMS** | Invoke CMS command on lines extracted from an Xedit session | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PUTCMS) |
| **PUTFILES** | PUTFILES is the converse of GETFILES Pipelines stage V2.2 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PUTFILES) |
| **PUTVER** | PUT macro for XEDIT that respects VERIFY setting. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PUTVER) |
| **PVMBATCH** | PVMBATCH - How to Run PVM Sessions like Batch Jobs | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PVMBATCH) |
| **PWCHECK** | HTTP Basic Authentication Exit for ISFC Collection | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=PWCHECK) |
| **QBRAPA** | Browse text part of a APA document (3820/4250/38PP), CMS/TSO | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QBRAPA) |
| **qclib** | a C API for extraction of system information for Linux on z Systems | [Github](https://github.com/ibm-s390-linux/qclib) |
| **QDASD** | Display information about DASD devices in table form. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QDASD) |
| **QDEVS** | QDEVS displays devices owned by the system or a virtual machine. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QDEVS) |
| **QDIR** | Make your interactions with DIRMAINT much quicker and easier. Instantly review a USER/IDENTITY/PROFILE by displaying it on screen. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QDIR) |
| **QDISK** | A quadri-modal repackaging of XASTOR, QDISK, DLIST and QDEVS V1.5.2 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QDISK) |
| **QID** | CSO interface to CallUp phone directories | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QID) |
| **QLINKS** | Displays links to any user's minidisk. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QLINKS) |
| **QMDC** | Get IO counts and MDC hit% per minidisk per user. Version 1.0.a | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QMDC) |
| **QMVSP** | Query the Status of an MVS-attached JES2 Printer | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QMVSP) |
| **QN** | Selective QUERY NAMES | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QN) |
| **QRYWWPNS** | Find out which FCP & WWPNs can reach a given LUN Version 1.0 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QRYWWPNS) |
| **Q_SMAPI** | SMAPI - Query Dir. Manager Level & Query API Func. Level API clients | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=Q_SMAPI) |
| **QSSIMEM** | SMAPI routine to return SSI Member of an active virtual machine | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QSSIMEM) |
| **QUERYINF** | Query and/or change your INFORM requests for TOOLS. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=QUERYINF) |
| **R4MON** | Report on VM66095 EDEV FCP chpid and device records. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=R4MON) |
| **RACHELP** | Create normal CMS Help files for RACF from RACF help facility files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RACHELP) |
| **RACK** | Display a selection menu for processing acknowledgments | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RACK) |
| **RC** | RexxComment Xedit macro | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RC) |
| **RDRLAPP** | Intelligent APPEND & REPLACE from RDRLIST. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RDRLAPP) |
| **RDRLMENU** | Super Menu for RDRLIST. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RDRLMENU) |
| **RDRLOGR** | Logs Reader files and notes into selected files on disk. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RDRLOGR) |
| **RECOVER** | RECOVER - recover files from CMS minidisks | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RECOVER) |
| **RELODOM** | Displays the relocation domains in a member of an SSI. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RELODOM) |
| **REMEMBER** | REMEMBER an XEDIT session, for recreating later | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REMEMBER) |
| **RENSSI** | Rename a member of an SSI | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RENSSI) |
| **REPLACE** | Replace files while preserving previous versions. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REPLACE) |
| **REPORTER** | Soft Splitting and Electronic Mailing of Reports. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REPORTER) |
| **REPORTSS** | Starter Set package for the REPORTER PACKAGE. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REPORTSS) |
| **REQUEST** | Request a package from another user or fulfill such requests | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REQUEST) |
| **RETBUF** | Fullscreen CP retrieve buffer selection panel. Version 2.1.2. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RETBUF) |
| **REXXCOND** | Pipeline filter based on Rexx expression | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REXXCOND) |
| **REXXCSL** | Call CSL routine from Rexx program | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REXXCSL) |
| **REXXEDIT** | Execute records as REXX directly from XEDIT. Not Y2K sensitive. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REXXEDIT) |
| **REXXG** | EXECs and XEDIT macros for the REXX programmer Version 1.1 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REXXG) |
| **REXXIUCV** | IUCV interface for REXX | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=REXXIUCV) |
| **RLPF** | The ULTIMATE in RACF usability tools | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RLPF) |
| **RRTGEN** | Generate Rail Road Track syntax diagrams from user written SYNTAX files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RRTGEN) |
| **RRT** | Make 'railroad track' syntax diagrams readable | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RRT) |
| **RSCSMDSK** | RSCS Minidisk Transfer Utility. Version 1.1.2. Y2K ready. Independent of tools. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RSCSMDSK) |
| **RSCSOP** | RSCSOP is a service machine to provide dynamic AUTH control over printers. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RSCSOP) |
| **RSCSTAPE** | RSCS Tape Transfer Utility. Version 1.1.2. Y2K ready. Independent of tools. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RSCSTAPE) |
| **RSF** | Send a FILE/PACKAGE/NOTE to all in REQUESTS file. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RSF) |
| **RSKFIX** | Reusable Server Kernel (RSK) fix pack | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RSKFIX) |
| **RSK-GA** | RSK Extras (GA level | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RSK-GA) |
| **RSK-GA** | RSK Extras (GA level) | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RSK-GA) |
| **RSKPROB** | Problem Tracking Tool for EnterpriseWeb/VM | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RSKPROB) |
| **RUNREXX** | A framework to develop crossplatform Rexx programs using the eclipse framework | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RUNREXX) |
| **RXDASD** | DASD I/O as REXX a function | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RXDASD) |
| **RXDISP** | CMS REXX display utility | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RXDISP) |
| **RXFLOW** | REXX function to reflow/justify text or to separate sentences. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#namesearch=RXFLOW) |
| **RXMODE** | Rexx Mode Function | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RXMODE) |
| **RXSERVER** | A kernel to build REXX WAKEUP servers, such as VMUTIL. V6.7 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RXSERVER) |
| **RXSORT** | A Sort function for REXX | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RXSORT) |
| **RXTAPE** | API to issue commands to a tape device | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=RXTAPE) |
| **SCIF** | Easier "talking" to SCIFfed users (avoid the CP SEND command) V1.4 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SCIF) |
| **SCKSMAP1** | No description provided | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SCKSMAP1) |
| **SCKSMAP2** | No description provided | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SCKSMAP2) |
| **SCKSMAPI** | Socket access to SMAPI functions | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SCKSMAPI) |
| **SCKXPIPE** | Socket access to XPIPES functions | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SCKXPIPE) |
| **SCRUSCRD** | XEDIT Macros to Scroll Up and Down by Cursor position | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SCRUSCRD) |
| **SDOENA54** | Enabling Aid files for z/VM 5.4.0 SDO configuration. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SDOENA54) |
| **SEARCH** | Search Engine for VM-Hosted Web Sites | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SEARCH) |
| **SEEFILE** | Point to a filename and VIEW, PRINT, SEND etc. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SEEFILE) |
| **SEE** | Like the ALL macro but see the item, not just target lines. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SEE) |
| **SELFLGR** | Relocate a connected user to another SSI member | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SELFLGR) |
| **SELMACS** | Various macros controlling the SELECT levels in XEDIT | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SELMACS) |
| **SENDMAIL** | Send a FILE as a DOCUMENT. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SENDMAIL) |
| **SENDXTND** | SENDXTND - Extension to the FILELSND PACKAGE | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SENDXTND) |
| **SERVEPDF** | View a PDF file from the CMS session in the web browser | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SERVEPDF) |
| **SESTOOLS** | SESTOOLS has tools to make working with VM/SES easier V1.3 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SESTOOLS) |
| **SETDATE** | SETDATE EXEC - Set the date of last update on CMS or SFS files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SETDATE) |
| **SETVMDBK** | Dynamically change user options in VMDBK (eg MAINTCCW) V1.3 | [z/VM/downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SETVMDBK) |
| **SETVMDBK** | Dynamically change user options in VMDBK (eg MAINTCCW) V1.3 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SETVMDBK) |
| **SFCOUNTR** | SFCOUNTR makes a list of users with more than a requested number of spool files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SFCOUNTR) |
| **SFLIST** | z/VM tool to manipulate (view, receive, purge, transfer) SPOOL files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SFLIST) |
| **SFL** | Super Front end to fileList. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SFL) |
| **SFSGRAPH** | No description provided | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SFSGRAPH) |
| **SFSKTOOL** | Various tools related to SFS management. V1.0 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SFSKTOOL) |
| **SFSTAR** | Archive (zip up) SFS directory tree into file/pipeline stream | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SFSTAR) |
| **SFSTOOLS** | Shared File System Tools | [z/VM Downloads](https://www.z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SFSTOOLS) |
| **SFSULIST** | SFSUserList lets you handle SFS users in a FILELIST like way V1.13 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SFSULIST) |
| **SG245148** | Redbook "VM/ESA Network Computing with Java and NetRexx" sample programs | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SG245148) |
| **SG245164** | Redbook "Exploiting Recent CMS Function: A User's Guide to CMS Application Multitasking" sample programs. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SG245164) |
| **SG245164** | Redbook sample programs | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SG245164) |
| **SHADLIST** | Build a List of TOOLSRUN Shadows from QUERY DISK Requests | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SHADLIST) |
| **SHAREDQS** | Shared CMS Queues over DCSS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SHAREDQS) |
| **SHOWDCF** | SHOWDCF to compose Script source on screen in CUA form | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SHOWDCF) |
| **SHOWGML** | SHOWGML to display GML/SGML source file on screen in CUA form | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SHOWGML) |
| **SHUTTRAP** | CMS program to detect and react to CP SHUTDOWN signals | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SHUTTRAP) |
| **SMAPIREX** | Rexx routine to simplify the invocation of smapi | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SMAPIREX) |
| **SMARTX** | An XEDIT-based front-end for RTM/ESA and VM/RTM (known as SMART) V6.3.f | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SMARTX) |
| **smc-tools** | Utilities for use with AF_SMC sockets. | [Github](https://github.com/ibm-s390-linux/smc-tools) |
| **SMOF** | SMOF - append files to notebooks | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SMOF) |
| **SMTMET** | Extract SMT Metrics from Domain 0, Record 2. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SMTMET) |
| **SPFPACK** | SPFPACK determines which spool files have data on a particular spool pack. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPFPACK) |
| **SPITABCD** | Spits out permutations of command syntax for broadest coverage | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPITABCD) |
| **SPLIT** | Split any file that can be split ( example OFSLOGfl ). | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPLIT) |
| **SPOOLAID** | Full-screen browser for spool file internals | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLAID) |
| **SPOOLCHN** | System Programmer/System Operator Extended Spool Query Commands | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLCHN) |
| **SPOOLKIT** | Show SPOOL utilization details and allow viewing/manipulating SPOOL files (replaces SFLIST package | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLKIT) |
| **SPOOLKIT** | Show SPOOL utilization details and allow viewing/manipulating SPOOL files (replaces SFLIST package) | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLKIT) |
| **SPOOLPIG** | Display the largest spool files and users of the spool on a system. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLPIG) |
| **SPOOLUSE** | Smart query of RDR, PRT, and PUN files | [z/VM Downloads](https://z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPOOLUSE) |
| **SPXPINTV** | SPXTAPE Progress Report Interval Modifications | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SPXPINTV) |
| **SQLITE** | SQLite is a C-language library that implements a small, self-contained, high-reliability, full-featured, SQL database engine, ported to CMS. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SQLITE) |
| **SRCHDATA** | Process the $SEARCH$ OFSDATA file produced by OV/VM. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SRCHDATA) |
| **SRCHDOCS** | Search OV/VM Database, OFSLOGfl, FORUM etc. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SRCHDOCS) |
| **SRCHLIST** | An XEDIT macro that can search through files from FILELIST or MACLIST | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SRCHLIST) |
| **SRMTIDLE** | Sets value of CP dispatcher "test-idle" timer | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SRMTIDLE) |
| **SSIQSERV** | Issue Q CPSERVICE on all SSI members and show differences in the active fixes. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SSIQSERV) |
| **STACKTYP** | STACKTYP - divert TYPLIN output to stack or discard | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=STACKTYP) |
| **STORACC** | Compute amount of storage used by filemode accesses | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=STORACC) |
| **STORSUMM** | Give summary of how allocated CMS storage is being used | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=STORSUMM) |
| **SUBMIT** | SUBMIT Command to send a job to batch processor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SUBMIT) |
| **SUPERSAY** | Issue multiline message, color selectable, with/without editor | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SUPERSAY) |
| **SUPPRESS** | VM read in non-display mode, like asking for password. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SUPPRESS) |
| **SWITCH** | SWITCH mode | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SWITCH) |
| **SYNPEEK** | Syntax Diagram Peeker | [z/VM Downloads](https://www.ibm.com/support/pages/zmm/download/packages/#search=SYNPEEK) |
| **SYSLOGD** | SYSLOGD daemon for CMS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=SYSLOGD) |
| **syslog_vm** | A simplistic syslog daemon which accepts UDP/TCP connections plus a shared library containing the APIs ``openlog(), syslog(), closelog()`` and ``setlogmask()``
| **TAB2GC** | Draw charts entirely on CMS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TAB2GC) |
| **TABCRE** | EASY SCRIPT/GML/BOOKMASTER TABLES (WYSIWYG | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TABCRE) |
| **TAB** | TAB -- Add Thumb Tabs to BookMaster | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TAB) |
| **TABULATE** | Pipelines stage- tabulate columns of data | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TABULATE) |
| **TALK2** | Talk to another VM user. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TALK2) |
| **TBROWSE** | Display CMS tabular Files with Sort, Select and Statistics. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TBROWSE) |
| **TCATALOG** | YC2VM Program Update & Tools Catalog | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TCATALOG) |
| **TCVM1** | Advanced REXX Telecourse (an HTML selfstudy course) V1.3 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TCVM1) |
| **TCVM2** | CMS Pipelines Telecourse (an HTML selfstudy course) V1.3 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TCVM2) |
| **TEDIT** | Text and Table editor for Script Report Table Schedule Package | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TEDIT) |
| **tela** | framework for running tests that are controlled by a Makefile. | [Github](https://github.com/ibm-s390-linux/tela) |
| **TELELIST** | Generate Distribution Lists from CALLUP directories. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TELELIST) |
| **TELESITE** | Make access to a CALLUP directory easier. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TELESITE) |
| **TELETREE** | Climb the Telephone Directory (CALLUP) 'tree'. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TELETREE) |
| **Terraform** | Terraform integration with the z/VM SDK/Feilong ecosystem | [GitHub](https://github.com/mfcloud/terraform-provider-zvmsdk) |
| **TEXTFLOW** | Pipeline stage to flow or justify text into paragraphs | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TEXTFLOW) |
| **THEX** | Type or Print files in HEX | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=THEX) |
| **TIMEBOMB** | Set, snooze or cancel the CP timebomb (diagnose 288) feature from CMS. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TIMEBOMB) |
| **TIMESERV** | VM/TimeServ - An SNTP Version 4 Time Server for VM/ESA and z/VM | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TIMESERV) |
| **TLD** | TCP/IP line driver for CMS distributed queues. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TLD) |
| **TMSTMP** | TMSTMP - A C/370 and PL/I execution profiler | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TMSTMP) |
| **TODALLOW** | Require Operator reply to continue IPL if current TOD is outside allowed range. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TODALLOW) |
| **TOG** | A full function multi-session 'TOGGLER' | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOG) |
| **TOOLHELP** | No description provided | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLHELP) |
| **TOOLNOTE** | User Interface to TOOLSRUN via NOTE or PROFS | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLNOTE) |
| **TOOLPRT** | A facility to print the content of a catalog of tools. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLPRT) |
| **TOOLSDOC** | Documentation for TOOLS and TOOLSRUN | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLSDOC) |
| **TOOLSPDF** | No description provided | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLSPDF) |
| **TOOLSRUN** | TOOLSRUN Distributed Master/Shadow Disks and Conference Manager | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLSRUN) |
| **TOOLS** | User interface program for managing and updating TOOLSRUN maintained disks. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOOLS) |
| **TOVMWEB** | Send package to VM DownLoad Library, including NON-IBM. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TOVMWEB) |
| **TRACEXEC** | An interactive debugger for REXX execs; a tool for analyzing EXEC applications. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TRACEXEC) |
| **TRACK** | tool for tracking virtual machine operation | [Velocity Software](https://vmtrack.velocitysoftware.com/trackmod.vmarc) |
| **TRF2TCPD** | Convert VM TCP/IP Packet Trace to Linux tcpdump format | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TRF2TCPD) |
| **TRFILTER** | No description provided | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TRFILTER) |
| **TRSOURCE** | TOOLSRUN Package, additional source files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TRSOURCE) |
| **TSLAMON** | REXX to exploit CP monitor data in real time eg user %CPU, %WAIT V1.1 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TSLAMON) |
| **TT** | XEDIT prefix macro which aligns/flows text for paragraphs, etc. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TT) |
| **TZDATES** | Generation of the TIMEZONE_BOUNDARY statements to use in the SYSTEM CONFIG. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=TZDATES) |
| **UFT File Transfer** | works like NJE but no NJE needed | [Github](https://github.com/trothtech/uft) |
| **USAGE** | Check A-disk usage and warn if exceeds stated percent | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=USAGE) |
| **VDISKRPT** | No description provided | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VDISKRPT) |
| **VIEW4GDF** | ADMGDF/CGM Editor - Support for ADMPRINT/ADMIMG files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VIEW4GDF) |
| **VIEWER** | View most types of file. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VIEWER) |
| **VIEWGDF** | VIEW, MERGE, PLOT ADMGDF files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VIEWGDF) |
| **VIFWWW** | Web commander for z/VM System Administration Facility V2.10 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VIFWWW) |
| **VIR2REAL** | Compute the Virtual to Real storage (memory) ratio of running users in a VM LPAR. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VIR2REAL) |
| **VM220PRF** | VM/ESA Version 2 Release 2.0 Performance Report | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VM220PRF) |
| **VM230PRF** | VM/ESA Version 2 Release 3.0 Performance Report | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VM230PRF) |
| **VM240PRF** | VM/ESA Version 2 Release 4.0 Performance Report | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VM240PRF) |
| **VMADMANY** | VMADMIN client anywhere | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMADMANY) |
| **VMESABIT** | VM/ESA Bitmaps for OS/2 Background/Display | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMESABIT) |
| **VMHP** | Tools we use to manage the VM home page system | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMHP) |
| **VMLINK** | VMLINK - Link and Access tool for CMS 10 and below. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMLINK) |
| **VMLOGS** | Create an automatic managed repository for Consoles and data files. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMLOGS) |
| **VMMENU** | Easy selection menu presentation for CMS V2.0 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMMENU) |
| **VMREVIEW** | EXEC to check the major changes to a z/VM system if migrating to z/VM 6.4.0. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMREVIEW) |
| **VMSERVE** | A Disconnected Virtual Machine manager for VM that handles reader files, messages and time-of-day events. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMSERVE) |
| **VMWEBCD** | Redbook SG24-5347 "Web-Enabling VM resources" sample programs | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=VMWEBCD) |
| **WAKERDR** | WAKERDR a RDR Scanner, Wakeup monitor, VM Server thru RDR/RSCS. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WAKERDR) |
| **WHO-IS** | Frontend EXEC for NAMEFIND and PROFS name files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WHO-IS) |
| **WINMAKER** | FULLSCREEN MENU/TOOLBAR/SCROLL, VERSION 3. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WINMAKER) |
| **WITHHOLD** | Calculate Federal/state Withholding Allowances | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WITHHOLD) |
| **WKPITCH** | 1997 VM Workshop Presentations from Brian Wade | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WKPITCH) |
| **WORDEVAL** | Pipeline stage to evaluate Rexx expr with variables fm input | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WORDEVAL) |
| **WORDMACS** | XEDIT macros that locate, change, or count words | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WORDMACS) |
| **WORFAUTH** | WORF SFS ESM rule database updater | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WORFAUTH) |
| **WORF** | Simple Shared File System (SFS) external security manager (ESM | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=WORF) |
| **XASTOR** | A multi-functioned, programmable, full-screen storage display | [z/VM Downloads](https://README.md](https://www.ibm.com/support/pages/zvm/download/packages/#search=XASTOR) |
| **XBROWSE** | XBROWSE is a compiled REXX replacement for PEEK and BROWSE (in module form | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XBROWSE) |
| **XCOL** | Xedit Column Editing for VM/ESA | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XCOL) |
| **XFER2** | Transfer a file from your RDRLIST. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XFER2) |
| **XFILE** | Displays files being XEDITed by other users. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XFILE) |
| **XGRAPHIC** | Safe character translate graphics for BookMaster | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XGRAPHIC) |
| **XLISTF** | Listfile for CMS in CUA mode, Give TOOLS description. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XLISTF) |
| **XMENUVM** | A really cool CMS user interface! | [z/VM Downloads](https://www.ibm.com/search=...???) |
| **XMITMSGX** | works like APPLMSG and XMITMSG but for Unix/Linux | [Github](https://github.com/trothtech/xmm) |
| **XRECALL** | Recall/execute previous XEDIT commands in a window | [z/VM Downloads](https://www.ibm.com/support/pages/zmdownload/packages/#search=XRECALL) |
| **XREC** | Receive Current Note up to Cursored Line | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XREC) |
| **XRL** | An X-Windows view of CMS Reader List | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XRL) |
| **XSF** | XEDIT files that reside in unaccessed SFS directories. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XSF) |
| **X_SMAPI** | SMAPI - Image_Disk_Delete_DM & Image_Volume_Space_Remove_DM API clients | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=X_SMAPI) |
| **XTBL** | XEDIT table files | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XTBL) |
| **XTREE** | To display Package tree hierarchy forward and backward | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XTREE) |
| **XVIEW** | An expert File viewer, Script, Package, Packlib Members. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XVIEW) |
| **XX** | Frontend for XEDIT, provides windows. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=XX) |
| **YR2000VM** | Technical Description of VM/ESA's Year 2000 Support (updated Sept. 1999 | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=YR2000VM) |
| **YVETTE** | Yvette - provide multiple sessions to DIALed 3270s. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=YVETTE) |
| **zvm-ssh-extension** | used by VSCode to access and modify files residing on CMS | [Github](https://github.com/nealef/zvm-ssh-extension) |
| **ZXCATIVP** | Preparation script for the Installation Verification Program for xCAT and OpenStack on z/VM. | [z/VM Downloads](https://www.ibm.com/support/pages/zvm/download/packages/#search=ZXCATIVP) |

## Other Community Tools and Projects

| Name | Description | Source | URL |
|---|---|---|---|
| Terraform Provider for z/VM | Terraform integration with the z/VM SDK/Feilong ecosystem | GitHub | https://github.com/mfcloud/terraform-provider-zvmsdk |
| zPXE | PXE-like network boot functionality for z/VM guests | GitHub | https://github.com/beaker-project/zpxe |
| z/VM REXX language support | REXX syntax highlighting | Open Mainframe Project | https://github.com/openmainframeproject/atompkg-language-zvm-rexx |
| z/VM assembler support | Assembler syntax highlighting | Open Mainframe Project | https://github.com/openmainframeproject/atompkg-languages-zvm |
| CMS NAMES support | CMS NAMES syntax highlighting | Open Mainframe Project | https://github.com/openmainframeproject/atompkg-language-zvm-names |
| SCRIPT/BookMaster support | GML syntax highlighting | Open Mainframe Project | https://github.com/openmainframeproject/atompkg-language-zvm-gml |

## Source Notes

- IBM package data: [IBM z/VM Download Packages](https://www.ibm.com/support/pages/zvm/download/packages/).
- Community/project data: [Open Mainframe Project z/VM Community Tools README](https://github.com/openmainframeproject/zvm-community-tools#other-sources-of-community-tools).
- The README describes the IBM examples as representative rather than exhaustive; the IBM section above is populated from the supplied complete package-page HTML.
- A package being listed in IBM's download library does not by itself establish that it is open source. Check each package's license and source availability.
