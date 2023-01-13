#Name: Lameya Mostafa
#Email: Lameya.mostafa18@myhunter.cuny.edu
#Date: September 12, 2022
#This program prints reverse, uppercase and abbreviation

user_input = input("input: ")
reverse = user_input[::-1]
print("user reverse: " + reverse)
print("user reverse upper: " + reverse.upper())
def fxn(stng):

	# get all words
	lst = stng.split()
	oupt = ""
	
	# iterate over words
	for word in lst:
	
		# get first letter of each word
		oupt += word[0]
		
	# uppercase oupt
	oupt = oupt.upper()
	return oupt

# output acronym
print("user abbreviation: "+fxn(user_input))
