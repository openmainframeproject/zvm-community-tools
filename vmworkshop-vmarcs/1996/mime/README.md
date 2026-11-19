## ORIGINAL README
```
Note that this accessory to RiceMAIL often uses your plain XEDIT
environment to display mail.   Some users will find this distasteful
because they haven't changed XEDIT defaults with a PROFILE XEDIT.

You'll probably want to fix your PROFILE XEDIT.   XEDIT leaves some
synonyms in place when you open other files.   Thus  PF3 (QUIT)  when
editing another file from viewing or composing MIME mail does strange
things.   Set PF3 to  COMMAND QUIT  instead of just plain  QUIT  in your
PROFILE XEDIT.   This symptom also affects  PF8 (FORWARD).   If you viewa MIME item,
then   X fn ft   to get another file into the XEDIT ring,  and then use
PF8 to scroll down,  you'll likely wind up in RiceMAIL's FORWARD screen.

Please read MIME NOTE about CHARSET issues from John Klensin.
SMTP and MIME (RFC822 and RFC1341 and friends) do not have a concept
of  "plain text".   On VM  (specifically on BITNET and with VM TCP/IP)
we've cheated and treated mail as  "plain text".

From SYSJJH%NMSUVM1.BITNET@pucc.princeton.edu Fri Mar 25 13:33:36 1994
Date: Thu, 24 Mar 1994 13:04:22 EST
From: Jeff Hoover <SYSJJH%NMSUVM1.BITNET@pucc.princeton.edu>
Reply to: VM GOPHER discussion list <VMGOPHER@pucc.princeton.edu>
To: Multiple recipients of list VMGOPHER <VMGOPHER@pucc.princeton.edu>
Subject: Re: Read MIME files from mail

On Thu, 24 Mar 1994 14:51:56 EST Jean Bedard said:

Jean, after several days I finally found out how to make the mailer read
MIME files. You have to get the MIMEREAD code like Rick said. But in
addition, in your mail options you need to set POSTREAD YES. If you don't
do this then the mail code will never enter into the MIME code.

I think it would have been a lot easier if in the header to some of these
programs if that had been stated. Other than that, it works real good.

If anyone is having any problems getting the mime/mail programs to work
just drop me a line. I will be more than happy to help you out.


Jeff Hoover


>>        Look on the gopher server at vm.rice.edu
>>under  "Other freely distributable CMS software"
>>for  "MIME decoder for CMS Gopher and RiceMAIL".
>>
>I did that. MIMEREAD EXEC can't be accessed. There is no documentation
>as how to implement it all (or is it in the MIMEREAD EXEC?)
>
>
>Jean Bedard, C.T.I., Universite Laval, Quebec, Canada
>Resp. VM/CMS, NetNorth, Listserv     Bitnet:   ADMIN AT LAVALVM1
>(418) 656-3632                     From SYSJJH%NMSUVM1.BITNET@pucc.princeton.edu Fri Mar 25 13:33:36 1994
Date: Thu, 24 Mar 1994 13:04:22 EST
From: Jeff Hoover <SYSJJH%NMSUVM1.BITNET@pucc.princeton.edu>
Reply to: VM GOPHER discussion list <VMGOPHER@pucc.princeton.edu>
To: Multiple recipients of list VMGOPHER <VMGOPHER@pucc.princeton.edu>
Subject: Re: Read MIME files from mail

On Thu, 24 Mar 1994 14:51:56 EST Jean Bedard said:

Jean, after several days I finally found out how to make the mailer read
MIME files. You have to get the MIMEREAD code like Rick said. But in
addition, in your mail options you need to set POSTREAD YES. If you don't
do this then the mail code will never enter into the MIME code.

I think it would have been a lot easier if in the header to some of these
programs if that had been stated. Other than that, it works real good.

If anyone is having any problems getting the mime/mail programs to work
just drop me a line. I will be more than happy to help you out.


Jeff Hoover


>>        Look on the gopher server at vm.rice.edu
>>under  "Other freely distributable CMS software"
>>for  "MIME decoder for CMS Gopher and RiceMAIL".
>>
>I did that. MIMEREAD EXEC can't be accessed. There is no documentation
>as how to implement it all (or is it in the MIMEREAD EXEC?)
>
>
>Jean Bedard, C.T.I., Universite Laval, Quebec, Canada
>Resp. VM/CMS, NetNorth, Listserv     Bitnet:   ADMIN AT LAVALVM1
>(418) 656-3632                       Internet: admin@vm1.ulaval.ca

------------------------------------------------------------------------

From SYSJJH%NMSUVM1.BITNET@pucc.princeton.edu Fri Mar 25 13:33:36 1994
Date: Thu, 24 Mar 1994 13:04:22 EST
From: Jeff Hoover <SYSJJH%NMSUVM1.BITNET@pucc.princeton.edu>
Reply to: VM GOPHER discussion list <VMGOPHER@pucc.princeton.edu>
To: Multiple recipients of list VMGOPHER <VMGOPHER@pucc.princeton.edu>
Subject: Re: Read MIME files from mail

On Thu, 24 Mar 1994 14:51:56 EST Jean Bedard said:

Jean, after several days I finally found out how to make the mailer read
MIME files. You have to get the MIMEREAD code like Rick said. But in
addition, in your mail options you need to set POSTREAD YES. If you don't
do this then the mail code will never enter into the MIME code.

I think it would have been a lot easier if in the header to some of these
programs if that had been stated. Other than that, it works real good.

If anyone is having any problems getting the mime/mail programs to work
just drop me a line. I will be more than happy to help you out.


Jeff Hoover


>>        Look on the gopher server at vm.rice.edu
>>under  "Other freely distributable CMS software"
>>for  "MIME decoder for CMS Gopher and RiceMAIL".
>>
>I did that. MIMEREAD EXEC can't be accessed. There is no documentation
>as how to implement it all (or is it in the MIMEREAD EXEC?)
>
>
>Jean Bedard, C.T.I., Universite Laval, Quebec, Canada
>Resp. VM/CMS, NetNorth, Listserv     Bitnet:   ADMIN AT LAVALVM1
>(418) 656-3632                     From SYSJJH%NMSUVM1.BITNET@pucc.princeton.edu Fri Mar 25 13:33:36 1994
Date: Thu, 24 Mar 1994 13:04:22 EST
From: Jeff Hoover <SYSJJH%NMSUVM1.BITNET@pucc.princeton.edu>
Reply to: VM GOPHER discussion list <VMGOPHER@pucc.princeton.edu>
To: Multiple recipients of list VMGOPHER <VMGOPHER@pucc.princeton.edu>
Subject: Re: Read MIME files from mail

On Thu, 24 Mar 1994 14:51:56 EST Jean Bedard said:

Jean, after several days I finally found out how to make the mailer read
MIME files. You have to get the MIMEREAD code like Rick said. But in
addition, in your mail options you need to set POSTREAD YES. If you don't
do this then the mail code will never enter into the MIME code.

I think it would have been a lot easier if in the header to some of these
programs if that had been stated. Other than that, it works real good.

If anyone is having any problems getting the mime/mail programs to work
just drop me a line. I will be more than happy to help you out.


Jeff Hoover


>>        Look on the gopher server at vm.rice.edu
>>under  "Other freely distributable CMS software"
>>for  "MIME decoder for CMS Gopher and RiceMAIL".
>>
>I did that. MIMEREAD EXEC can't be accessed. There is no documentation
>as how to implement it all (or is it in the MIMEREAD EXEC?)
>
>
>Jean Bedard, C.T.I., Universite Laval, Quebec, Canada
>Resp. VM/CMS, NetNorth, Listserv     Bitnet:   ADMIN AT LAVALVM1
>(418) 656-3632                       Internet: admin@vm1.ulaval.ca
```
