class Language:
    def __init__(self, name, lowercase, uppercase):
        self.name = name
        self.lowercase = lowercase
        self.uppercase = uppercase


def save_language(path, name, lower, upper):
    with open(path, "a", encoding="utf=8") as file:
        file.write(f'\n{name.lower()}:{lower}:{upper}')


def load_languages(path):
    languages = []
    with open(path, 'r', encoding="utf=8") as filehandle:
        for line in filehandle:
            line = line[:-1]
            languages.append(Language(line.split(':')[0], line.split(':')[1], line.split(':')[2]))
    return languages


def alpha_from_pangram(pangram):
    shuffled_alpha = ''
    for c in pangram:
        if c not in shuffled_alpha and c.isalnum():
            shuffled_alpha += c
    shuffled_lang = Language('shuffled', shuffled_alpha, shuffled_alpha.upper())
    return shuffled_lang


def select_languages(languages, selected=None):
    active_languages = []
    chars_in_use = ''
    if selected:
        active_languages.append(selected)
        chars_in_use += selected.lowercase + selected.uppercase
    for lang in languages:
        for c in lang.lowercase + lang.uppercase:
            if c in chars_in_use:
                break
        else:
            active_languages.append(lang)
            chars_in_use += lang.lowercase + lang.uppercase
    return active_languages


