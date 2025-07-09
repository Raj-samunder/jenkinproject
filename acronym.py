
# Acronym program
# Taking input from user
user_input = str(input("Enter a Sentence: ")) 

# Making list of words
text = user_input.split()

# Creating empty string
a = " "

# Accessing each word one by one using for loop
for i in text:
    # Taking first letter of word and converting to uppercase
    a = a + str(i[0]).upper()

# Printing acronym
print(a)
