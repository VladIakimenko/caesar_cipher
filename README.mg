# Caesar Cipher
This program is intended to code and decode ciphers based on the **Caesar algorithm**.

Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift,
is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced
by a letter some fixed number of positions down the alphabet.

For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
The method is named after Julius Caesar, who used it in his private correspondence.

https://en.wikipedia.org/wiki/Caesar_cipher

The message in this program is shifted by one character each step allowing to check if the 
code-message was encrypted with the Caesar cipher even if you don't know the ROT-parameter (the shift size).

### Supported languages
The app supports several languages allowing to use multi-lingual encryption. All supported 
languages are stored at ...data/lang.txt, giving an option to freely modify the languages
library, as directly by editing the .txt file as within the program interface 
(add_new_language command may be entered instead of a message to open the dialogue)

The amount of languages to be active at the same time is not restricted unless they don't have the same symbols in their
alphabets. Naturally cyrillic languages work well with latin languages and hieroglyph-based
alphabets. These three normally will work together, meaning that you can enter a multi-lingual
phrase to work with.
However if the symbols of the newly selected alphabet coincide with any of the previously
active, the newly chosen alphabet will replace the corresponding language and will be used
instead.
This dialogue allows to choose one language to work with, other active languages will reset
to defaults. You can edit the default languages by swapping them in the ...data/lang.txt.

...data/lang.reserve_copy is a reserve copy for lang.txt (rename it to lang.txt to restore languages
to defaults in case the original file is messed up with editing)

### Key-phrase encryption
The program gives an opportuninty to use a key-phrase for complex encryption. The user is offered
to enter a pangram in which repeated symbols are removed thus shrortening it to shuffled alphabet
that is now used instead of the standrd one.

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

NOTE: _Modern means of breaking ciphers include frequency analysis and other advanced
methods that can brake practically any substitution cipher.
This app is just a toy and should not be relied on in significant affairs!_