# ztrust

This is the ztrust folder
which serves as a trust anchor for the "System Z" mainframe community.

In the late 1980s, we got asymmetric cryptography.
The logic had been developed a decade earlier (two independent teams)
but it took some time for the idea to catch on. The most significant
thing asymmetric crypto gives us is the ability to form *cryptographic*
trust relationships, where we can use digital media to assure authenticity.

As of this writing, there are three popular services which use asymmetric
crypto: PKI (SSL/TLS), SSH Secure Shell, and PGP "Pretty Good Privacy".

This collection is all about BYOK. (see below)

## PGP keys

The `pgp` sub-directory has a number of PGP keys
contributed by members of the community. It forms a web-of-trust.

The signifcance of PGP is that it is person-to-person.
It goes deeper than commercial or institutional trust.
But establishing and maintaining personal trust can be time consuming.

## PKI certificates

The `pki` sub-directory has a number of PKI root certificates
contributed by members of the community. Some of these are signed
using PGP.

Most readers will understand that PKI is the differentiator between
`http` and `https` on the web. The latter is secured via SSL (now known
as TLS). Web servers speaking HTTPS must have a server certificate.
Technically, that certificate is a "PKI server certificate".

Ordinarily, PKI certificates are issued by a Certificate Authority (CA).
There are cases where a CA is not available or where an in-house
or home-grown CA is preferred. Root certificates found here are
of that sort. When they are signed using PGP, consumers have assurance
which they would not otherwise have.

## BYOK - Bring Your Own Key

One of the biggest problems with cryptography and security is that
most folks don't understand the caveats, go in with both feet first,
and get burned. All of the CSPs, for example, offer some sort of
cryptographic service. None of them are BYOK (Bring Your Own Key).
In other words, you're trusting the service itself not to attack you
or to get compromised and allow an attack. What could go wrong?

Here we have a combination of cross-signed PGP keys forming a
web of trust. We also then have PKI root certificates which have been
signed by PGP keys from that trust web. Signature verification using
`gpg` is easy. Both GPG and (especially) OpenSSL are common on Linux
systems (Z or otherwise) and available for z/OS.

You can (should!) bring your own key to this party.
If you don't know how to generate a PGP key pair, there are markdown
docs in this folder to guide you. The collection of keys and certs here
is for your consumption. When the time comes that you want to go further
and protect your own email and content, you will want to use PGP
and are then welcome to connect with this web of trust.

## Multiplicity

This sub-directory exists in two repositories:

https://github.com/openmainframeproject/zvm-community-tools/tree/main/ztrust

https://github.com/trothr/vmworkshop/tree/master/ztrust


