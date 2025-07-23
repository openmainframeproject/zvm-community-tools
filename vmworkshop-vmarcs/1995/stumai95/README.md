## ORIGINAL README

```
The STUMAIL archive contains the following files (grouped by functionality):

+------------------+
| CALVIEW Services |
+------------------+

The CALVIEW utility allows non-OfficeVision customers to query the calendars
of registered OfficeVision users, and view the result in an XEdit-based
panel format.

Filename Filetype Brief Description
-------- -------- -------------------------------------------------------------
CALVIEW  EXEC    *Used to allow customers to call CalView as a command
CALVIEW  XEDIT   *Displays a panel requesting calendar query parameters
CALVIEW  HELPCMS  Help file for CalView query panel
CALVIEWV XEDIT    Displays the calendar returned from the STUDENTS server
CALVIEWV HELPCMS  Help file for CalView query results (calendar display) panel
STUDENTS EXEC     STUDENTS service machine code, accepts queries from CALVIEW
                  client and returns results to client

* Requires DOPANEL EXEC and $$TEMP$$ $$FILE$$, also in the STUMAIL ARCHIVE.

+--------------------------------------------+
| Automated Student Account Request Services |
+--------------------------------------------+

ISARC (Individual Student Account Request Component) and its associated servers
form the automated student account request services.  In addition to the
client interface (ISARC), two service machines exist in our environment.
The first service machine, VMSERV01, runs the SAMSERVE EXEC code below.  Its
main two functions is to receive and respond to client requests, and at
designated times form the account creation job and pass the job on to the
second service machine, VMSERV02.  VMSERV02 takes the account request job
and essentially creates the accounts, updates online messages, and places
the new account ids into a database.  The code for VMSERV02 is not included
with this archive as the entire account creation process is largely site-
dependent.  The original documentation for ISARC has been included with the
archive.

Filename Filetype Brief Description
-------- -------- -------------------------------------------------------------
ISARC    LISTING  Documentation for student account request component
ISARC    EXEC    *Used to initiate the account request client interface
ISARCMNU XEDIT    Code to display menu of choices for account request
ISARCREQ XEDIT    Code to obtain information for requesting account
ISARCQRY XEDIT    Code to obtain information to query status of account request
ISARCRST XEDIT    Code that interfaces with VMSERV01.  Registers request for
                  account.
ISARCQST XEDIT    Code that interfaces with VMSERV01.  Obtains status of
                  account request.
ISARCINF XEDIT    Code to display information about student accounts
ISARCINS XEDIT    Code to display instructions on requesting a student account
ISARCHLP XEDIT    Code to display help screens
INSTRUCT ISARCTXT Actual text explaining how to request an account
INFORM   ISARCTXT Actual text explaining student accounts before requesting
$MAINT   $DISABLE#Used to disable entire account request interface
$ABOUT   $DISABLE#Used to disable only the "About Accounts" menu item
$QUERY   $DISABLE#Used to disable only the "Query status of request" menu item
$REQUEST $DISABLE#Used to disable only the "Request account" menu item
ISARCREQ ISARCHLP Help text for account request panel
ISARCINF ISARCHLP Help text for about accounts panel
ISARCMNU ISARCHLP Help text for main menu
ISARCQRY ISARCHLP Help text for query status panel
MAKISARC EXEC     File used to "make" account request component
SAMSERVE EXEC     VMSERV01 service machine code
PUTDATA  REXX     VMSERV01 service machine additional code

* Requires $$TEMP$$ $$FILE$$, also in the STUMAIL ARCHIVE.
# See documentation, ISARC LISTING, for instructions on use.

+------------------------------+
| Panels to Front-End Commands |
+------------------------------+

The following code together form several different panels that gather input
from customers and forms the appropriate command for them.  These panels
were used to provide an intermediary between the menus and the commands to
invoke several different utilities and applications (such as MailBook, CMS
TELL, WHOIS, etc.).

Filename Filetype Brief Description
-------- -------- -------------------------------------------------------------
MMAILUSR EXEC    *Used to allow customers to call MMAILUSR as a command
MMAILUSR XEDIT   *Code to display panel and accept input for MailBook
MMAILUSR HELPCMS  Help file for the MMAILUSR panel
WHOISIT  EXEC    *Used to allow customers to call WHOSIT as a command
WHOSIT   XEDIT   *Code to display panel and accept input for WHOIS
WHOSIT   HELPCMS  Help file for the WHOSIT panel
WHOSIT   LOCATION Contains the locations to query for KECNET (Kentucky
                  Educational Computing NETwork).  Can be modified as desired.
TELLPRMT EXEC    *Used to allow customers to call TELLPRMT as a command
TELLPRMT XEDIT   *Code to display panel and accept input for CMS TELL
TELLPRMT HELPCMS  Help file for the TELLPRMT panel

* Requires DOPANEL EXEC and $$TEMP$$ $$FILE$$, also in the STUMAIL ARCHIVE.

+-------------------+
| OTHER INFORMATION |
+-------------------+

The programs, data, and documentation included with this archive may be
freely distributed and modified in whatever manner the user sees fit.
The files in this archive have been provided courtesy of the University
of Louisville (Louisville, KY) and the programmers responsible for the
files' development.  As such, the programmers would appreciate notification
of any changes, enhancements, or just general comments and suggestions
concerning the code and/or data.  Such comments and suggestions are
very much welcome and could help us improve the code for our customers!
On behalf of all those who wrote the code for the University of
Louisville, please send any correspondence to either

     Paul Lewis          PDLEWI01@ULKYVM.LOUISVILLE.EDU

          -or-

     Barbara Jones       BAJONE02@ULKYVM.LOUISVILLE.EDU
```
