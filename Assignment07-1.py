# -------------------------------------------------- #
# Title: 
# Description: Pickling and Structured Error Handling
# ChangeLog (Who,When,What):
# KBanfill, 3-7-2022, Created Script
# KBanfill, 3-9-2022, Modified script
# -------------------------------------------------- #

data = []

import pickle

try:
    strPickle = str(input("Enter a pickle type: "))
    strRank = str(input("Enter pickle ranking: "))
    lstPickleTier = [strPickle, strRank]
    if strPickle.lower() == 'dill' and strRank.strip() == '1':
        raise Exception('Dill pickles are terrible. Please don\'t rank them number 1.')
    if strPickle.isnumeric():
        raise Exception('Please don\'t enter numbers for pickle names.')
except Exception as e:
    print('Non-specific error. We\'re in a pickle!')
    print('Built-In Python error info: ')
    print(e, e.__doc__, type(e), sep='\n')

else:
    try:
        print(lstPickleTier)

        print('<------------Pickling------------>')
        objFile = open("AppData.dat", "ab")
        pickle.dump(lstPickleTier, objFile)
        objFile.close()
    except Exception as e:
        print('Non-specific error. We\'re in a pickle!')
        print('Built-In Python error info: ')
        print(e, e.__doc__, type(e), sep='\n')

    try:
        print('<-------------Unpickling------------->')
        objFile = open("AppData.dat", "rb")
        objFileData = pickle.load(objFile)
        objFile.close()

        print(objFileData)
    except FileNotFoundError as e:
        print("Error. The file does not exist.")
    except Exception as e:
        print('Non-specific error. We\'re in a pickle!')
        print('Built-In Python error info: ')
        print(e, e.__doc__, type(e), sep='\n')
