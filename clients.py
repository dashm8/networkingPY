import socket
import threading

def tcpclient(target,port):
    #create a tcp client
    target_host = target
    target_port = port


    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(target_host,target_port)
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    response = client.recv(4096)
    print response

def udpclient():
    
    target_host = "127.0.0.1"
    target_port = 80

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto("AAABBBCCC",(target_host,target_port))

    
