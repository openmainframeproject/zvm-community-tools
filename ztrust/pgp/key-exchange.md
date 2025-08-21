# Key Exchange

When PGP was first released, it was called
"strong encryption for the masses". Since then,
other security and privacy schemes also use asymmetric cryptography.
But in all cases, there is the need to establish trust
and that involves acquiring or deploying public keys.

There are many ways to distribute your own public key(s).
Or if you are the public party, there are many ways to acquire
the public keys of others. The hard part is assuring the ownership
of the key. Here are three ways to vet public keys.

## In Person

There is a tradition of "key signing parties" in the PGP world.
We come with printed copies of our PGP key fingerprints and photo IDs
(driving license, passport, etc), confirm our fingerprints with the group,
then go back to our keyboards and sign the keys of those which match.
(No need for computers during the face-to-face part.)

On a smaller scale, you can swap removable media containing your keys.
The fact that you got a thumb drive from the other person means that you
*know* it came from them. (Unlikely to have been tampered with.)

Such in person exchanges are the single most effective way to assure
ownership of the keys we are collecting. But they're not always practical
so there are other ways to introduce ourselves.

## Signed Introductions

In the first section, "in person", we cryptographically sign
the public keys of other people. That's not so much for our own benefit.
(We posess those keys and can now use them.) It's for the benefit
of others. Rick and Matt met face-to-face and exchanged public keys
and cross-signed. So now if you know Matt but don't know Rick,
you can "trust" Rick's key because of Matt's signature, and vice versa.

This is the concept behind the PGP "web of trust".
When Matt, Rick, Arty, and Jim have all signed Tom's key,
you have strong assurance that Tom's key is legitimate.
The more co-signed keys in the web, the stronger the trust.

Going further, a signature from someone in the web of trust
on Todd's PKI certificate proves that Todd really does own that cert.
Similarly, code from Ed's company with a web-of-trust signature
assures you that it's the real installation media.

## Visual Online

What if you are trying to vet the public key of a colleague
on the other side of the ocean? In a post-pandemic world,
we have gotten more comfortable with online meetings.
(The downside to this is that AI evolves and deep fakes grow
so weigh the risks.)

For online key exchange, the minimum requirement is for the two parties
exchaing keys (obviously) and a third person who knows both of the first
two well. This third person (call him the verifier) need not be a PGP
participant. He only needs to assure key holder A, "yes, this is B",
and assure key holder B, "yes, this is A". He must recognize both A and B
by sight and ideally should be able to ask one or more questions of each
for additional assurance.


