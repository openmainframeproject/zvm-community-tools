#!/usr/bin/env python3
#
# Port of the VIR2REAL EXEC, by Bruce Hayden, to Python 
# Display ratio or quotient of total virtual memory to LPAR real memory of your z/VM system
#
import logging
import subprocess
import sys
import re

# globals
logging.basicConfig(filename='/var/log/zlma/vir2real.log', format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger(__name__)
CMS_NSS = ["CMS", "GCS"]
CMS_DEV = ["0190", "0490", "0890", "0990"]
virtual_dev = 0
virtual_nss = 0
wss_pages = 0
total_vdisk = 0
vdisk_count = 0
IND_LINES = 3
WSS_VAR = "WS"

def run_cp_cmd(cp_cmd: str):      
  # run a CP command using vmcp
  cmd = f"sudo /usr/sbin/vmcp {cp_cmd}"
  log.debug(f"run_vm_cmd() running CP cmd: {cmd}")
  try:
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
  except subprocess.CalledProcessError as e:
    log.error(f"run_vm_cmd(): cmd {cmd} returned subprocess exception: {e}")
    sys.exit(1)
  vmcp_out = result.stdout
  return vmcp_out.strip().split('\n')      # split into lines

def conv_mem(memsize: str) -> int:
  # convert z/VM memory strings (1G, 512M) into MB
  memtype = memsize[-1]
  try:
    memory = int(memsize[:-1])
  except ValueError:
    try:
      return int(memsize)
    except ValueError:
      return 0
  if memtype in "Mm":
    return memory
  if memtype in "Gg":
    return memory * 1024
  if memtype in "Tt":
    return memory * 1048576
  if memtype in "Pp":
    return memory * 1073741824
  if memtype in "Kk":
    return memory // 1024
  return memory

def check_vmcp():
  # check that vmcp works 
  out = run_cp_cmd("QUERY USERID")
  if not out:
    print("Error: cannot run 'sudo vmcp'")
    sys.exit(4)

def get_virtual_memory():
  # query all logged-on users and accumulate virtual memory numbers
  # sample IND USER output:
  # ind user mikemac
  # USERID=MIKEMAC  MACH=ESA STOR=16M VIRT=V XSTORE=---
  # IPLSYS=CMS      DEVNUM=00010
  # PAGES: RES=226  WS=168  LOCKEDREAL=0  RESVD=0
  #        INSTAN=226
  # NPREF=0  PREF=0  READS=0  WRITES=0
  # CPU 00: CTIME=00:00 VTIME=000:00 TTIME=000:00 IO=000049
  #         RDR=000000 PRT=000001 PCH=000000 TYPE=CP   CPUAFFIN=ON
  global virtual_dev, virtual_nss, wss_pages
  users_output = run_cp_cmd("QUERY NAMES at '*'")
  for line in users_output:
    entries = [e.strip() for e in line.split(",") if e.strip()]
    for entry in entries:
      if "VSM " in entry:
        # print(f"get_virtual_memory(): skipping VSM line")
        continue
      parts = entry.split()
      user_id = parts[0].strip(",")
      # print(f"get_virtual_memory(): user_id: {user_id}")
      if user_id.startswith("LOG"):
        # print(f"get_virtual_memory(): skipping LOG entry")
        continue
      ind_output = run_cp_cmd(f"INDICATE USER {user_id}")[:IND_LINES]
      if not ind_output:                     # not expected
        # print(f"get_virtual_memory(): WARNING!  No ouptut from INDICATE USER {user_id}")
        continue
      text = " ".join(ind_output)
      stor_match = re.search(r"STOR=\s*([0-9]+[KMGTP]?)", text, re.IGNORECASE) # match STOR=16M
      if not stor_match:
        # print(f"get_virtual_memory(): WARNING! Did not find STOR value - skipping")
        continue
      memory_size = conv_mem(stor_match.group(1))
      wss_match = re.search(r"WS=\s*(\d+)", text, re.IGNORECASE) # match WS=168 (working set pages)
      if wss_match:
        wss_pages += int(wss_match.group(1))
      is_cms = any(nss in text for nss in CMS_NSS)
      if not is_cms:
        for dev in CMS_DEV:
          if dev in text:
            is_cms = True
            break
      if is_cms:
        virtual_nss += memory_size
        # print(f"get_virtual_memory(): virtual_nss for {user_id}: {memory_size} virtual_nss: {virtual_nss}")
      else:
        virtual_dev += memory_size
        # print(f"get_virtual_memory(): virtual_dev for {user_id}: {memory_size} virtual_dev: {virtual_dev}")

def get_real_memory():
  # Query real memory totals (MB)
  # Return: {"total": <val>, "standby": <val>, "reserved": <val>}
  total = standby = reserved = 0
  for line in run_cp_cmd("QUERY STORAGE"):
    # Example: STORAGE = 48G CONFIGURED = 48G INC = 1M STANDBY = 0  RESERVED = 0
    m = re.search(r"STORAGE\s*=\s*([0-9]+[KMGTP]?)", line)
    if m:
      total = conv_mem(m.group(1))
      # print(f"get_real_memory: found STORAGE total: {total} MB")
    m = re.search(r"STANDBY\s*=\s*([0-9]+[KMGTP]?)?", line)
    if m:
      standby = conv_mem(m.group(1))
      # print(f"get_real_memory: found STORAGE standby: {standby} MB")
    m = re.search(r"RESERVED\s*=\s*([0-9]+[KMGTP]?)?", line)
    if m:
      reserved = conv_mem(m.group(1))
      # print(f"get_real_memory: found STORAGE reserved: {reserved} MB")
  return {"total": total, "standby": standby, "reserved": reserved}

def get_vdisk_info():
  # query defined virtual disks
  count = size_mb = 0
  for line in run_cp_cmd("QUERY VDISK"):
    # Example: "VDISK RHEL8    0152   200000 BLK"
    m = re.search(r"VDISK\s+\S+\s+\S+\s+(\d+)\s+BLK", line)
    if m:
      count += 1
      blocks = int(m.group(1))
      size_mb += blocks * 512 // (1024 * 1024)  # Convert blocks to MB 
      # print(f"Found VDISK: {blocks} blocks = {blocks * 512 // (1024 * 1024)} MB")
  # print(f"Total VDISKs: {count}, Total size: {size_mb} MB")
  return {"count": count, "size_mb": size_mb}

def get_nss_info():
  # query NSS definitions 
  # Example output of Q NSS:
  # OWNERID  FILE TYPE CL RECS DATE  TIME     FILENAME FILETYPE ORIGINID
  # *NSS     0115 NSS  A  033K 08/24 01:16:29 CCNSEG   DCSS     BLDSEG
  # *NSS     0117 NSS  A  1302 08/24 01:16:54 ZCMS     NSS      BLDCMS
  count = recs = 0
  for line in run_cp_cmd("QUERY NSS"):
    if line.strip().startswith("*NSS"):    # Get NSS entries 
      count += 1
      parts = line.split()
      if len(parts) >= 5:                  # Extract ECS - 5th column after splitting
        recs_str = parts[4]                # RECS column
        if recs_str.endswith('K'):         # nnnK = multiply by 1000
          recs += int(recs_str[:-1]) * 1000
        elif recs_str.endswith('M'):       # nnnM = multiply by 1000000
          recs += int(recs_str[:-1]) * 1000000
        elif recs_str.isdigit():           # Plain number
          recs += int(recs_str)
        else:
          print(f"Warning: Could not parse RECS value: {recs_str}")
  # print(f"Total NSS count: {count}, Total records: {recs}")
  return {"count": count, "recs": recs}

def to_pages(s):
  if s.endswith("K"):
    return int(s[:-1]) * 1024
  if s.endswith("M"):
    return int(s[:-1]) * 1024 * 1024
  return int(s)

def get_paging_info():
  # query page usage
  # sample Q ALLOC MAP output:
  # ...
  # VOLID  RDEV      START        END  PAGES IN USE   PAGE USED
  # ...
  # SUMMARY                            1761K      0          0%
  # ...
  # Returns: dict: {"total": int, "free": int, "used": int}
  total_pages = free_pages = used_pages = 0
  for line in run_cp_cmd("QUERY ALLOC PAGE"):
    if line.strip().startswith("SUMMARY"):
      # print(f"SUMMARY line: {line}")
      parts = line.split()
      if len(parts) >= 3:
        total_str = parts[1]   # e.g., "1761K"
        used_str  = parts[2]   # e.g., "0"
        total = to_pages(total_str)
        used = to_pages(used_str)
  free = total - used
  # print(f"total: {total} free: {free} used: {used}")
  return {"total": total, "free": free, "used": used}

def create_report():
  # gather the numbers and produce the report
  global virtual_dev, virtual_nss, wss_pages
  real = get_real_memory()                 # gather values
  vdisk = get_vdisk_info()
  nss = get_nss_info()
  paging = get_paging_info()
  get_virtual_memory()
  total_virtual = virtual_dev + virtual_nss
  instantiated = (wss_pages * 4) // 1024   # pages to MB
  usable_real = real["total"] - real["reserved"]

  print(f"Total Virtual storage (non CMS): {virtual_dev:7d} MB ({virtual_dev/1024:.1f} GB)")
  print(f"Total Virtual storage (CMS):     {virtual_nss:7d} MB ({virtual_nss/1024:.1f} GB)")
  print(f"Total Virtual storage (all):     {total_virtual:7d} MB ({total_virtual/1024:.1f} GB)")
  print(f"Total of all Instantiated pages: {instantiated:7d} MB ({instantiated/1024:.1f} GB)")
  print(f"Usable real storage (pageable):  {usable_real:7d} MB ({usable_real/1024:.1f} GB)")
  print(f"Total LPAR Real storage:         {real['total']:7d} MB ({real['total']/1024:.1f} GB)")
  print(f"Maximum possible storage:        {real['total']:7d} MB ({real['total']/1024:.1f} GB)")
  print()
  print(f"Total Virtual disk (VDISK) space: {vdisk['size_mb']:7d} MB ({vdisk['size_mb']/1024:.1f} GB)")
  if vdisk["count"] > 0:
    print(f"Average Virtual disk size:        {vdisk['size_mb']//vdisk['count']:7d} MB")
  if usable_real > 0:                      # ratios
    print()
    print(f"Virtual to (usable) Real storage ratio:     {total_virtual/usable_real:.1f} : 1")
    print(f"Virtual + VDISK to Real storage ratio:      {(total_virtual+vdisk['size_mb'])/usable_real:.1f} : 1")
    if virtual_dev > 0:
      print(f"Virtual to Real ratio (non CMS work only): {virtual_dev/usable_real:.1f} : 1")
    if instantiated > 0:
      print(f"Total Instantiated to Real storage ratio:   {instantiated/usable_real:.1f} : 1")
  print()                                  # paging space
  if paging["total"] > 0:
    used_pct = 100 * paging["used"] / paging["total"]
    total_mb = paging["total"] * 4 // 1024 # pages to MB
    free_mb = paging["free"] * 4 // 1024
    print(f"Paging: {total_mb:7d} MB total, {free_mb:7d} MB free, {used_pct:.1f}% used")
    req_all = total_virtual * 120 // 100   # ~20% overhead margin
    req_noncms = virtual_dev * 120 // 100
    warn_threshold = total_mb * 0.10
    print(f"ATTENTION:")
    print(f"Paging space should be at least: {req_all:7d} MB (all users)")
    # print(f"Paging space (excl CMS users):   {req_noncms:7d} MB")
    # print(f"Paging space warning if < {warn_threshold:.0f} MB free")
  else:                                    # no page space - not expected
    print("Paging space: 0")

# main() 
if __name__ == "__main__":
  check_vmcp()                             # verify vmcp works
  create_report()                          # get values and create report

