def loopTest():

    print('Please type cassandra')

    while True:

        cassandraChoice = input('   >')
    
        try:
            if (str(cassandraChoice).lower().strip() == 'cassandra'):
                break
            else:
                raise Exception
        except:
            pass