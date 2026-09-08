/* PUTDATA REXX */
Arg datafid                             /* GET DATA FILE NAME */
'READTO inputjcl'                       /* READ RECORD */
Do until rc=12                          /* do until eof */
  /* check for input dd */
  If inputjcl='//SYSUT1   DD *' then do
    'OUTPUT 'inputjcl                   /* write the line */
    'READTO inputjcl'                   /* read the BLANK record */
    'OUTPUT 'inputjcl                   /* write the BLANK line */
    rfname= Delstr(Date(O),3,1)         /* build request file name */
    rfname= 'ST'Delstr(rfname,5,1)
    'CALLPIPE < 'datafid ,              /* GET DATA FILE */
    '| *:'
    End
  Else
    'OUTPUT' inputjcl                   /* copy record to output */
  'READTO inputjcl'                     /* read the next record */
  End                                   /* end JCL file read */
EXIT RC*(RC^=12)                        /* RC = 0 IF END-OF-FILE */
