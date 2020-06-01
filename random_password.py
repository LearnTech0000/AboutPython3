import os
import sys
import getpass
#import attachment
from time import localtime
from random import randint, shuffle
from configparser import ConfigParser


def log(password: str, userName=getpass.getuser()):
    os.chdir(os.getcwd())
    _, month, day, hour, minute, second, *rest = localtime()
    nowTime = f"{month}.{day}>>{hour:0>2}_{minute:0>2}_{second:0>2}.ini"
    history = open(nowTime, "w+")

    wLog = ConfigParser()
    wLog['Password'] = {"record": f"{userName} >>> {password}"}
    with open(nowTime, "w") as f:
        wLog.write(f)


def randomPassword(pwLength, password=None):
    if password is None:
        password = []

    charList = [chr(i) for i in range(33, 127)]
    abortItem = [
        '(', ')', '/', ':', ';', '<', '=', '>', '?', '@',
        '[', '\\', ']', '^', '`', '{', '|', '}', '~', '"',
        "'", '*', '+', '!', '$', '%', '&', ',', '_'
    ]

    for item in abortItem:
        charList.remove(item)
    charList.insert(0, '_')

    numberNum = randint(1, pwLength // 2)
    letterNum = randint(1, pwLength // 2)
    charNum = randint(1, pwLength // 2)

    lengthNumList = [numberNum, letterNum, charNum]

    while sum(lengthNumList) > pwLength:
        if lengthNumList[0] != 1:
            lengthNumList[0] -= 1
        else:
            lengthNumList[1] -= 1
    while sum(lengthNumList) < pwLength:
        lengthNumList[1] += 1

    nN, lN, cN = lengthNumList

    while nN > 0:
        numIdx = randint(4, 13)
        password.append(charList[numIdx])
        nN -= 1

    while lN > 0:
        letIdx = randint(13, len(charList) - 1)
        password.append(charList[letIdx])
        lN -= 1

    while cN > 0:
        chrIdx = randint(0, 3)
        password.append(charList[chrIdx])
        cN -= 1

    while len(password) < pwLength:
        idx = randint(0, len(charList) - 1)
        password.append(charList[idx])

    shuffle(password)

    password = ''.join(password)
    return password


def main(specLength=12):
    try:
        if len(sys.argv) == 3:
            _, userName, pwLength = sys.argv
            pwLength = int(pwLength)
            if pwLength >= 6:
                pwd = randomPassword(pwLength)
                log(pwd, userName)
                print(pwd)
            else:
                print("Password must be at least 6 digits")
        else:
            pwd = randomPassword(specLength)
            log(pwd)
            print(f"{getpass.getuser()} >>> {pwd}")
    except ValueError:
        print("Wrong format!")
    #attachment.sendEmail()

if __name__ == '__main__':
    main()
