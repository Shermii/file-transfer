import socket
import _thread
import os



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),8080))
s.listen(5)

cwd = os.getcwd()
files = os.listdir(cwd)


commands = ['help','ls','receive','get','getsize','getdir','quit']

desc = {commands[1] : "Lists all files",
        commands[2] : "Downloads file",
        commands[3] : "Downloads file",
        commands[4] : "Gets size of a file",
        commands[5] : "Gets current directory",
        commands[6] : "Self explanatory"}



def comm(a):
    a = a.lower()
    sumn = a.split(' ')
    result = ''
    
    if  sumn[0] == commands[1]:
        result = "\n >> ".join(files)
        
    elif sumn[0] == commands[2]:
        pass
    
    elif sumn[0] == commands[2]:
        pass
        
    elif sumn[0] == commands[4]:
        name = a[8:]
        result = os.path.getsize(f'{cwd}\{name} ')
        result = str(round(result/1000000,2))+' MB '+str(round(result/1000,2))+ ' KB'
        
    elif sumn[0] == commands[5]:
        result = "Current directory = " + cwd
    
    elif sumn[0] == commands[6]:
        clientsocket.close()

    return result

xpa = 0

while True:

    if xpa == 0:
        clientsocket,adress = s.accept()
        print(adress)
        clientsocket.send(bytes(f"Welcome to the server!", "utf-8"))
        xpa += 1
    else:
        pass

    msg = ''

    try:   
        msg = clientsocket.recv(2048).decode()


        sumn = msg.split(' ')

        if msg != '':
            if sumn[0] == commands[3]:
                file = open(msg[4:],'rb')
                result = file.read(2048)
                clientsocket.send(result)
                file.close()

            else:
                res = comm(msg)
                clientsocket.send(bytes(f"{res}" , "utf-8"))
        else:
            pass
            
    except OSError:
        xpa -= 1
        pass

input()


