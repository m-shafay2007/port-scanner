import socket
target=input("enter target ip address")
starting_port=int(input("enter starting port number:"))
ending_port=int(input("enter ending port number: "))
for port in range(starting_port,ending_port +1):
	s=socket.socket()
	s.settimeout(1)
	result=s.connect_ex((target,port))
	if result==0:
		print("port",port,"--OPEN")
	with open("result_of_port_scanner.txt","a") as f:
		f.write("port" + str(port) + "OPEN\n")
s.close()
