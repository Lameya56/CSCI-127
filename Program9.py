#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 9, 2022
#This program prints cipher
import string
plain_text = input ("Enter an all-small-letter string: ")
shift = int(input("Enter a non-negative int to shift: "))
alphabet = string.ascii_lowercase
shifted = alphabet[shift:]+ alphabet[:shift]
table = str.maketrans(alphabet,shifted)
encrypted = plain_text.translate(table)
print("ciphered string: " + encrypted)