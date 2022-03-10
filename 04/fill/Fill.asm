// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
// Put your code here.
// 256 rows, 512 columns
// 256 rows, 512/16=32 words per row. 256*32=8192 words in screen (8192 * 16 pixels)

(WHILELOOP)
    @i
    M=0 // i=0

    // if(key pressed) R0 = 1 else R0 = 0
    @KBD
    D=M
    @IFNOKEYPRESSED
    D;JEQ

    @R0
    M=1 // R0 = 1
    @LOOP
    0;JMP

(IFNOKEYPRESSED)
    @R0
    M=0 // R0 = 0

    // go to end if i >= 8192
(LOOP)
    @i
    D=M
    @8192
    D=D-A
    @END
    D;JGE 

    // if R0 = 1 blacken screen else whiten
    @R0
    D=M
    @ELSE
    D;JEQ

    // M[screen + i] = -1
    @i
    D=M
    @SCREEN
    A=D+A
    M=-1

    @ENDIF
    0;JMP

(ELSE)
    // M[screen + i] = 0
    @i
    D=M
    @SCREEN
    A=D+A
    M=0

(ENDIF)
    // i++
    @i
    M=M+1

    @LOOP
    0;JMP

    // go to top level while loop
(END)
    @WHILELOOP
    0;JMP
