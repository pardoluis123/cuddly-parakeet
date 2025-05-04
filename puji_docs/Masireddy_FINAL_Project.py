
####This file is an old Python script that I used to test the Streamlit UI. The Streamlit UI successfully read this file, suggested improvements, and output a file with those suggestions. 

#Puji Masireddy
#COMP112-02
#Hangman Project Final
#12/16/23

"""
1. What were the 3 goals?
My goals were to become more familiar with using turtle, to become better at using while loops, and to code a play-able game.

Were the goals met? Yes

2. How does this project illustrate your mastery of Python?
I demonstrated how to use turtle to build a stick figure body; I used while loops and if statements; I also utilized a dictionary for my word bank. 

3. What have you learned from doing this project?
I learned how to debug efficiently by sectioning my code; I learned how to embed functions, and how to use turtle graphics. 
"""

#Imports

import turtle
import random

#Functions for the scaffold and body parts

def scaffold():
    """
    sig: none -> none
this function draws the hangman scaffold
    """
    turtle.hideturtle()
    turtle.color('green')
    turtle.pensize(10)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(20)

def head(): 
    """
    sig: none-> none
this function draws the hangman head"""

    turtle.penup()
    turtle.right(190)
    turtle.forward(1)
    turtle.left(90)
    turtle.pendown()
    turtle.color('purple')
    turtle.pensize(10)
    turtle.circle(30)


def body():
    """
    sig: none-> none
this functions draws the hangman body
    """
    turtle.penup()
    turtle.left(100)
    turtle.forward(60)
    turtle.pendown()
    turtle.color('purple')
    turtle.pensize(10)
    turtle.forward(100)

def right_leg():
    """
    sig: none->none
this function draws hangman right leg"""

    turtle.left(40)
    turtle.pendown()
    turtle.color('purple')
    turtle.pensize(10)
    turtle.forward(50)

def left_leg():
    """
    sig: none->none
this function draws left leg"""

    turtle.penup
    turtle.right(180)
    turtle.forward(50)
    turtle.pendown()
    turtle.right(260)
    turtle.color('purple')
    turtle.pensize(10)
    turtle.forward(50)

def left_arm():
    """
    sig: none->none
this function draws left arm"""

    turtle.penup
    turtle.right(180)
    turtle.forward(50)
    turtle.left(40)
    turtle.forward(50)
    turtle.right(270)
    turtle.pendown()
    turtle.color('purple')
    turtle.pensize(10)
    turtle.forward(50)

def right_arm():
    """
    sig: none->none
this function draws right arm"""

    turtle.right(180)
    turtle.forward(100)
    turtle.color('purple')
    turtle.pensize(10)
    
#window=turtle.Screen()
#scaffold()
#head()
#body()
#right_leg()
#left_leg()
#left_arm()
#right_arm()
#turtle.done()


#######

def draw_hangman(nwrong):
    """
    sig: int->none
this function draws hangman body part corresponding to number wrong
    """
#nwrong is counter for missed guesses, then call draw hangman

    if nwrong==1:
        head()
    elif nwrong==2:
        body()
    elif nwrong==3:
        right_leg()
    elif nwrong==4:
        left_leg()
    elif nwrong==5:
        left_arm()
    else:
        right_arm()

def draw_man():
    """
    sig: none-> none
this function runs draw_hangman to draw the whole hangman. for testing."""
    head()
    body()
    right_leg()
    left_leg()
    left_arm()
    right_arm()
#turtle.done()
   

def setup_turtle():
    """
    sig: none-> none
this function sets up game"""
    window=turtle.Screen()
    scaffold()
    
#choose a word

def select_word(wordbank):
     """
    sig: list ->list[str]
this function returns a random word from the wordbank and breaks out as a list"""
#get random number generator
#ex "blue" into ['b', 'l'...]

wordbank=['wesleyan','cardinal','exley','olin','usdan','scili', 'picafe', 'foss', 'study',
'wesshop', 'westco', 'clark', 'bennett', 'fauver', 'woodframe', 'nics', 'highrise', 'lowrise',
'butterfields', 'summies', 'hewitt', 'middletown', 'fisk', 'boger', 'judd', 'swings', 'redandblack',
'freeman', 'zilkha', 'allbritton', 'davison', 'weswell', 'downey', 'writersblock', 'xhouse', 'espwesso',
'northcollege', 'southcollege']
x = random.randint(0,len(wordbank)-1) 
y = 0

word = wordbank[x]
#set is because if yellow was the word, a list would only remove one L and not both L's
dictionary = set(word) 

"""example python output:
yellow
['y', 'e', 'l', 'l', 'o', 'w']
"""

currentguess = "_ "* len(word)
alreadyguessedletters = []

print ("Let's play a game! Wesleyan-themed Hangman!")
(draw_hangman(0))
print(currentguess)


def isvalid(guess):
    """
    sig: str -> Bool
this function validates input guess. Returns True if it is a single alphabetic character."""
  
nwrong=0

setup_turtle()

while len(dictionary) >0 and nwrong < 6:
    print ("You have already guessed " + str(nwrong) + " times")
    print ("You have already guessed the following letters:" + ", ".join(alreadyguessedletters))
    guess = input("Please enter a single Letter:")

    
    if len(guess)==1 and guess.isalpha()==False:
        print ('Please enter a letter!')

    elif len(guess)!=1:
        print ('Please enter only one character at time!')

    elif len(guess)==1 and guess.isalpha()==True:
        if guess in alreadyguessedletters:
            nwrong += 1
            draw_hangman(nwrong)
            print ('You have already guessed this letter, please choose a different letter')
        elif guess in word:
            print ('You have guessed a correct letter')
            alreadyguessedletters.append(guess)
            dictionary.remove(guess)

            currentguess = ""
            for letter in word:
                if letter in alreadyguessedletters:
                    currentguess += letter + " "
                else:
                    currentguess += "_ "
        else:
            print ('You have guessed incorrectly, please try again')
            nwrong += 1
            draw_hangman(nwrong)
            if guess not in alreadyguessedletters:
                alreadyguessedletters.append(guess)

        print(currentguess)
        print(f'Attempts remaining: {6-nwrong}')

    if len(dictionary) == 0:
        print('Congrats! You won!')
    elif nwrong == 6:
        print('Sorry, you lost, thanks for playing!')



