import random
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_characters = '!@#$%&*?'
uppercaseLetter1 = random.choice(letters)
uppercaseLetter2 = random.choice(letters)
lowercaseLetter1 = random.choice(letters.lower())
lowercaseletter2 = random.choice(letters.lower())
digit1 = str(random.randrange(0, 9))
digit2 = str(random.randrange(0, 9))
punctuationSign1 = random.choice(special_characters)
punctuationSign2 = random.choice(special_characters)

password =(uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseletter2  + digit1 + digit2 + punctuationSign1 + punctuationSign2)
password = ''.join(random.sample(password, len(password)))
print(f' Your new password is : {password}')