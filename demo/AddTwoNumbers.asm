// Usage: RAM[2] = RAM[1] + RAM[0]

    @0
    D=M

    @1
    D=D+M

    @2
    M=D

    @6
    0;JMP