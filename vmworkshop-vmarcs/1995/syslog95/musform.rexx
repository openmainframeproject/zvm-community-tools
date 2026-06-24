/* Format MUSIC bad password report */
 
SIGNAL ON ERROR
 
DO FOREVER
  'readto in'
  SELECT                         /* format output line */
     WHEN POS('MUSICA',in) ^= 0
       THEN 'callpipe',
              '  var in',
              '| specs 12.7 1.7 5.6 9.6 5.6 16.6 /0/ 28.1 /0/ 35.1',
              '| *:'
     WHEN POS('MUSICB',in) ^= 0
       THEN 'callpipe',
              '  var in',
              '| specs 12.7 1.7 5.6 9.6 /0/ 21.1 5.6 23.6 /0/ 35.1',
              '| *:'
     WHEN POS('MUSICF',in) ^= 0
       THEN 'callpipe',
              '  var in',
              '| specs 12.7 1.7 5.6 9.6 /0/ 21.1 /0/ 28.1 5.6 30.6',
              '| *:'
     OTHERWISE,
            'callpipe',
              '  var in',
              '| specs 12.7 1.7 5.6 9.6 /*** Unknown system/ 37 20.6 nw',
              '| *:'
  END
END
 
error:
IF RC = 12 THEN RC = 0
EXIT RC
