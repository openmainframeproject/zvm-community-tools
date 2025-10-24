#
#
#         Name: makefile (rules file for 'make')
#         Date: 2024-09-03 (Tue) and prior and following
#       Author: Rick Troth
#
#

_default:  cphost.hex

cphost.hex:
	sh ./2cms cphbwrap.exec
	cms 'PIPE < cphost.s | PAD 80 | > CPHOST ASSEMBLE A F 80'
#
	-cms 'erase cphost text'
#	cms 'GLOBAL MACLIB HCPGPI HCPPSI'
	cms 'GLOBAL MACLIB HCPGPI HCPPSI HCPOM1 HCPOM2 DMSOM'
	# 'HLASM CPHOST'
	cms 'CPHBWRAP EXEC VMFHLASM CPHOST HCPVM (OUTMODE A'
	cms 'erase cphost assemble'
#
	cms 'PIPE < CPHOST TEXT | SPEC 1-* C2X N | > ./cphost.hex'
	cms 'erase cphost text'

cphost.vmarc.b64:  cphost.exec cphost.hex
	-cms 'erase cphost vmarctmp'
	sh ./2cms cphost.exec
	cms 'pipe < ./cphost.hex | spec 1-* x2c n | fblock 80 00 | > cphost text a f 80'
	cms 'vmarc pack cphost text a cphost vmarctmp a'
	cms 'vmarc pack cphost exec a cphost vmarctmp a (append'
	cms 'pipe < cphost vmarctmp | 64encode | > ./cphost.vmarc.b64 '
	cms 'erase cphost vmarctmp'

clean:
	rm -f cphost.hex cphost.vmarc.b64


