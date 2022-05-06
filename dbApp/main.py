#imports
import os
import sys

#file imports
import redisFile
import sqlFile #use pyodbc
import mongoFile
import cassandraFile

#run menu
def mainMenu():
    #menu prompts
    os.system('cls')
    print('Select a database below, or type "Exit": \n1. SQL\n2. Redis\n3. Mongo\n4. Cassandra')

    #verify menu choice
    while True:
        try:
            choice = input('   >')

            if (str(choice).lower().strip() == 'exit'):
                sys.exit()
            else:
                dbChoice = int(choice)

            if (dbChoice < 1 or dbChoice > 4):
                raise Exception
            else:
                break

        #needed since calling sys.exit() will throw an exception SystemExit
        except SystemExit:
            os.system('cls')
            sys.exit()

        except:
            pass #will not end the code
            
    #menu choice action
    match dbChoice:
        case 1:
            #run sql menu, which will return here when broken
            sqlFile.loopTest()

            input('\nPress "Enter" to continue')
            return
        case 2:
            #run redis ''
            redisFile.redisConnect()
            redisFile.redisMenu()
            return
        case 3:
            #run mongo ''
            mongoFile.loopTest()

            input('\nPress "Enter" to continue')
            return

        case 4:
            #run cassandra ''
            cassandraFile.loopTest()

            input('\nPress "Enter" to continue')
            return



#run app
while True:
    mainMenu()