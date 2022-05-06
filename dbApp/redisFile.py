import sys
import os
import redis

#connect to redis db
def redisConnect():

    os.system('cls')
    connectionString = input('\nEnter the IPv4 and port of the server, seperated by a ":". Leave blank for default 127.0.0.1:6379\n   >')

    while True:

        if connectionString == '':
            redisIP = '127.0.0.1'
            redisPort = 6379
        else:
            try:
                redisIP, redisPort = connectionString.split(':', 2)
                redisIP, redisPort = str(redisIP.strip()), int(redisPort.strip())
            except:
                print('Ensure the format is correct and try again')
                continue

        global db
        db = redis.Redis(host = redisIP, port = redisPort)
        break

    #check if connection is successful
    try:
        db.ping()
        print(f'\nConnected to Redis at:\n{db}')
    except:
        print('\nError connecting to Redis. Ensure the server is running\nThe program will now terminate')
        input('Press "Enter" to continue')
        sys.exit()

#run redis menu
def redisMenu():

    #menu prompt
    print('\nEnter a command, or type "Help", "Main", or "Exit"')

    while True:

        #get command
        while True:
            command = str(input('   >')).lower().strip()
            
            if command != '':
                break

        #menu commands
        match command:

            case 'main':
                return
            
            case 'exit':
                sys.exit()
            
            case 'help':
                print('\nhelp menu\n')
                continue
        
        #keyword commands
        match command:

            case 'delall':
                db.flushdb()
                print('\nAll keys have been deleted\n')
                continue
            
            case 'viewall':
                print('\nview all keys\n')
                continue

        #split command
        try:
            commandAction, commandArg = command.split(' ', 2)
        except:
            print('\nInvalid Command, type "Help" for more information\n')
            continue

        #match command
        match commandAction:

            case 'set':
                try:
                    keyChoice, valueChoice, expiryChoice = commandArg.split(':', 3)
                    keyChoice, valueChoice, expiryChoice = keyChoice.strip(), valueChoice.strip(), expiryChoice.strip().lower()
                except:
                    print('\nEnsure that the format is correct and try again\n')
                    continue
                
                setKey(keyChoice, valueChoice, expiryChoice)
                continue

            case 'get':
                getKey(commandArg)

            case 'del':
                delKey(commandArg)
                continue

            case _:
                print('\nInvalid Command, type "Help" for more information\n')
                continue

#command methods
def setKey(keyChoice, valueChoice, expiryChoice):
           
    db.set(keyChoice, valueChoice)
    
    if expiryChoice != 'none':
        try:
            expiryTime = int(expiryChoice)
        except:
            print('\nEnsure that the format is correct and try again\n')
            return
        db.expire(keyChoice, expiryTime)
        print(f'\n({keyChoice}: {valueChoice}) has been set and will expire in {expiryTime} seconds\n')
        return
    else:
        print(f'\n({keyChoice}, {valueChoice}) has been set and will not expire\n')
        return

def getKey(getKey):
    try:
        if db.exists(getKey) > 0:
            valueString = rf'{db.get(getKey)}'
        else:
            raise Exception
    except:
        print('\nKey not found\n')
        return

    try:
        preValue, value, postValue = valueString.split("'", 3)
        print(f'\n{getKey}: {value}\n')
    except:
        print('\nError converting value\n')


def delKey(delKey):
    try:
        if db.exists(delKey) > 0:
            db.delete(delKey)
            print(f'\nThe {delKey} key has been deleted\n')
        else:
            raise Exception
    except:
        print(f'\nThe operation did not succeed correctly. The database might be empty, or the "{delKey}" key is not set\n')