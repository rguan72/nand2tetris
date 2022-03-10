// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

// prod = 0
    @prod
    M=0

// i = R1
    @R1
    D=M
    @i
    M=D

// if i == 0 go to ENDLOOP
(LOOP)
    @i
    D=M
    @ENDLOOP
    D;JEQ

// prod += R0
    @R0
    D=M
    @prod
    M=D+M

// i -= 1
    @i
    M=M-1

// jump to LOOP
    @LOOP
    0;JMP

(ENDLOOP)
    // R2 = prod
    @prod
    D=M
    @R2
    M=D

(END)
    @END
    0;JMP
