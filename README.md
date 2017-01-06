# Enigma

A Smart MonoAlphabetic Substitution Cipher Breaker made by Rishabh Bector. 

Enigma uses a combination of a genetic and hill-climb algorithms to quickly and efficiently crack a monoalphabetic substitution.
Needless to say, with `403291461126605635584000000` possible keys, brute force would be tricky.

Don't know what a MonoAlphabetic substitution is? --> http://crypto.interactive-maths.com/monoalphabetic-substitution-ciphers.html

This method is better than simply using English letter frequencies, as it works with small text samples, in which case letter frequencies would fail.

## Documentation

Make sure you have python 3.0 or above installed.

Run the following commands:

`pip install tqdm`

`git clone https://github.com/rishabh-bector/Enigma.git`

`cd Enigma/`

 `python geneticsub.py`
 
 Paste your cipher text into the prompt and hit `Enter`
 
 Wait.
 
 Once your text has been decrypted (Normally around 2-3 minutes), you can exit the program.
 
Have Fun!
