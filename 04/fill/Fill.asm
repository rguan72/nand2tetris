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

    @i
    M=0 // i=0

    // go to end if i >= 8192
(LOOP)
    @i
    D=M
    @8192
    D=D-A
    @END
    D;JGE 

    // M[screen + i] = -1
    @i
    D=M
    @SCREEN
    A=D+A
    M=-1

    // i++
    @i
    M=M+1

    @LOOP
    0;JMP

(END)
    @END
    0;JMP
