from math import floor

def kla1(sentence: str) -> str:
    sentence = sentence.split()
    encrypted = ''
    for i in sentence:
        firstLetter = i[0]
        word = i[:0:-1]
        encrypted += firstLetter + word + ' '
    return encrypted

def kla2(sentence: str) -> str:
    sentence = sentence.split()
    encrypted = ''
    for i in sentence:
        firstLetter = i[0]
        word = i[:0:-1]
        lastHalf = (firstLetter + word)[floor((len(firstLetter) + len(word))/2):]
        firstHalf = (firstLetter + word)[:floor((len(firstLetter) + len(word))/2)]
        encrypted += lastHalf + firstHalf + ' '
    return encrypted

def kla3(sentence: str) -> str:
    sentence = sentence.split()
    encryptedLevelOne = ''
    encryptedLevelTwo = ''
    for i in sentence:
        firstLetter = i[0]
        word = i[:0:-1]
        lastHalf = (firstLetter + word)[floor((len(firstLetter) + len(word))/2):]
        firstHalf = (firstLetter + word)[:floor((len(firstLetter) + len(word))/2)]
        encryptedLevelOne += lastHalf + firstHalf + ' '
    for i in encryptedLevelOne:
        number = ord(i) + 1
        if not chr(number).isspace() and chr(number - 1).isalpha() and 97 < number > 122:
            number = 97
        if not chr(number).isspace() and chr(number - 1).isalpha() and 65 < number > 90 and number < 97:
            number = 65
        if chr(ord(i)).isspace():
            letter = ' '
        else:
            letter = chr(number)
        encryptedLevelTwo += letter
    return encryptedLevelTwo

def decode_kla3(sentence: str) -> str:
    sentence = sentence.split()
    encryptedLevelOne = ''
    encryptedLevelTwo = ''
    for i in sentence:
        firstLetter = i[0]
        word = i[:0:-1]
        lastHalf = (firstLetter + word)[floor((len(firstLetter) + len(word))/2):]
        firstHalf = (firstLetter + word)[:floor((len(firstLetter) + len(word))/2)]
        encryptedLevelOne += lastHalf + firstHalf + ' '
    for i in encryptedLevelOne:
        number = ord(i) - 1
        if not chr(number).isspace() and number == 96:
            number = 122
        if not chr(number).isspace() and number == 64:
            number = 90
        if chr(ord(i)).isspace():
            letter = ' '
        else:
            letter = chr(number)
        encryptedLevelTwo += letter
    return encryptedLevelTwo


if __name__ == "__main__":
    print(decode_kla3(input("Here: ")))
