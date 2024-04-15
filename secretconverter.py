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
        if ord('a') < number > ord('z'):
            number = ord('a')
        if ord('A') < number > ord('Z') and number < ord('a'):
            number = ord('A')
        if not chr(ord(i)).isalpha():
            letter = chr(ord(i))
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
        if number == ord('a') - 1:
            number = ord('z')
        if number == ord('A') - 1:
            number = ord('Z')
        if not chr(ord(i)).isalpha():
            letter = chr(ord(i))
        else:
            letter = chr(number)
        encryptedLevelTwo += letter
    return encryptedLevelTwo


if __name__ == "__main__":
    encrypt = input("Here: ")
    print(kla3(encrypt))
    print(decode_kla3(kla3(encrypt)))
