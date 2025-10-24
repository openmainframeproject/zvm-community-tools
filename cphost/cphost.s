.* Some lines had to be added or changed for z/VM 5.2.0.  For each
.* line changed, the pre-5.2.0 line immediately follows as a comment,
.* with a marker such as "// Before 5.2.0" or "// < 5.2.0" appended.
.* For larger sections, look for "*** Begin/End" comments.
         MACRO
&LABEL   TDGMDLAT &EPNAME
         MDLATHDR &EPNAME
         MDLATENT CP1STL,MODATTR=(RES,MP,DYN)
.*       MDLATENT CP1STL,MODATTR=(PAG,MP,DYN)  //Before 5.2.0
.*
         MDLATTLR
         MEXIT
         MEND
**********************************************************************
         HCPCMPID COMPID=TDG
         COPY HCPOPTNS
CP1STL   HCPPROLG ATTR=(RESIDENT,REENTERABLE),BASE=(R12)
* CP1STL   HCPPROLG ATTR=(PAGEABLE,REENTERABLE),BASE=(R12)  // < 5.2.0
* (c) Copyright International Business Machines Corporation, 2000, 2005
*                      All rights reserved
* Dummy update to create a CPHOST TXT620
*
* CP Exit to allow issuing 1st-level CP command from a live
* 2nd-level system.
*
* To use, once you have assembled this file into CP1STL TEXT
* put these files on
* some Class A user's A (191) disk and invoke the following commands
* (Subsequent lines assume you chose filemode B on the first line):
*
*   CPACCESS userid 191 filemode RR
*   CPXLOAD CP1STL TEXT B NOCONTROL TEMP
*   DEF COM CP1STLVL ANYTIME EPNAME CP1STLIN PRIVCLASSANY
*   ENABLE CMD CP1STLVL
*
* Then you invoke the desired 1st-level command by prepending CP1STLVL.
* For example,
*
*   CP1STLVL Q USERID
*
* In order to undo some of your handiwork, you may want to be aware
* of a few other commands:
*   DISABLE CMD CP1STLVL -- to disable the CP1STLVL command
*   QUERY CPXLOAD        -- find the identifier number of CP1STLVL TEXT
*   CPXUNLOAD ID nn      -- unload CP1STLVL TEXT (nn is the identifier)
*
* Notes:
*   The macro defined at the beginning allows for compiling, since
*   the program will not be listed in the regular HCPMDLAT.
*
* For more information, see _VM/ESA CP Exit Customization_.  The first
* edition of this is for VM Version 2, Release 1.0, October 1995,
* IBM publication number SC24-5672-00.
*
* Register usage:
*  R0  - Input, Prefix page addressing
*  R1  - Addresses of text input, temp storage
*  R2  - Length of text input data
*  R3  - Addressing for text output to console
*  R4  - not used
*  R5  - not used
*  R6  - Rx for Diagnose
*  R7  - Rx+1 for Diagnose, stand in for R1 in HCPCONSL
*  R8  - Ry for Diagnose
*  R9  - Ry+1 for Diagnose
*  R10 - not used
*  R11 - Addressing VMDBK
*  R12 - Addressing of this CSECT
*  R13 - Addressing SAVBK
*  R14 - not used
*  R15 - Return code
*
* >>> ORIGINALLY BY TIM GREER, AVAILABLE AT:                         @1
* HTTP://WWW.VM.IBM.COM/DOWNLOAD/PACKAGES/DESCRIPT.CGI?CP1STLVL      @1
* ----- CHANGES BY SHIMON (integrated in zVM5.2 by Kris Buelens)     @1
* 21/11/03 - 1. DON'T BOTHER SAVING R0.                              @1
*            2. USE PFX1 INSTEAD OF INTERNAL CONSTANT F'1'           @1
*            3. USE HCPGETST TO ALLOCATE 4000 BYTES, INSTEAD OF      @1
*               AN INTERNAL BUFFER OF 1600 BYTES.                    @1
*            4. ADD SPECIAL RETCODES 30K+4, 8, 12                    @2
*            5. RETURN CODES MUST USE SAVER2, NOT SAVER15.           @1
*            6. CHECK FOR 2ND LEVEL                                  @1
*            7. CHECK CC AFTER DIAG08. IF CC¼=0:                     @2
*               SCAN BACK FROM END OF BUFFER FOR LAST X'15'          @2
*               CALCULATE LENGTH OF EXISTING DATA TO DISPLAY         @2
*               ADD 31K TO REAL CP RETCODE: Buffer overflow          @2
*            8. DO NOT STORE INTO PROGRAM, USE SAVEWRK0-1 FOR PTRS   @2
* -------------                                                      @1
*
         COPY HCPEQUAT - Equates for common items
         COPY HCPPFXPG - Prefix Page for all host CPUs
         COPY HCPSAVBK - Call with savearea Block
