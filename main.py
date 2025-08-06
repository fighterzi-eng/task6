import word_selector
import text_colourer
import iterator
import logic
import input_handler
import random
resume="y"
while resume=="y":
    tries=6
    prev_answers=[]
    word=word_selector.word_selector
    while tries >0:
        x=logic.game(word,input_handler.take_input)
        if x==text_colourer.colouring("g",word):
            print("you won")
            break
        else:
            prev_answers.apppend(x)
            ties-=1
            print("incorrect try again")
            print("you have"+str(tries)+"tries left")
            print("your previous answers are:")
            print("////////////////////////////////")
            iterator.previous_answers(prev_answers)
            print("////////////////////////////////")
            if tries==0:
                print("you lost")
                print("the word was"+word)
                break
    resume=input("would u like to play again,type y for yes ")
print("Thank you for playing")