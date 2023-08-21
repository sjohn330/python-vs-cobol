       IDENTIFICATION DIVISION.
       PROGRAM-ID. "SORT".

       ENVIRONMENT DIVISION.
           INPUT-OUTPUT SECTION.
               FILE-CONTROL.
               SELECT ARRVALUES ASSIGN TO 'py_vs_X_assign2.txt'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
           FILE SECTION.
           FD ARRVALUES.
           01 ARR-FILE.
               05 ARR-VALUE PIC 9(6).

           WORKING-STORAGE SECTION.
           01 ARR PIC S9(6) OCCURS 500000 TIMES INDEXED BY ARRINDEX.
           01 ARRAYSIZE PIC 9(6) VALUE 1.
           01 TEMP PIC 9(6) VALUE 000.
           01 I PIC 9999 VALUE 0.
           01 J PIC 9999 VALUE 1.
           01 WS-ARRVALUES.
               05 WS-NUMVALUE PIC 9(6).
           01 WS-EOF PIC A(1).

       PROCEDURE DIVISION.
           OPEN INPUT ARRVALUES.
           PERFORM UNTIL WS-EOF = 'Y'
               READ ARRVALUES INTO WS-NUMVALUE
               AT END MOVE 'Y' TO WS-EOF
               NOT AT END
                   MOVE WS-NUMVALUE TO ARR(ARRAYSIZE)
                   ADD 1 TO ARRAYSIZE
           end-read
           end-perform.
           CLOSE ARRVALUES.

      *   SET ARRAYSIZE TO 5000

      * Bubble sort method.
           MOVE 1 TO I.
           PERFORM UNTIL I > ARRAYSIZE
           MOVE I TO J
               PERFORM UNTIL J > ARRAYSIZE
                 IF (ARR(I) < ARR(J))
                   MOVE ARR(J) TO TEMP
                   MOVE ARR(I) TO ARR(J)
                   MOVE TEMP TO ARR(I)
                 END-IF
               ADD 1 TO J GIVING J
               END-PERFORM
           ADD 1 TO I GIVING I
           END-PERFORM.

           DISPLAY "AFTER SORTING:"
           MOVE 0 TO I.
           PERFORM UNTIL I = 100
           ADD 1 TO I  
           DISPLAY  ARR(I)
           END-PERFORM.
       
       STOP RUN.
       END PROGRAM SORT.