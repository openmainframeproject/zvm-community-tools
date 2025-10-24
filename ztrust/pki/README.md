# ztrust/pki

This is the ztrust/pki folder
containing root PKI certificates of z/VM and z/Linux vendors and users.

## Signing

Root certificates are not signed by another party or key or certificate.
Root certificates are by nature self-signed. Their veracity is indicated
by their presence in the trust store distributed with 

PKI root certificates found here *may* be signed by PGP keys
(found in the companion "pgp" folder) as detached signatures.
A "detached" signature does not change the content of the signed file,
so detached PGP signing does not harm the certificates.

## Naming

PEM-encoded certificates have a file type extension of `.crt`.

Human readable "text" form have a file type extension of `.txt`.
The PEM-encoded certificate will be found at the end of such a file.

Detached PGP signatures have a file type extension of `.asc`
indicating that they are ASCII-armored. The full extension is `.crt.asc`.

## Rationale

The following observation is from Dan Rathbun, CIO/CISO for
several enterprises:

*"One of the inherent problems of standard HTTPS is that trust put in
a website is defined by certificate authorities: a hierarchical and
closed set of companies and governmental institutions approved by your
web browser vendor. This model of trust has long been criticized
and proven ... to be vulnerable to attacks ..."*

This trust anchor is intended to remedy that problem
in the context of the mainframe community.


