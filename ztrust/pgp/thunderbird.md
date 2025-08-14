# Thunderbird and PGP

Thunderbird email has built-in PGP capability.
For earlier releases of Thunderbird, there was a plug-in to enable
PGP encryption and decryption of email. As of version 78 in July of 2020,
Thunderbird includes an OpenPGP implementation, so integration is much easier.

This document discusses creating your own key pair,
setting your account to use the key pair,
and gathering public keys from other email users.

This document assumes that you are already using the
Thunderbird email client for at least one of your email identities.

## Receiving and Signing

Asymmetric cryptography which OpenPGP provides gives us two things:
the ability to *cryptographically sign* outgoing email
and the ability to *receive encrypted* incoming email.

Establishing your own PGP keys is an essential first step.

## Generate your Key Pair

To use PGP, you need a PGP key pair. 
The "public" half of the pair is intended to be shared far and wide.
But keep the "secret" (or "private") half to yourself. DO NOT let it
get exfiltrated from your Thunderbird configuration.

Under the `Tools` menu, find `OpenPGP Key Manager`. Select that.

In the key manager menu, select `Generate` to generate a new key pair.
Choose the identity (the email address) for this key pair. You can choose
"key does not expire" for now and can add an expiration later. A key type
of RSA is good, and select the largest key size available (usually 4096 bits).

Key generation usually takes less than a minute. When you generate
an asymmetric key pair you get both the public and the private.

## Enable your Key Pair

Under the `Account Settings` menu, find the `End-to-End Encryption`
option for your email address and select that. The key pair that you
just generated should be available. Check that.

You can (and should) sign all (or most) outgoing email.
Anyone with whom you share you public key can verify that a signed
message actually came from you. Signing with your public key adds to
the broader recognition of that key. (It boosts your reputation.)

When composing a message, under the `Security` menu,
select `Digitally Sign`.

Note: Some email distribution lists prevent sending with attachments.
The standard for signing email with PGP presents the signature as a
MIME attachment. Mailing lists which strip attachments will render your
messages unsigned (but still go through). Mailing lists which reject
email with attachments will prevent you from posting. It's best to
persuade email list managers to allow attachments (or at least to allow
PGP signatures, if the list management software can be that selective).

## Distribute your Public Key

Your public key (that is, the "public" half of your key pair) is so
called because it is intended to be distributed publicly far and wide.

Note: NEVER let out your PRIVATE key (the secret half of your key pair).

People who have your public key can encrypt email that they send to you,
mitigating the risk that a third party might read it. Only you have the
private key. Services like GMail become a pipeline between both parties.

In Thunderbird's `OpenPGP Key Manager`, highlight your identity
and several options become available:

* `File` / `Export Public Key(s) To File`
* `File` / `Send Public Key(s) By Email`
* `Edit` / `Copy Public Key To Clipboard`
* `Keyserver` / `Publish`

The first is probably the most straight-forward.
It saves your public key to a file which you can then distribute
on a flash drive. (Getting keys in person is the single most reliable
way to know with certainty that the key belongs to the named owner.)

## Acquire Other Public Keys

In order to verify signatures of others, you need their public keys. <br/>
In order to send encrypted email to others, you need their public keys. <br/>
Either way, you want the public keys of people with whom you exchange email.

The `OpenPGP Key Manager` function has several ways to import keys.

* `File` / `Import Public Key(s) From File`
* `Edit` / `Import Key(s) From Clipboard`
* `Edit` / `Import Keys(s) From URL`
* `Keyserver` / `Discover Keys Online`

The first of these options is probably the easiest to work with:
Save a public key which you have received (securely) to a file
and then import that public key from the file.

A single file can contain many keys.

## References

https://support.mozilla.org/en-US/kb/openpgp-thunderbird-howto-and-faq


