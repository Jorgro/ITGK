løsning = 'løsningsforslag'
def hangman_med_herman(løsning):
    ord = list(løsning)
    blank = "_" * len(ord)
    blank = list(blank)
    gale = 6
    while gale > 0:
        if blank == ord:
            print(f'Du vant! Ordet var {løsning}')
            break
        else:
            print("\nDu har {} sjanser igjen.".format(gale)
              + "\nOrdet ditt: " + "".join(blank))
            bokstav = input('Din gjetning: ').lower()
            if bokstav in ord:
                for index, karakter in enumerate(ord):
                    if karakter == bokstav:
                        blank[index]=bokstav
            elif bokstav not in ord:
                gale -= 1
                print('Du har mistet et liv! Prøv igjen!')
    else:
        print('You ded')
hangman_med_herman(løsning)
















# word = "hus"
# word_list = list(word)
# guess_list = []
# # for i in range(len(word)):
# #     guess_list.append("_")

# while word_list != guess_list:
#     blanks = "_" * len(word)
#     print(guess_list)
#     guess = input("Bokstav: ")
#     if guess in word_list:
#         for index, character in enumerate(word_list):
#             blanks =list(blanks)
#             if character == guess:
#                         blanks[index] = guess
#                         current = "".join(blanks)
#                         if blanks == word_list:
#                             print("\n\nCONGRATULATIONS, YOU WON!!\nYour word was " + ''.join(word) + ".\n")


# print("You won! The word was:", word)
