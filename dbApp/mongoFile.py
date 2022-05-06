def loopTest():

    print('Please type mongo')

    while True:

        mongoChoice = input('   >')
    
        try:
            if (str(mongoChoice).lower().strip() == 'mongo'):
                break
            else:
                raise Exception
        except:
            pass