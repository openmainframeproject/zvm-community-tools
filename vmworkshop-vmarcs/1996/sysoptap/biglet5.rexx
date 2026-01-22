/* BIGLET REXX: This CMS Pipelines filter converts each line of input
into five output lines, containing the input translated to big 5x5
characters. Beware that output lines will be 6 times as long as the
input, and that there will be 5 times as many of them.
 
MODIFICATION HISTORY: */
/* BIGM EXEC started Saturday, 17 Mar 1984 14:16:26 by MW9      */
/*   Exec to sent a big message -  R. Kandhal                   */
/*   REVISED BY MSP   4/20/83    (quicker!)                     */
/*   Revised by K27   4/25/83    (Allow sEnd to a remote site)  */
/*   Revised by MW9   3/17/84    (Translated into REXX)         */
/*                               (Takes nicknames!)             */
/*                    3/20/84    (No need for 'BLOCKPS')        */
/*                    3/21/84    (Lower case letters!)          */
/*        getname proc courtesy of BSD                          */
/* 02/12/91 - Roger Deschner, UIC - convert to Pipelines filter. */
/* 04/02/93 - Roger Deschner, UIC - 5x5 letter version */
 
charstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
charstring = charstring||'~|@#$%^&*()-_=+!\:;''"{},./?<>'
charstring = charstring||'abcdefghijklmnopqrstuvwxyz'
bs.1 =       '  A   BBBB   CCCC DDDD  EEEEE '
bs.2 =       ' A A  B   B C     D   D E     '
bs.3 =       'A   A BBBB  C     D   D EEE   '
bs.4 =       'AAAAA B   B C     D   D E     '
bs.5 =       'A   A BBBB   CCCC DDDD  EEEEE '
 
bs.1 = bs.1||'FFFFF  GGGG H   H  III      J '
bs.2 = bs.2||'F     G     H   H   I       J '
bs.3 = bs.3||'FFF   G  GG HHHHH   I       J '
bs.4 = bs.4||'F     G   G H   H   I   J   J '
bs.5 = bs.5||'F      GGGG H   H  III   JJJ  '
 
bs.1 = bs.1||'K   K L     M   M N   N OOOOO '
bs.2 = bs.2||'K  K  L     MM MM NN  N O   O '
bs.3 = bs.3||'KKK   L     M M M N N N O   O '
bs.4 = bs.4||'K  K  L     M   M N  NN O   O '
bs.5 = bs.5||'K   K LLLLL M   M N   N OOOOO '
 
bs.1 = bs.1||'PPPP   QQQ  RRRR  SSSSS TTTTT '
bs.2 = bs.2||'P   P Q   Q R   R S       T   '
bs.3 = bs.3||'PPPP  Q Q Q RRRR  SSSSS   T   '
bs.4 = bs.4||'P     Q  QQ R  R      S   T   '
bs.5 = bs.5||'P      QQQQ R   R SSSSS   T   '
 
bs.1 = bs.1||'U   U V   V W   W X   X Y   Y '
bs.2 = bs.2||'U   U V   V W   W  X X   Y Y  '
bs.3 = bs.3||'U   U  V V  W W W   X     Y   '
bs.4 = bs.4||'U   U  V V  WW WW  X X    Y   '
bs.5 = bs.5||' UUU    V   W   W X   X   Y   '
 
bs.1 = bs.1||'ZZZZZ  000    1    222  33333 '
bs.2 = bs.2||'   Z   0 0   11   2   2    3  '
bs.3 = bs.3||'  Z   0   0   1     22    33  '
bs.4 = bs.4||' Z     0 0    1    2        3 '
bs.5 = bs.5||'ZZZZZ  000   111  22222 3333  '
bs.1 = bs.1||'   4  55555  666  77777  888  '
bs.2 = bs.2||'  44  5     6        7  8   8 '
bs.3 = bs.3||' 4 4  5555  6666    7    888  '
bs.4 = bs.4||'44444     5 6   6  7    8   8 '
bs.5 = bs.5||'   4  5555   666  7      888  '
 
bs.1 = bs.1||' 999   ~  ~   |   @@@@@  # #  '
bs.2 = bs.2||'9   9 ~ ~~    |   @ @ @ ##### '
bs.3 = bs.3||' 9999         |   @ @@@  # #  '
bs.4 = bs.4||'    9         |   @     ##### '
bs.5 = bs.5||' 999          |   @@@@   # #  '
 
