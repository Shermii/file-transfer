import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),8080))

msg = s.recv(2048)
print(msg.decode("utf-8"))

commands = ['help','ls','receive','get','getsize','getdir','quit']

desc = {commands[1] : "Lists all files",
	commands[2] : "Downloads file",
	commands[3] : "Downloads file",
	commands[4] : "Gets size of a file",
	commands[5] : "Gets current directory",
	commands[6] : "Self explanatory"}



def comm(a):
    a = a.lower()
    if a == commands[0]:
        for i in range(1,len(commands)):
            print(commands[i],'>>',desc[commands[i]])

def get(a,mess):
    sumn = a.split(' ')
    if sumn[0] == commands[3]:
        file = open(a[4:],'wb')
        file.write(mess)
        file.close()


while True:

    a = ''
    a = input('#> ')
    sumn = a.split(' ')
    if sumn[0] not in commands:
        print('for info type HELP')
        a = input('#> ')

    s.send(a.encode())
    msg = s.recv(2048)
    print(msg.decode(),'\n')

    if sumn[0] == commands[3]:
        file = open(a[4:],'wb+')
        file.write(msg)

        file.close()


