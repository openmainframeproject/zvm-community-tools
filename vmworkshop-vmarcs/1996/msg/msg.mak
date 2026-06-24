# 
#	  Name: msg.mak (make file) 
#		makefile for MSG package: tell, msgcat, msgd 
#	Author: Rick Troth, Houston, Texas, USA 
#	  Date: 1996-Mar-25 (Oscar night), cut from main "makefile" 
# 
 
default:	tell msgcat msgd  
 
msgcat: 	msg.mak msgcat.o putline.o 
		cc -o msgcat msgcat.o putline.o 
		strip msgcat 
 
msgd:		msg.mak msgd.o putline.o tcpio.o 
		cc -o msgd msgd.o putline.o tcpio.o 
		strip msgd 
 
tell:		msg.mak msgc.o msgcmsp.o msgcuftd.o msglocal.o \
			getline.o tcpio.o userid.o putline.o 
		cc -o tell msgc.o msgcmsp.o msgcuftd.o msglocal.o \
			getline.o tcpio.o userid.o putline.o 
		strip tell 
 
msgcmsp.o: 	msg.mak msghndlr.h msgcmsp.c 
		cc -c msgcmsp.c 
 
msgcuftd.o:	msg.mak msghndlr.h msgcuftd.c 
		cc -c msgcuftd.c 
 
msglocal.o:	msg.mak msghndlr.h msglocal.c 
		cc -c msglocal.c 
 
install:	tell msgcat msgd 
		mv tell msgcat /usr/local/bin/. 
		mv msgd /usr/local/etc/. 
 
clean:
		rm -f *.o *.a core a.out tell msgcat msgd 
 
 
