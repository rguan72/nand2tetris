#!/bin/bash

for fName in BasicTest PointerTest SimpleAdd StackTest StaticTest
do 
    echo "Testing $fName"
    python ../main.py $fName.vm $fName.out.asm
    diff $fName.out.asm $fName.asm
done

echo "ALL TESTS COMPLETE"

# cleanup
for fName in BasicTest PointerTest SimpleAdd StackTest StaticTest
do
    rm $fName.out.asm
done
