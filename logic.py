import text_colourer
def game(word,guess):
    ur_answer=""
    for i in range(0,len(guess)):
        if word[i]==guess[i]:
            ur_answer+=text_colourer.colouring("g",guess[i])
        elif guess[i] in word:
            ur_answer+=text_colourer.colouring("y",guess[i])
        else:
            ur_answer+=text_colourer.colouring("r",guess[i])

    return ur_answer

