# Quick-Guide to Setting Up IPGATE

## 1. CP USER Definition

Define an appropriate CP USER for IPGATE:

```text
USER IPGATE LBYONLY 128M 256M BG
INCLUDE IBMDFLT
*
IPL CMS PARM FILEPOOL VMSYSU
IUCV *IDENT RESANY GLOBAL REVOKE
IUCV ALLOW PRIORITY MSGLIMIT 2000
IUCV ANY PRIORITY MSGLIMIT 2000
MACHINE ESA
OPTION QUICKDSP APPLMON MAXCONN 1000
CONSOLE 0009 3215 T OPMGRM1
```

### Notes & Variations

* **VMSYSU Filepool:** If the `VMSYSU` filepool is being used for IPGATE's "A" disk, run:
  ```text
  ENROLL USER IPGATE VMSYSU (BLOCKS 500
  ```

* **Operations Manager for z/VM:** If Operations Manager for z/VM is **not** being used, change the `CONSOLE` statement to reference the desired `SECUSER`, or simply omit `"OPMGRM1"`:
  ```text
  CONSOLE 0009 3215 T
  ```

---

## 2. File Configuration ("A" Disk)

IPGATE requires configuration of the following files on its "A" disk:

### `PROFILE EXEC`
* SPOOL the CONSOLE to the appropriate place.
* Un-comment the `NUCXDROP` and `NUCXLOAD` commands if you are running a version of z/VM that does **not** supply a version of `RXSOCKET MODULE` that supports TLS and IPv6.

### `IPGATE EXEC`
* Set `tls_label` to the value of IPGATE's TLS label (This label must be present in the `GSKKYMAN` database).
* `tls_label` may be set to a null value if TLS is not desired.
* **Note:** The current implementation of IPGATE only supports a single TLS label per IPGATE server.

### `TCPIP DATA`
* Reduce `ResolverTimeout` to a value between `3` and `5` (reduces potential wait time for IPGATE clients).
* Ensure proper values for `NSinterAddr` (If DNS servers are to be used with IPGATE, multiple values for `NSinterAddr` should be specified).
* Set `DomainLookup` to `FilesOnly` if DNS servers are **not** to be used for IPGATE.
* Change `TCPuserID` to an alternate TCP/IP stack if desired (IPGATE will pick up the TCPIP userid from this file).

### `ETC HOSTS`
* Add the appropriate hosts along with their desired IPv4 or IPv6 host addresses (This file is critical if `DomainLookup` has been set to `FilesOnly`).
* Every "node" name appearing in `IPGATE RESOURCE` should be **PINGable**.

### `ETC SERVICES`
* Port `4567` is the default for IPGATE (Providing a modified `ETC SERVICES` file allows for a symbolic port name override for port 4567).
* *Optional:* If the code is ever changed to reference the IPGATE port by name (e.g., `ipgate`), this modified file will be required.

### `IPGATE RESOURCE`
Code the local and remote filepool resource names in this file.

* **Format:**
  1. **Word 1:** Advertised name of the local resource
  2. **Word 2:** Actual local resource name
  3. **Word 3:** Scope of the resource
  4. **Word 4:** TCP port
  5. **Word 5:** IP address or Node Name where the advertised resource can be found

> **Node Name Note:** Refers to a standard hostname without a domain name suffix. It is not technically restricted to 8 characters (like a standard VM system name), but is restricted to 15 characters for backward compatibility.

**Example:**
To advertise your local `VMSYS` resource as `FREDSYS`, residing on node `FLINTSTONE`:

```text
*2345678  12345678 12345678 1234 123......
FREDSYS   VMSYS    SYSTEM   4567 FLINTSTONE
```

* `FLINTSTONE` must appear in `ETC HOSTS` with a valid IPv4 or IPv6 address, or pass through DNS resolution.
* An IPv4 address may be specified in place of `FLINTSTONE`.
* For backward compatibility, an IPv6 address should **not** be specified directly; specify a node name instead (field is restricted to 15 characters).
* *(See output of `CP QUERY RESOURCE` for current resource names).*

### `IPGATE USERMAP`
Code the mapping for incoming users to local resources.

* **Format:**
  1. **Word 1:** Origin IPv4 or Node Name
  2. **Word 2:** Originating user's VM userid
  3. **Word 3:** (Real) Local resource name
  4. **Word 4:** Local VM userid to use ("map") for authorization

**Example:**
To map user `BARNEY` at node `RUBBLE` to local user `FRED`:

```text
;origin_system origuser resource locuser
;23456789012345 12345678 12345678 12345678
;00.000.000.000 MAINT    VMSFS01  GUEST
RUBBLE          BARNEY   VMSYS    FRED
```

> **How it works:** Advertised resource `FREDSYS` is really `VMSYS` running on node `FLINTSTONE`. Local user `FRED` on node `FLINTSTONE` has authority to local resource `VMSYS`. This entry in `IPGATE USERMAP` allows user `BARNEY` at node `RUBBLE` to access local resource `VMSYS` as local user `FRED`.

⚠️ **Warning:** It is strongly recommended **not** to specify an SFS Administrator as the local user.

---

## 3. Required Files

| File | Description |
| :--- | :--- |
| `MTREXX MODULE` | Multitasking REXX enabler |
| `IPGATE1 MTREXX` | Main driver; starts Listener, handles console input |
| `IPGATE1I MTREXX` | Authenticate and handle incoming connections |
| `IPGATE1L MTREXX` | Listener: Accepts new connections, handoff to IPGATE1I (Handles "server" connections to resources) |
| `IPGATE1W MTREXX` | Wait for resource interactions |
| `IPGATE1Y MTREXX` | Handle "client" connections to resources |

* **Prerequisite:** `RXSOCKET MODULE` must be version **3.05 or later** (required for TLS and IPv6 support).

---

## Credits

* **Original Implementation:** Based upon previous work by Perry Ruiter, IBM, and others.
* **Updates:** TLS support, IPv6 support, and general code cleanup by Arty Ecock.