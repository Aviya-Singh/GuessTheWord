#Import random module
import random

print("Welcome to the Guess my Word App!!!")

game_dict={"colors":['orange', 'yellow', 'purple', 'acquamarine', 'violet', 'gold'], 
           "sports":['basketball', 'football', 'baseball', 'soccer', 'tennis', 'curling'], 
           "fruits":['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'], 
           "classes": ['english', 'science', 'mathematics', 'history', 'art', 'health']}

#print(game_dict["colors"])

game_category=[]

for key in game_dict:
    game_category.append(key)
#print(game_category)

playing=True
while playing:
    mycategory=random.choice(game_category)
    #print(mycategory)
    guess_word=(random.choice(game_dict[mycategory]))

    print(f"Guess a {len(guess_word)} letter word from the following category: {mycategory}")

    blank_word=[]
    for i in range(len(guess_word)):
        blank_word.append("-")

    print("".join(blank_word))

    #We need to ask user to guess the word --> game word...in how many guesses user has guessed

    guess=''
    guess_count=0

    while guess!=guess_word:
        guess=input("\n Enter your guess: ").lower()
        guess_count=guess_count+1
        if guess==guess_word:
            print(f"Correct!! You guessed the word in {guess_count} guesses!")
            break
        else:
            print("Incorrect!! Let us reveal a letter to help you!!")
            #random index from the game word
            index_val=random.randint(0,len(guess_word)-1)
            if blank_word[index_val]=="-":
                blank_word[index_val]=guess_word[index_val]
                print("".join(blank_word))
    choice=input("\n Do you wish to play again(Y/N)? ").upper()
    if choice!='Y':
        playing=False