*        COPY HCPSYSCM - System Common Area
         COPY HCPCSLPL - CONSOLE MACRO PARM LIST
         COPY HCPGSDBK - GENERAL SYSTEM DATA BLOCK
         COPY HCPVMDBK - VIRTUAL MACHINE DEFINITION BLOCK
*
CP1STLVL CSECT
         HCPUSING PFXPG,R0
         HCPUSING SAVBK,R13
*
CP1STLIN HCPENTER CALL,SAVE=DYNAMIC
*
*****************************************************************
         TM    PFXCPUID,CPUIDVM    RUNNING IN A VIRTUAL MACHINE?     @1
         BNO   NOTLVL2             NO, BETTER NOT USE DIAGNOSE       @1
         HCPUSING VMDBK,R11  ADDRESSING THE VMDBK
         L     R3,VMDCFBUF   GET THE ADDRESS OF THE CONSOLE
*                            INPUT BUFFER; REFERENCE THE
*                            BUFFER WITH A GSDBK
         HCPDROP R11         NO LONGER ADDRESSING THE VMDBK
         HCPUSING GSDBK,R3   ADDRESSING THE GSDBK
         LH    R1,GSDSCAN    GET BYTE DISPLACEMENT TO START
         LA    R1,1(,R1)     Increment by one to account for space
         LH    R2,GSDDCNT    GET LENGTH OF DATA
         SR    R2,R1         Subtract length of command from total len
         BC    B'1100',GOTNONE    User error -- no input data
         LA    R1,GSDDATA(R1)     GET ADDRESS OF BYTE TO START
         HCPDROP R3          NO LONGER ADDRESSING THE GSDBK
         LR    R6,R1               Put addr of token in Rx for Diag 08
*** Begin changes for 5.2.0
         LR    R1,R2         Put length of input into R1
         C     R1,MAXLCMD    Is command too long?                    @1
         BH    TOOLONG       Yes                                     @1
         SRL   R1,3          Divide by 8 to convert bytes to Dwords
         LA    R1,1(,R1)     Increment by one to round up
         HCPGETST LEN=(R1),BACKING=BELOW2G   Get storage for input line
*        ST    R1,INBUFA     Save address for HCPRELST later         @2
         ST    R1,SAVEWRK0   Save address for HCPRELST later         @2
         BCTR  R2,0          Decrement length since MVC uses 1 less
         EX    R2,INMVC      MVC of text at R6 to R1
         LA    R2,1(,R2)     Increment to undo the BCTR above
         LRA   R6,0(,R1)     Replace R6 with real address of location
*                            where input data was copied to
         LA    R1,4000       Length of output buffer                 @1
         LR    R9,R1         ALSO L'RESPBUF TO RY+1 FOR DIAG 8       @1
         SRL   R1,3          CONVERT TO DOUBLEWORDS                  @1
         HCPGETST LEN=(R1),BACKING=BELOW2G  Get storage for output line
*        ST    R1,OUTBUFA    Save address for HCPRELST later         @2
         ST    R1,SAVEWRK1   Save address for HCPRELST later         @2
         LRA   R7,0(,R1)     Put real address of output buffer in R7
*        LA    R7,CPTALKS          Buffer for CP command response
*** End changes for 5.2.0
         LA    R8,X'40'            Tell Diag 08 to put output in buffer
         SLL   R8,24               Shift flag bits into high byte
         OR    R8,R2               Put length of token in Ry=R8
*        L     R0,KEEPR0           Recover R0                        @1
*        LA    R9,CPTALKSL         Length of buffer for cmd response @1
         DC    X'83',X'68',XL2'0008'   Diag 08 to invoke the command
         BZ    NOOVF               No Overflo Response fits in buffer@2
         L     R1,SAVEWRK1         Address of output buffer          @2
         LA    R1,3999(,R1)        Last possible buffer address      @2
FINDEOL  DS    0H                                                    @2
         CLI   0(R1),X'15'         Is that the last EOL?             @2
         BE    DISPLEN             Go set up display length and RC   @2
         BCT   R1,FINDEOL          Back up 1 byte                    @2
