def machine():
    key = 'abcdefghijklmnopqrstuvwxyz !'
    value = key[-1] + key[0:-1]

    encryptDict = dict(zip(key, value))
    decryptDict = dict(zip(value, key))

    message = input("Please Enter Your Message :  ")
    mode = input("Please Select The mode : Emcode(X)   or   Decode(Y):")

    if mode.upper() == 'X':
        newMessage = ''.join([encryptDict[letter]
                            for letter in message.lower()])
    elif mode.upper() == 'Y':
        newMessage = ''.join([decryptDict[letter]
                            for letter in message.lower()])
    else:
        print("Please Enter a Valid Option ? ")

    return newMessage.capitalize()

print(machine())