message = "GUVF VF ZL FRPERG ZRFFNTR"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# loop through every possible key
for key in range(len(LETTERS)):

    # it is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared
    translated = ""

    # the rest of the program is the same as the original caesar cypher
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)  # find the number of the symbol
            num = num - key

            # handle the wrap-around if number is greater than 26 or less than
            # 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol to the translated message
            translated = translated + LETTERS[num]

        else:
            # just add the symbol if it isn't contained in letters
            translated = translated + symbol

    # display the current key being decrypted and the translated message
    print("Key " + str(key) + " -- Message: " + translated)
