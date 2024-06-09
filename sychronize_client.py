import socket

def Main():

    host='192.168.1.107' #client ip
    port = 8000
    
    server = ('192.168.1.107', 5000)
    
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.bind((host,port))    

    while True:
        # s.sendto(message.encode('utf-8'), server)
        data, addr = c.recvfrom(1024)
        data = data.decode('utf-8')
        print("server address:"+ str(addr) +",client address:" + host + ":" + str(port))
        print("Received from server: " + data)
        c.sendto(data.encode('utf-8'), server)

    s.close()

if __name__=='__main__':
    Main()