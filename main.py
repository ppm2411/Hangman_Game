import random
import words
import hangman_art

#converting a list into a string to display it
def list_str(l):
    a="".join(l)
    return a

# Introduction to the game to the user
print("WELCOME TO HANGMAN GAME")
print('''
.......................%@$$$$$$$$$$$$$$$$$$$$$@!................................
.......................@%:::::::::::::.......:@$................................
.......................@*..................!$$$@@!..............................
.......................@*.................:&!...!@%.............................
.......................@*.................*&.....$$.............................
.......................@*.................!&:..:%@:.............................
.......................@*..................*$$@$*...............................
.......................&!....................*&.................................
......................:#:....................%@:!!*%!...........................
......................!&.....................$#%%**!:...........................
......................*@.....................$%.................................
......................$$.....................&*.................................
......................@*....................:#:.................................
......................&!...................!$#%:................................
......................&:................:*@$!:*@%:..............................
.....................:#:...............%@%:....:%@*.............................
.....................:#................!:........:%:............................
.....................!&.........................................................
.....................:#.........................................................
........*$$$%%%%%%%%%$&$%%%%%%%%%%%%%...........................................
..........:::::::::::::::::::!!!!!!::...........................................
................................................................................
................................................................................
''')

print(hangman_art.hgmn)
print(''' 
      A word is choosen. You have to choose a letter. If the letter is not present in the word, 
      you would loose a life.You have to guess all the letters in the word. 
      Remember you only have 6 lives.
      ''')

# Choosing a random word
choosen_word=random.choice(words.w)
copied_word=choosen_word

# converting the word into a list
l1=list(choosen_word)

# creating another list with as many as blankspaces as letters in the word
blank=[]
for i in l1:
    blank.append("_")

# life given to the user
life=6
stg=6
# taking guessed letter from user
while life>0:
    print(hangman_art.stages[stg])
    guess=input("Guess a letter ")
    guess=guess.lower()
    if guess in copied_word:
        pos=copied_word.find(guess)
        blank[pos]=guess
        print(list_str(blank))
        copied_word=copied_word.replace(guess,"_",1)
    else:
        life=life-1
        stg=stg-1
        print(f"You have lost a life. You have currently {life} lives")
    if life == 0:
        print(f"You lost. You have exhausted all of your lives. The word was {choosen_word}. You can try again.")
        print(hangman_art.stages[stg])
        break
    if list_str(blank)==choosen_word:
        print("You won! Congratulations. Thank you for playing.")
        break
    

