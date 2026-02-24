# The focus of this workshop was mainly working with defs in the form of making a ceaser cipher

# Creating a def for the basis of the caesar cipher
def caesar(text, shift, encrypt=True):
    # The lab didnt have me make a "Test" to verify that the text parameter was a string
    # Built in test to make sure that the shift parameter is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    # Second built in test to make sure that shift parameter is between 1 and 25
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
    # This is what we are using to shift our "code"
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # This is for the use case that the encrypt=False then it using a negative value for the shift
    # This allows the shift to take palce in the opposite direction baded on the encryption process
    if not encrypt:
        shift = - shift
    
    # we are uisng this to capture the whole "alphabet" variable since the shift will cut off "x" of the string based on the shift value
    # This adds the "missing" section onto the end of the shifted "alphabet" so we dont lose any characters
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    # This is focusing on the str.maketrans(x,y) function we are using to make a translation table, mapping x to y
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    # This is executing the encyption using the previously made table and then storing the value with the return
    encrypted_text = text.translate(translation_table)
    return encrypted_text

# here we are creating a encrypt def using the previous caesar def
def encrypt(text, shift):
    return caesar(text, shift)

# here we are creating a decrypt def also using the previous caesar def    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# Actual use case of the encrypt def
encrypted_text = encrypt('freeCodeCamp', 3)
print("Encrypted:",encrypted_text)

# Actual use case of the decrypt def
decrypted_text = decrypt('Pbhentr vf sbhaq va hayvxryl cynprf.', 13)
print("Decrypted:",decrypted_text)