#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: November 22, 2022
#This program loops from 0 to 100



ADDI $s0, $zero, 0
ADDI $s1, $zero, 5
ADDI $s2, $zero, 100
AGAIN: ADD $s0, $s0, $s1
BEQ $s0, $s2, DONE
J AGAIN
DONE: