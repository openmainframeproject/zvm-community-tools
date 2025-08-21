# Verification

Asymmetric crypto is more often used for *verification*
than for data protection. (Think "code signing".)

The process can be reversed: If I run some hash or checksum over a
message that I want to send, and then encrypt that with my *private* key,
anyone who has my public key can decrypt that checksum/hash and use it
as a signature. They would run their own hash/checksum against the
file or message and compare with the decrypted one check.
If they match then the signature is authentic.

## Signing Email

Many PGP users regularly sign their outgoing email.
The standard method presents the signature as a MIME attachment.
(Email services and programs which don't recognize the standard
will present the signature rather than process it.)

Any recipient with your public key and using an email client program
that honors the standard will be able to confirm that the message
is legitimate (that it came from you). As the "PGP web of trust"
grows, it becomes easier for recipients who don't know you personally
to "trust" your public key and therefore "trust" your signed email.

Email signature verification is automatic with email client programs
which have built-in PGP support. The program will alert the user when
a signature fails to verify or when the relevant public key is missing.

Email can also be "signed" using PKI certificates,
but that usually involves commercial certificate authorities (CAs).

## Signing Files (Signing Code)

The same encrypted hash logic applies both to email and to files.

More and more open source software is PGP signed by the authors.
That is usually achieved using a detached signature, which is easy
to do with `gpg` which is standard on Linux systems and commonly
available for most other systems (Unix and Windows and MacOS).

    gpg  --armor  --detach-sign  file-to-sign

The above command results in a file named `file-to-sign.asc`.
If the file to be signed was named `myprogram.c` then the detached
signature would be named `myprogram.c.asc`.

Verification is similarly easy:

    gpg  --verify  file-to-sign.asc

`gpg` will know to remove the `.asc` suffix and comare against
`file-to-sign`, extracting key ID and related info from the
signature file.

A real-life example is the source code to the BASH shell. A recent
release of BASH is packged as `bash-5.3.tar.gz`. The detached signature
is `bash-5.3.tar.gz.sig`. (`.sig` is a binary signature file,
contrast with `.asc` which is "ASCII armored". Either type works.
Download both files from the web site, then ...

    gpg  --verify  bash-5.3.tar.gz.sig

That confirms both the integrity of the download
and that it was not modified by a rogue actor on the server side.


