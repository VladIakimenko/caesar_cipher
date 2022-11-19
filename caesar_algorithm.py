languages = {
    'english': {
        'lower': 'abcdefghijklmnopqrstuvwxyz',
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
               },
    'russian': {
        'lower': 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
        'upper': 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
               }
            }


def add_custom_alpha(name, lower, upper):
    """
    1) The function checks if newly entered alphabet has symbols that
    coincide with existing alphas;
    2) if it does, function replaces the existing alphabet with newly entered
    3) adds newly entered alphabet to the existing structure where:

    name - is the name of the new alphabet (may be helpful if saved to file)
    lower - line with lower case symbols
    upper - line with UPPER CASE symbols

    Function returns None
    """
    for language, case_dicts in languages.items():
        break_flag = False
        for value in case_dicts.values():
            for c in lower + upper:
                if c in value:
                    del languages[language]
                    break_flag = True
                    break
            if break_flag:
                break
        if break_flag:
            break

    new_dict = {'lower': lower, 'upper': upper}
    languages[name] = new_dict


def encrypt(phrase, rot):
    decoded_phrase = ''
    for c in phrase:
        found_char = False
        if c in ''' ,.:-!;'"?''':
            decoded_phrase += c
            found_char = True
        else:
            for language in languages.values():
                for value in language.values():
                    if c in value:
                        decoded_phrase += (value[value.index(c) + rot]
                            if value.index(c) + rot < len(value)
                            else value[value.index(c) - (len(value) - rot)])
                        found_char = True
                        if abs(rot) == len(value):
                            rot = 0

    # ord() alternative - less attractive for me since we're bound to Unicode and can't use custom alphabets:
            # if ord(c) in range(97, 123):
            #     if 97 <= ord(c) + rot <= 122:
            #         decoded_phrase += (chr(ord(c) + rot))
            #     elif ord(c) + rot > 122:
            #         decoded_phrase += chr(ord(c) + rot - 25)
            #     elif ord(c) + rot < 97:
            #         decoded_phrase += chr(ord(c) + rot + 25)
            #     continue
            #
            # if ord(c) in range(65, 91):
            #     if 65 <= ord(c) + rot <= 90:
            #         decoded_phrase += (chr(ord(c) + rot))
            #     elif ord(c) + rot > 90:
            #         decoded_phrase += chr(ord(c) + rot - 25)
            #     elif ord(c) + rot < 65:
            #         decoded_phrase += chr(ord(c) + rot + 25)
            #     continue

        if not found_char:
            decoded_phrase += '_'

    return decoded_phrase, rot

def main():
    print("""
    This program is intended to code and decode ciphers based on the Caesar algorithm.
    
    Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
    is one of the simplest and most widely known encryption techniques. 
    It is a type of substitution cipher in which each letter in the plaintext is replaced
    by a letter some fixed number of positions down the alphabet.
     
    For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
    The method is named after Julius Caesar, who used it in his private correspondence.
    
    https://en.wikipedia.org/wiki/Caesar_cipher
         """)
    custom_added = False
    while True:
        print()
        if custom_added:
            print('Please enter the phrase to '
                  'encode/decode (custom alphabet added)')
        else:
            print('Enter the phrase to encode/decode '
                  '(spaces, case and punctuation is preserved)\n'
                  'You can use English or Russian language'
                  ' ("ё" is skipped for Russian)\n'
                  'Or you can add a custom alphabet'
                  ' by typing "add_custom_alpha"')
        phrase = input().strip()

        if phrase == 'add_custom_alpha':
            print("""
    Welcome to custom alphabet editor. You will be required to enter the lower and the upper cases
    for your custom alphabet that will later be used for encrypting. Please enter the symbols
    in 2 lines (each for every case) starting with the lower case. Use no spaces, and ensure there
    are no garbage symbols or missprints. You will have an option to re-enter the alphabet before
    confirming if you make a mistake.
    
    Important: if the symbols of the newly entered alphabet coincide with English or Russian alphabet
    symbols, the newly entered alphabet will replace the corresponding language and will be used
    instead. If you want to return to standard English or Russian(no "ё") - restart the program.
    In case only new symbols are added, the languages will happily work together.
    
    You may want to learn about:
    The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven 
    Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution.
            
    https://en.wikipedia.org/wiki/Vigenere_cipher
                  """)
            while True:
                lower = input('Enter the lower case symbols'
                              ' in one line no spaces:\n').replace(' ', '')
                upper = input('Enter the UPPER CASE symbols'
                              ' in one line no spaces:\n').replace(' ', '')
                check = input('Please carefully check '
                              'the alphabet before saving.\n'
                         'Press "y" to save the alphabet.\n'
                         'Press "n" to re-enter symbols\n').strip().lower()
                while check not in ('y', 'n', 'yes', 'no'):
                    check = input().strip().lower()

                if check in ('y', 'yes'):
                    print('Please choose a name for your alpha\n')
                    name = input().strip().lower()
                    add_custom_alpha(name, lower, upper)
                    break
            print('Alphabet added. Feel free to use. '
                  'Please enter a phrase to encrypt.\n')
            phrase = input().strip()
            custom_added = True

        print()
        print('Enter "+" to rotate the cipher from "a" to "z". '
              'Each round ROT parameter will increase by 1.')
        print('Enter "-" to rotate the cipher from "z" to "a". '
              'Each round ROT parameter will decrease by 1.')
        print('Type "q" or "quit" to enter a new phrase')

        cmd = ''
        rot = 0

        while cmd not in ('quit', 'q'):
            cmd = input().strip()
            if cmd == '+':
                rot += 1
            elif cmd == '-':
                rot -= 1
            decoded_phrase, rot = encrypt(phrase, rot)
            print(f'ROT: {rot}')
            print(decoded_phrase)

        else:
            print()
            input('Thanks for using! And remember - loose lips sink ships!')

main()
