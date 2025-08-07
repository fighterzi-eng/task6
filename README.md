# task6
wordle game
input handler:


contains the function that takes input from the user and checks wether its valid or not(in terms of lenght only) 
if its not valid it will continue to request input from the user.


iterator:


it just iretates over a given list.


text colourer:


colours the given string with the given colour(red,green,yellow).
word selector:it transforms the text file into a list then returns a random item from the list


logic:

take two word(guess, word),it compares each letter in the guess with the corresponing letter in the word if this case rturns false it will check wether the letter is present in the word or not
and based on the result it will give each letter a certain colour and add it to a variable,in the end it will return this variable which contains the coloured answer(guess). 


main:


this contains the main game with an added play again option depending on a variable(while condition) it chooses a random word from the list and takes input from the user
then puts the in the game logic then compares it with the coloured version of the chosen word(because coloured text doesnt equal uncoloured text even if its the same) if this case returns true then the program breaks the inner while loop and you win otherwise the output of the logic function is saved to the list that contains all the previos answers from the user,the tries counter decreases by one,and the the previos answers list is iterated through printing each value this loop continues until the user runs out of trails 