def encrypt(phrase, rot, active_languages):
    decoded_phrase = ''
    for c in phrase:
        found_char = False
        if not c.isalnum():
            decoded_phrase += c
            found_char = True
        else:
            for lang in active_languages:
                for case in [lang.lowercase, lang.uppercase]:
                    if c in case:
                        decoded_phrase += (case[case.index(c) + rot]
                                           if case.index(c) + rot < len(case)
                                           else case[case.index(c) - (len(case) - rot)])
                        found_char = True
                        if abs(rot) == len(case):
                            rot = 0
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

    languages = load_languages('data/lang.txt')
    active_languages = select_languages(languages)

    while True:
        print(f"Currently selected languages are: "
              f"{', '.join([lang.name.capitalize() for lang in active_languages])}")
        print('Would you like choose another language?')
        print(f"Languages available: {', '.join([lang.name.capitalize() for lang in languages])}")
        while True:
            reply = input('"y" - change language\n"n" - continue\t').strip().lower()
            if reply in ('y', 'yes'):
                print("""
    You are about to select the active language to be used for encrypting. The amount of languages
    to be active at the same time is not restricted unless they don't have the same symbols in their
    alphabets. Naturally cyrillic languages work well with latin languages and hieroglyph-based
    alphabets. These three normally will work together, meaning that you can enter a multi-lingual
    phrase to work with.
    However if the symbols of the newly selected alphabet coincide with any of the previously 
    active, the newly chosen alphabet will replace the corresponding language and will be used
    instead. 
    This dialogue allows to choose one language to work with, other active languages will reset
    to defaults. You can edit the default languages by swapping them in the ...data/lang.txt.
                      """)
                print(f"Currently selected: "
                      f"{', '.join([lang.name.capitalize() for lang in active_languages])}")
                print('Choose a language you would like to use'
                      ' (enter the number and press "enter"):')
                counter = 0
                enumeration = {}
                for lang in languages:
                    if lang not in active_languages:
                        counter += 1
                        print(str(counter) + '. ' + lang.name)
                        enumeration[counter] = lang
                while True:
                    num = input().strip()
                    if num.isdigit() and int(num) in range(1, counter + 1):
                        break
                for key, lang in enumeration.items():
                    if key == int(num):
                        active_languages = select_languages(languages, lang)
                print(f'Languages in use: '
                      f"{', '.join([lang.name.capitalize() for lang in active_languages])}")
                break
            elif reply in ('n', 'no'):
                break

        print()
        print('Enter the phrase to encode/decode '
              '(spaces, case and punctuation is preserved).\n'
              'You can also encode with a key phrase by typing "use_key".\n'
              'Or you can add a custom alphabet by typing "add_new_alpha"')
        phrase = input().strip()

        if phrase == 'use_key':
            print("""
    You may want to learn about pangrams:
    A pangram or holoalphabetic sentence is a sentence using every letter of a given 
    alphabet at least once. Pangrams have been used to display typefaces, test equipment, and
    develop skills in handwriting, calligraphy, and keyboarding.
    Example: "The quick brown fox jumps over a lazy dog!"
            
    https://en.wikipedia.org/wiki/Pangram
    
    Below you will be able to enter your code-phrase, that will automatically transform to a
    shuffled alphabet that will later be used for encryption. Ensure all characters that will
    be used in a message are in the key-phrase. 
    Key-phrases are easy to remember. This opens opportunities for advanced encryption. 
    If the code recipient knows the key phrase (that will be transformed to a shuffled alphabet)
    and the ROT-parameter (the shift) for the Caesars cipher, then he can use this function to
    decode a message, that is impossible to break using the standard alphabet order.
    
    NOTE: Modern means of breaking ciphers include frequency analysis and other advanced
    methods that can brake practically any substitution cipher. 
    This app is just a toy and should not be relied on in significant affairs!
                  """)
            print()
            code_phrase = input('Enter your code-phrase:\n').replace(' ', '').lower()
            shuffled_lang = alpha_from_pangram(code_phrase)
            print('Your code-phrase forms the following alphabetic lines:\n'
                  f'{shuffled_lang.lowercase}\n'
                  f'{shuffled_lang.uppercase}')
            languages.append(shuffled_lang)
            active_languages = select_languages(languages, shuffled_lang)
            print()
            print('Code-phrase applied!')
            phrase = input('Enter the text to encrypt:\n').strip()

        if phrase == 'add_new_alpha':
            print("""
    Welcome to custom alphabet editor. You will be required to enter the lower case and
    (optionally) the upper case of your custom alphabet that will later be used for encrypting.
    Please enter the symbols in one-line. Use no spaces, and ensure there are no garbage symbols
    or missprints. 
    You will have an option to re-enter the alphabet before confirming if you make a mistake.
                  """)
            while True:
                lower = input('Enter the lower case symbols in one line no spaces:\n')
                lower = lower.replace(' ', '')
                print('enter UPPER CASE?')
                while True:
                    reply = input('"y" - enter\n"n" - continue\t')
                    if reply in ('y', 'yes'):
                        upper = input('Enter the UPPER CASE symbols in one line no spaces:\n')
                        upper = upper.replace(' ', '')
                        break
                    elif reply in ('n', 'no'):
                        upper = lower.upper()
                        print(upper)
                        break
                check = input('Please carefully check the alphabet before saving.\n'
                              'Press "y" to save the alphabet.\n'
                              'Press "n" to re-enter symbols\n').strip().lower()
                while check not in ('y', 'n', 'yes', 'no'):
                    check = input().strip().lower()
                if check in ('y', 'yes'):
                    print('Please choose a name for your alpha')
                    name = input().strip().lower()
                    save_language('data/lang.txt', name, lower, upper)
                    languages = load_languages('data/lang.txt')
                    for lang in languages:
                        if lang.name == name:
                            active_languages = select_languages(languages, lang)
                    print(f'Alphabet added. Languages in use: '
                          f"{', '.join([lang.name.capitalize() for lang in active_languages])}")
                    break
            print()
            print('Please enter a phrase to encrypt:')
            phrase = input().strip()

        print()
        print('Each round the "ROT" parameter will increase or '
              'decrease by 1, depending on the shift direction.')
        print('Enter "+" to perform the right shift.')
        print('Enter "-" to perform the left shift.')
        print('Type "q" or "quit" to enter a new phrase')

        cmd = ''
        rot = 0
        while cmd not in ('quit', 'q'):
            cmd = input().strip()
            if cmd == '+':
                rot += 1
            elif cmd == '-':
                rot -= 1
            decoded_phrase, rot = encrypt(phrase, rot, active_languages)
            print(f'ROT: {rot}')
            print(decoded_phrase)
        else:
            print()
            input('Thanks for using! And remember - loose lips sink ships!\n')


main()
