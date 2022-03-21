// push constant 17
    @17
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 17
    @17
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// eq
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @EQUAL2
    D;JEQ
    @SP
    A=M-1
    M=0
(EQUAL2)
// push constant 17
    @17
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 16
    @16
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// eq
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @EQUAL5
    D;JEQ
    @SP
    A=M-1
    M=0
(EQUAL5)
// push constant 16
    @16
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 17
    @17
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// eq
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @EQUAL8
    D;JEQ
    @SP
    A=M-1
    M=0
(EQUAL8)
// push constant 892
    @892
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 891
    @891
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// lt
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @LT11
    D;JLT
    @SP
    A=M-1
    M=0
(LT11)
// push constant 891
    @891
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 892
    @892
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// lt
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @LT14
    D;JLT
    @SP
    A=M-1
    M=0
(LT14)
// push constant 891
    @891
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 891
    @891
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// lt
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @LT17
    D;JLT
    @SP
    A=M-1
    M=0
(LT17)
// push constant 32767
    @32767
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 32766
    @32766
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// gt
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @GT20
    D;JGT
    @SP
    A=M-1
    M=0
(GT20)
// push constant 32766
    @32766
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 32767
    @32767
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// gt
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @GT23
    D;JGT
    @SP
    A=M-1
    M=0
(GT23)
// push constant 32766
    @32766
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 32766
    @32766
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// gt
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    D=M-D
    M=-1
    @GT26
    D;JGT
    @SP
    A=M-1
    M=0
(GT26)
// push constant 57
    @57
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 31
    @31
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 53
    @53
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// add
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    M=M+D
// push constant 112
    @112
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// sub
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    M=M-D
// neg
    @SP
    A=M-1
    D=M
    M=-D
// and
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    M=M&D
// push constant 82
    @82
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// or
    @SP
    M=M-1
    A=M
    D=M
    @SP
    A=M-1
    M=M|D
// not
    @SP
    A=M-1
    D=M
    M=!D
