![z/VM Community Tools Logo](https://raw.githubusercontent.com/openmainframeproject/artwork/5b27f85f886da75ddf53511eb5289c53c972415c/projects/zvm-community-tools/horizontal/color/zvm-community-tools-horizontal-color.svg)

# z/VM Community Tools

z/VM Community Tools

## Install

Each subdirectory has its own install process:  
- ``execs/`` - Download the ``https://github.com/openmainframeproject/zvm-community-tools/blob/main/execs/zvmtools.vmarc`` file and copy it to z/VM in binary, and unpack it.
- ``dmscmd/`` - Follow the instructions here: https://github.com/openmainframeproject/zvm-community-tools/tree/main/dmscmd#building-dmscmd 
- ``zlma`` - Use the ``instzlma`` bash script 
- ``ztrust/`` - Follow the instructions here: https://github.com/openmainframeproject/zvm-community-tools/tree/main/ztrust

## Build

Each subdirectory has its own build process, if any:  
- ``execs`` - Because REXX EXECs are interpreted, there is no build process necessary.

- ``zlma`` - There is an install script ``instzlma`` that will be described in detail...

## Discussion

You can connect with the community in a variety of ways...

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
- [8. Functional Categories](#8-functional-categories)
- [9. Catalog Metadata and Classification](#9-catalog-metadata-and-classification)

---

## 1. Open Mainframe Project

### z/VM Community Tools

- **Repository:** https://github.com/openmainframeproject/zvm-community-tools
- **Website:** https://www.zvmcommunitytools.org/

The Open Mainframe Project's z/VM Community Tools repository is a collection of community-maintained tools and utilities for z/VM.

Areas covered include:

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

Examples of packages and utilities include:

| Tool | Description |
|---|---|
| DISASM | z/Architecture instruction disassembler |
| SPOOLKIT | Inspect and manipulate spool files |
| CPUMF | CPU Measurement Facility reporting |
| CP3KVMXT | Generate zPCR/zCP3000 input from monitor data |
| RELODOM | Display SSI relocation domains |
| TZDATES | Generate timezone configuration statements |
| BFSLIST | Browse BFS filespaces |
| DRM | XEDIT interface for managing CP directory |
| PIPEDDR | Disk dump and restore, including remote transfer |
| QDIR | Directory and DIRMAINT inspection utilities |
| DMT-XX | Directory migration utilities |
| LINMON | MONWRITE collector |
| FCXTREND | Prune Performance Toolkit FCXTREND files |
| CHKAPARS | Analyze z/VM APAR and service information |
| MONVIEW | Examine raw MONWRITE data |
| MONCLEAN | Clean up MONWRITE files |
| LISTSG | FILELIST-like utilities |
| TAB2GC | Generate charts within CMS |
| SQLITE | SQLite-related CMS package |

This is a representative list, not a complete package inventory. Consult the IBM package index for the latest listings.

**Licensing note:** The IBM download library is a distribution repository, not a guarantee that every package is open source. Check the licensing terms and source availability of individual packages.

---

## 3. Independent GitHub Projects

Many useful z/VM tools are maintained independently of the Open Mainframe Project and IBM download library.

### Systems Management and Provisioning

#### Feilong

- **Repository:** https://github.com/openmainframeproject/feilong
- **Documentation:** https://cloudlib4zvm.readthedocs.io/
- **License:** Apache 2.0

An open-source REST API and SDK for provisioning and managing z/VM guests, images, networks, and volumes.

Feilong integrates with cloud management platforms and infrastructure automation tools.

#### ZLMA – z/VM and Linux Modern Administration

- **Repository:** https://github.com/mike99mac/zlma

Browser-oriented administration of Linux servers running under z/VM.

Provides a modern interface for Linux guest administration and management.

#### IBM zvm_ansible

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

#### Terraform Provider for z/VM

- **Repository:** https://github.com/mfcloud/terraform-provider-zvmsdk

Terraform integration with the z/VM SDK/Feilong ecosystem.

Provides an infrastructure-as-code approach to managing z/VM resources.

### CMS, Networking, and File Utilities

| Project | Description | Repository |
|---|---|---|
| VMLINK | CMS file and software linking automation | https://github.com/trothtech/vmlink |
| ZNETBOOT | Network booting tools | https://github.com/trothr/znetboot |
| zPXE | PXE-like network boot functionality for z/VM guests | https://github.com/beaker-project/zpxe |
| CMS Make | Make-like build automation for CMS | https://github.com/trothr/cmsmake |
| CMS TAR | TAR archive utility for CMS | https://github.com/trothr/cmstar |
| XMM | XMIT message management utility | https://github.com/trothtech/xmm |

These projects are particularly interesting because they address the traditional CMS environment rather than just Linux guests.

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

### Topics of Interest

Examples of subjects covered in recent presentations include:

| Topic | Area |
|---|---|
| CMS Pipelines Basics | CMS automation |
| Introduction to XEDIT | Editor extensions and productivity |
| Setting up z/VM Performance Monitoring | Performance monitoring |
| Operational Monitoring and Automation of Multiple z/VM LPARs | Systems management |
| Git for VMers | Source control |
| ZTRUST | Security and trust |
| VFILE | CMS file management |
| Python, a GUI, OpenSSH, and an SSH Server for CMS | CMS development |
| Express Linux Automation and Networking | Ansible and networking |
| IBM z/VM Express System Install | Installation automation |

The presentation archives are especially valuable for discovering software that was demonstrated but never formally published in a central repository.

Presentations may be copyrighted by their authors or organizations; reference and link to them rather than assuming they can be redistributed.

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

## 8. Functional Categories

For a comprehensive catalog, software should be organized by function rather than by its original distribution location.

| Category | Examples |
|---|---|
| CP and Systems Management | CP utilities, SSI, relocation domains |
| CMS Utilities | EXECs, REXX, XEDIT macros |
| Directory Management | DIRMAINT, RACF, directory migration |
| Performance and Monitoring | MONWRITE, CPUMF, performance reporting |
| Networking | TCP/IP, VMLINK, ZNETBOOT, zPXE |
| Storage and Filesystems | BFS, SFS, CMSFS, disk backup |
| Automation and Provisioning | Feilong, Ansible, Terraform |
| Security | ZTRUST, signing, encryption, access management |
| Development Tools | CMS Make, CMS TAR, XMM, Git |
| Linux Guest Utilities | s390-tools, hyptop, cmsfs-fuse |
| Installation and Maintenance | Installation, service, APAR, and migration tools |

---

## 9. Catalog Metadata and Classification

Each catalog entry should include as much of the following information as possible:

| Field | Description |
|---|---|
| Name | Tool or project name |
| Description | What the tool does |
| Category | Functional classification |
| Repository | Source-code location |
| Download | Binary or package download location |
| Author / Maintainer | Original developer or current maintainer |
| License | Actual software license |
| Source Available | Whether source code is available |
| Open Source | Whether it meets an open-source license definition |
| Execution Environment | CP, CMS, Linux guest, or external management server |
| Supported Releases | Supported z/VM versions |
| Last Updated | Last known release or source update |
| Documentation | Installation and usage instructions |
| Presentations | Relevant VM Workshop or other presentations |

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

