# P15/31457/2015
# KIRAGU WINNIE WANGECHI
# Caesar Cipher

MAX_KEY_SIZE = 26
choices = 'encrypt, e, decrypt, d'


def getMode():
    while True:
        task = raw_input('Do you wish to encrypt or decrypt a message?')
        mode = task.lower()
        if mode in choices:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')


def getMessage():
    input_variable = raw_input('What message would you like to cipher?: ')
    return input_variable


# lets the player type in the key they will use to encrypt or decrypt the message
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for l in message:
        if l.isalpha():
            num = ord(l)
            num += key

            if l.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif l.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += l
    return translated


mode = getMode()
message = getMessage()
key = getKey()

print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
