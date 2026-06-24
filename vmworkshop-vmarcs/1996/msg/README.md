# MSGD

This is freely distributable software.   The author shall not be held
liable for any incorrect operation of your system(s) resulting from
using this package.   (having said that,  I think you'll find that it
*does* work)

MSGD is a server to handle the Message Send Protocol per RFC 1312.
Neither the server nor the client implement all features of RFC 1312.
Note that you can run the client without the server and vice versa.

Files in the package are:
MSGD EXEC
TELL EXEC
MSGD README (this file)
MSGD DIRECT

To run MSGD,  you need:

1.   IBM VM TCP/IP Version 2 (5735-FAL)
2.   REXX/Sockets from Arty Ecock of CUNY
3.   a service virtual machine named MSGD

MSGD is the TCP and UDP operative Message Send Protocol server. It needs port 18 from your TCP/IP service machine and likes to have class B (for MSGNOH), but will work with just class G (for MSG).

TELL EXEC is a (from scratch) replacement for standard CMS TELL.

The Message Send Protocol is considered experimental. Discussion and suggestions for improvement are requested by the authors of RFC 1312. This protocol is used to send a short message to a given user on a given host. Such message service is known in the VM world as "TELL". On VM, RSCS provides this kind of interactive messaging, but TCP/IP, until now, has not.

The details of the protocol are discussed in RFC1312 TXT (included). Thanks go to Russell Nelson of Crynwr Software and Geoff Arnold of Sun Microsystems, Inc. for collaborating on this RFC.

All you really need to do is:

1.   Create the MSGD virtual machine,
2.   put MSGD EXEC on a disk available to the MSGD service VM and arrange that MSGD EXEC is invoked (eg: from PROFILE),
3.   put the supplied TELL EXEC in such a place where your users can invoke it. (the supplied TELL EXEC should function as a direct replacement for the standard CMS TELL, but there is NO WARRANTY provided)

## Bugs

The client (TELL) is only TCP based,  and should have UDP support for "broadcasts".   (server handles both)

The client ties-up CMS until the message is delivered. (just the sending virtual machine, not the whole system)

