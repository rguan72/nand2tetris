// push argument 1
    @ARG
    D=M
    @1
    A=D+A
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
// pop pointer 1
    @THIS
    D=A
    @1
    D=D+A
    @R13
    M=D
    @SP
    M=M-1
    A=M
    D=M
    @R13
    A=M
    M=D
// push constant 0
    @0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// pop that 0
    @0
    D=A
    @THAT
    D=M+D
    @R13
    M=D
    @SP
    M=M-1
    A=M
    D=M
    @R13
    A=M
    M=D
// push constant 1
    @1
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
// pop that 1
    @1
    D=A
    @THAT
    D=M+D
    @R13
    M=D
    @SP
    M=M-1
    A=M
    D=M
    @R13
    A=M
    M=D
// push argument 0
    @ARG
    D=M
    @0
    A=D+A
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 2
    @2
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
// pop argument 0
    @0
    D=A
    @ARG
    D=M+D
    @R13
    M=D
    @SP
    M=M-1
    A=M
    D=M
    @R13
    A=M
    M=D
(FibonacciSeries.MAIN_LOOP_START)
// push argument 0
    @ARG
    D=M
    @0
    A=D+A
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
// if-goto COMPUTE_ELEMENT
    @SP
    M=M-1
    A=M
    D=M
    @FibonacciSeries.COMPUTE_ELEMENT
    D;JNE
// goto END_PROGRAM
    @FibonacciSeries.END_PROGRAM
    0;JMP
(FibonacciSeries.COMPUTE_ELEMENT)
// push that 0
    @THAT
    D=M
    @0
    A=D+A
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push that 1
    @THAT
    D=M
    @1
    A=D+A
    D=M
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
// pop that 2
    @2
    D=A
    @THAT
    D=M+D
    @R13
    M=D
    @SP
    M=M-1
    A=M
    D=M
    @R13
    A=M
    M=D
// push pointer 1
    @THIS
    D=A
    @1
    A=D+A
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 1
    @1
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
// pop pointer 1
    @THIS
    D=A
    @1
    D=D+A
    @R13
    M=D
    @SP
    M=M-1
    A=M
    D=M
    @R13
    A=M
    M=D
// push argument 0
    @ARG
    D=M
    @0
    A=D+A
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
// push constant 1
    @1
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
// pop argument 0
    @0
    D=A
    @ARG
    D=M+D
    @R13
    M=D
    @SP
    M=M-1
    A=M
    D=M
    @R13
    A=M
    M=D
// goto MAIN_LOOP_START
    @FibonacciSeries.MAIN_LOOP_START
    0;JMP
(FibonacciSeries.END_PROGRAM)
