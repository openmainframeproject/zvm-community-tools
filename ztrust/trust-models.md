# Trust Models

It's all about trust.

With contemporary encryption, there are two primary types of keys:
symmetric and asymmetric. They provide two very different kinds of
protection. They are usually (almost always) used together,
but it's asymmetric encryption which lets us identify and verify.

Asymmetric cryptography provides the foundation for performing
verification and identification under program control, maintaining trust.

## Symmetric Cryptography

Symmetric cryptography is conceptually simple.
It's like the door to your house or apartment (assuming that you have
a traditional mechanical lock). You have a key. It unlocks the door.
It can also LOCK the door when you leave. The same key enables both tasks.

Symmetric keys are easily copied. That's both convenient and necessary.
This is why we change the locks when your place changes occupants.

## Asymmetric Cryptography

With asymmetric encryption, what you have is a *pair* of keys,
mathematically related but distinct. One half of the pair is the
"public key". The other is the "private key" or *secret* key. This
asymmetric type of crypto is commonly called "public key cryptography".

The way asymmetric encryption works is that someone who wants to send
a protected message to you must have your *public* key. They use your
public key to encrypt the message. But unlike for a symmetric key,
the process cannot be reversed. ONLY YOU, with your *private* key
can decrypt the message. This means that messages can be securely sent
to you and *only* you.

But there's more!

It turns out that the logic can be turned around for a really handy effect.
If you make some public statement, how do we know that it truly
came from you? You can run a hash or a checksum against the document
and then encrypt *that* with your private key (which only you possess)
then we in the public (with your public key) can decrypt the checksum
or hash and confirm authenticity. Any other key would either get
incorrect data or would fail to decrypt at all. We know it's you!

## Trust Models

There are at least three trust models using the asymmetric
cryptography we have described: hierarchical third party trust
(PKI), person-to-person trust (PGP/GPG), and manual assertion (SSH).

## PKI (SSL/TLS)

PKI stands for "Public Key Infrastructure".

When the World Wide Web was young, but we were starting to do business
on it, developers began creating data protection schemes, most visible
being SSL or "Secure Sockets Layer". SSL uses asymmetric cryptography
to provide assurance of the veracity of the target web site. The logic
works, but there is a need for distributing trusted keys and certificates.

How do you establish trust? How do you deploy the signing/issuing
certificates so that everyone's web browser will "trust" the good sites
and flag the forgeries? This is what Public Key Infrastructure is about.

For PKI, there are Certificate Authorities (CAs) who issue certificates
to the myriad web site operators. If you trust the CA, then you take
their root certificate(s) into your trust store and your browser will
perform the necessary asymmetric cryptography to confirm each site.

This has become big business,
but it requires ongoing reliance on a third party:
the CA must always be consulted (by proxy of its root certificates)
in the handshake between the end user or client program and the server.

## PGP and GPG

PGP stands for "Pretty Good Privacy" and was the first asymmetric
encryption service widely known to the general public. GPG is Gnu
Privacy Guard, a popular alternative, fully interoperable with PGP.

All implementations of PGP, including GPG, have the concept of a keyring
where you collect the public keys that you will use. The structure of the
keys allows that they be cryptographically "signed" by other PGP users
while remaining fully intact. There is an "import" function whereby you
add keys to your keyring. The import operation safely updates keys which
you already hold, adding signatures of others, etc.

By mutually signing each other's keys, the greater community of people
who use PGP has established a "Web of Trust". The PGP trust model is
*highly* reliable for personal affirmation, but it does not scale well
in enterprise environments. Bluntly, it is confusing for non-technical
users and training is already a huge cost.

The Debian Linux community has established their own trust web,
demonstrating that (for highly technical users) the PGP model *can* scale.

## SSH - Secure Shell

SSH, Secure Shell, uses the same combination of symmetric
and asymmetric cryptography as is found in TLS/SSL and in PGP.
But SSH does not use key signing for its primary operation.

The main thing most people use SSH for is secure remote access.
To this end, the user provides his SSH public key to the target systems.
For example, standard sign-on via SSH keys is achieved by appending
your SSH public key (from the secure side) to the `~/.ssh/authorized_keys`
file (on the target side). With that in place, there is no need for
sign-on via password. Indeed, sign-on via SSH key is more secure
and more manageable.


