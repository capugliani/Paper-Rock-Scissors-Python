alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

program_running = True

while program_running == True:

    direction_ok = False
    while direction_ok != True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode':
            direction_ok = True
        elif direction == 'decode':
            direction_ok = True
        else:
            print("Sorry, but i didn't understand if you want to encode or decode!")
            direction_ok = False

    text = input("Type your message:\n").lower()

    shift_is_number = False
    while shift_is_number != True:
        shiftcheck = input("Type the shift number:\n")
        if shiftcheck.isdigit():
            shift = int(shiftcheck)
            shift_is_number = True
        else:
            print("Please, only numbers is allowed in shifting function")
            shift_is_number = False

    reseting_shift = 1
    full_loops = 0

    for shift in range(1, shift+1):
        if reseting_shift == 27:
            reseting_shift = 1
            full_loops += 1
        reseting_shift += 1
    fixing_number = shift - (full_loops * 26)

    def encrypt(text_function, shift_function):
        encrypt_counting = 0
        crypto_list = []
        encrypting_text = list(text_function)

        for item in encrypting_text:
            letter_counting = 0
            for letter in alphabet:
                if encrypting_text[encrypt_counting] == alphabet[letter_counting]:
                    if letter_counting+shift_function >= 26:
                        actual_letter = letter_counting + shift_function - 26
                        crypto_list.append(alphabet[actual_letter])
                    else:
                        crypto_list.append(alphabet[letter_counting + shift_function])
                letter_counting += 1
                if letter_counting == 26:
                    checking_strings = 0
                    for letter in alphabet:
                        if letter != item:
                            checking_strings += 1
                        if checking_strings >= 26:
                            crypto_list.append(item)
            encrypt_counting += 1
        print_crypt = ''.join(crypto_list)
        print(print_crypt)

    def decrypt(text_function, shift_function):
        decrypt_counting = 0
        decrypto_list = []
        decrypting_text = list(text_function)

        for item in decrypting_text:
            letter_counting = 0
            for letter in alphabet:
                if decrypting_text[decrypt_counting] == alphabet[letter_counting]:
                    if letter_counting - shift_function <= 0:
                        actual_letter = letter_counting - shift_function + 26
                        decrypto_list.append(alphabet[actual_letter])
                    else:
                        decrypto_list.append(alphabet[letter_counting - shift_function])
                letter_counting += 1
                if letter_counting == 26:
                    checking_strings = 0
                    for letter in alphabet:
                        if letter != item:
                            checking_strings += 1
                        if checking_strings >= 26:
                            decrypto_list.append(item)
            decrypt_counting += 1
        print_decrypt = ''.join(decrypto_list)
        print(print_decrypt)


    if direction == 'encode':
        encrypt(text_function=text, shift_function=fixing_number)
    elif direction == 'decode':
        decrypt(text_function=text, shift_function=fixing_number)
    else:
        print("Sorry, but i didn't understand if you want to encode or decode!")

    running_question = True
    while running_question == True:
        running_question = input("Do you want to keep the program running?\nType 'yes' or 'no': ").lower()
        if running_question == 'yes':
            program_running = True
            running_question = False
        elif running_question == 'no':
            program_running = False
            running_question = False
        else:
            print("Sorry, You have to type 'yes' or 'no'")
            running_question = True