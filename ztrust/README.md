# ztrust

This is the ztrust folder
which serves as a trust anchor for the z/VM and z/Linux community.

## PGP keys

The `pgp` sub-directory has a number of PGP keys
contributed by members of the community. It forms a web-of-trust.

## PKI certificates

The `pki` sub-directory has a number of PKI root certificates
contributed by members of the community. Some of these are signed
using PGP.

## BYOK - Bring Your Own Key

One of the biggest problems, of course, is that folks don't understand
 the caveats, go in with both feet first, and get burned. All of the CSPs,
 for example, offer some sort of cryptographic service. None of them are
 BYOK (Bring Your Own Key)-in other words, you're trusting the service itself
 not to attack you or to get compromised and allow an attack. WCGW?

## Multiplicity

This sub-directory exists in two repositories:

https://github.com/openmainframeproject/zvm-community-tools/tree/main/ztrust

https://github.com/trothr/vmworkshop/tree/master/ztrust

Eventually we hope to include keys and certs from the larger mainframe community.


