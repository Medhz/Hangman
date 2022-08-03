import random
# from os import system, name
  
# # import sleep to show output for some time period
# from time import sleep
  
# # define our clear function
# def clear():
  
#     # for windows
#     if name == 'nt':
#         _ = system('cls')
  
#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')
  
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list=["ardvark","baboon","camel"]
word=random.choice(word_list)
print("you have 6 chances")
#print(word)
lives=6
print(stages[lives])


blanks=['_']*len(word)
print(f"{' '.join(blanks)}")
while '_' in blanks:
 ch=input("guess a letter: ").lower()
 if ch not in word:
     lives-=1
 print(stages[lives])
 

 for n in range(len(word)):
    if word[n]==ch:
        blanks[n]=ch
 print(f"{' '.join(blanks)}")
 if lives==0:
     print("You lost all your lives")
     break
 #sleep(3)
 #clear()
 
 #print(lives)   
 #print(blanks)
 
 
if lives==0:
    print("you loose")
else:
    print("you win")