DISPLEN  DS    0H                                                    @2
         S     R1,SAVEWRK1         Distance from start to last EOL   @2
         LA    R9,1(,R1)           L'Data includes last byte (X'15') @2
         A     R8,THIRTY1K         +31K to Retcode: Buffer Overflow  @2
NOOVF    DS    0H                                                    @2
         LR    R4,R8               COPY 1ST LEVEL RC                 @1
         C     R8,PFX1             IS RESPONSE HCP001E?              @1
         BZ    UNKNCMD             Yes, go say so
*** Begin changes for 5.2.0
         L     R7,SAVEWRK1         HCPCONSL won't accept R1          @2
         HCPCONSL WRITE,                                               X
               DATA=((R7),(R9))                                      @1
*              DESTINATION=TERMINAL   Remove DEST, so PIPE can trap  @1
*        HCPCONSL WRITE,
*              DATA=(CPTALKS,(R9)),
*              DESTINATION=TERMINAL
*** End changes for 5.2.0
         B     PREEXIT
*        B     EXIT                                         // < 5.2.0
UNKNCMD  DS    0H
         HCPCONSL WRITE,                                               X
               DATA='??? Unknown CP command.',                         X
               DESTINATION=TERMINAL
         A     R4,THIRTYK          DISTINGUISH FROM NO LOCAL CMD     @1
         B     PREEXIT
*        B     EXIT                                         // < 5.2.0
NOTLVL2  DS    0H                                                    @1
         HCPCONSL WRITE,                                             @1*
               DATA='??? NOT RUNNING IN A SECOND LEVEL VM.',         @1*
               DESTINATION=TERMINAL                                  @1
         L     R4,THIRTYK          SPECIAL RC                        @1
         LA    R4,8(0,R4)          NOT 2ND LEVEL VM: RC=8            @1
         B     EXIT                                                  @1
TOOLONG  DS    0H                  COMMAND WAS > 240, TOO LONG.      @1
         HCPCONSL WRITE,                                             @1*
               DATA='??? DIAGNOSE 8 LIMITED TO 240 CHARACTERS',      @1*
               DESTINATION=TERMINAL                                  @1
         L     R4,THIRTYK          SPECIAL RC                        @1
         LA    R4,12(0,R4)         TOO LONG: RC=12                   @1
         B     EXIT                TOOLONG doesn't HCPRELST          @1
*                                                                    @1
GOTNONE  DS    0H                  No token found; report error
         HCPCONSL WRITE,                                               X
               DATA='??? No CP command found to pass to 1st level.',   X
               DESTINATION=TERMINAL
         SPACE 1
         L     R4,THIRTYK          SPECIAL RC                        @1
         LA    R4,4(0,R4)          NO CMD: RC=4                      @1
*** Begin changes for 5.2.0
         B     EXIT                GOTNONE doesn't HCPRELST
PREEXIT  DS 0H                     Release storage before exiting
         L     R1,SAVEWRK0   Retrieve address of text input temp area@2
         HCPRELST BLOCK=(R1)   RELEASE BUFFER
         L     R1,SAVEWRK1   Retrieve address of text output temp are@2
         HCPRELST BLOCK=(R1)   RELEASE BUFFER
*** End changes for 5.2.0
EXIT     DS 0H
*        XR    R6,R6               Return code of 0 no matter what!  @1
*        MVC SAVER15,(R4)                Store the RC                @1
         ST    R4,SAVER2                 Store the RC                @1
         HCPEXIT EP=(CP1STLIN),SETCC=0  Return
 
         HCPDROP R0
         HCPDROP R13
         SPACE 1
*
* Data areas
*
*****************************************************************
MAXLCMD  DC    F'240'                                                @1
THIRTYK  DC    F'30000'            30,000 CONSTANT FOR SPECIAL RCODES@1
THIRTY1K DC    F'31000'            31,000 CONSTANT FOR SPECIAL RCODES@2
* INBUFA   DS    F                   Input buffer location           @2
* OUTBUFA  DS    F                   Output buffer location          @2
INMVC    MVC   0(0,R1),0(R6)       Used by EX to copy input text
* CPTALKS  DS    200D              Room for 1600 characters // < 5.2.0
* CPTALKSL EQU   *-CPTALKS                                  //< 5.2.0
* CPTALKSL EQU   1600             Length in bytes of text output area@1
         HCPEPILG