bs.1 = bs.1||'$$$$$ %   %   ^    &&&  *   * '
bs.2 = bs.2||'$ $      %   ^ ^   & &   * *  '
bs.3 = bs.3||'$$$$$   %         &&&&  ***** '
bs.4 = bs.4||'  $ $  %          &  &   * *  '
bs.5 = bs.5||'$$$$$ %   %       &&&&& *   * '
 
bs.1 = bs.1||'  (    )                      '
bs.2 = bs.2||' (      )               ===== '
bs.3 = bs.3||' (      )   -----             '
bs.4 = bs.4||' (      )               ===== '
bs.5 = bs.5||'  (    )                      '
 
bs.1 = bs.1||'        !   \     '
bs.2 = bs.2||'  +     !    \    '
bs.3 = bs.3||'+++++   !     \   '
bs.4 = bs.4||'  +            \  '
bs.5 = bs.5||'        !       \ '
 
/* The following is NOT an error - double quotes to create single */
bs.1 = bs.1||' :::   ;;;   ''''   " "    {{{  '
bs.2 = bs.2||' :::   ;;;    ''          {    '
bs.3 = bs.3||'                        {     '
bs.4 = bs.4||' :::   ;;;               {    '
bs.5 = bs.5||' :::     ;               {{{  '
 
bs.1 = bs.1||' }}}                  / ????? '
bs.2 = bs.2||'   }                 /      ? '
bs.3 = bs.3||'    }               /     ??  '
bs.4 = bs.4||'   }    ,,   ..    /          '
bs.5 = bs.5||' }}}    ,    ..   /       ?   '
 
bs.1 = bs.1||'    < >      aaa  b           '
bs.2 = bs.2||'  <     >       a b      ccc  '
bs.3 = bs.3||'<         >  aaaa bbbb  c     '
bs.4 = bs.4||'  <     >   a   a b   b c     '
bs.5 = bs.5||'    < >      aaa  dbbb   ccc  '
 
bs.1 = bs.1||'    d         ff   ggg  h     '
bs.2 = bs.2||'    d  eee   f    g   g h     '
bs.3 = bs.3||' dddd eeeee fff    gggg hhhh  '
bs.4 = bs.4||'d   d e      f        g h   h '
bs.5 = bs.5||' dddd  eee   f       gg h   h '
 
bs.1 = bs.1||'  i       j k      ll         '
bs.2 = bs.2||'            k       l   mmmm  '
bs.3 = bs.3||' ii       j k  k    l   m m m '
bs.4 = bs.4||'  i   j   j kkk     l   m m m '
bs.5 = bs.5||' iii   jjj  k  kk  lll  m m m '
 
bs.1 = bs.1||'                              '
bs.2 = bs.2||'nnnn   ooo  pppp   qqqq rrrr  '
bs.3 = bs.3||'n   n o   o p   p q   q r     '
bs.4 = bs.4||'n   n o   o pppp   qqqq r     '
bs.5 = bs.5||'n   n  ooo  p         q r     '
 
bs.1 = bs.1||'                              '
bs.2 = bs.2||' sss    t   u   u v   v w   w '
bs.3 = bs.3||' s     ttt  u   u v   v w w w '
bs.4 = bs.4||'   s    t   u   u  v v  w w w '
bs.5 = bs.5||' sss    tt   uuuu   v    w w  '
 
bs.1 = bs.1||'                  '
bs.2 = bs.2||'x   x y   y zzzzz '
bs.3 = bs.3||' x.x   y y    zz  '
bs.4 = bs.4||' x^x    y    z    '
bs.5 = bs.5||'x   x  y    zzzzz '
 
SIGNAL ON ERROR
DO FOREVER                    /* Do until EOF */
  'READTO record'             /* Suck from pipe */
  num = LENGTH(record)
  ostr. = ''
  pos = 0
  DO i = 1 TO num
    letter = SUBSTR(record,i,1)
    letnum = index(charstring,letter)
    IF (letnum = 0) THEN DO  /* Not found? Insert blank. */
      pos = pos + 6
    END
    ELSE DO   /* Move in letter. */
      ipos = (((letnum - 1) * 6 ) + 1)
      DO j = 1 TO 5
        ostr.j = LEFT(ostr.j,pos) || SUBSTR(bs.j,ipos,6)
      END
      pos = pos + 6
    END
  END
 
  /* Output the string */
 
  DO j = 1 TO 5
    'OUTPUT' ostr.j             /* Blow into pipe */
  END
END
 
ERROR: EXIT rc*(rc<>12)       /* On normal eof, set rc=0 */
