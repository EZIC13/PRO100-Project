
def loopTest():

    print('Please type sql')

    while True:

        sqlChoice = input('   >')
    
        try:
            if (str(sqlChoice).lower().strip() == 'sql'):
                break
            else:
                raise Exception
        except:
            pass

        