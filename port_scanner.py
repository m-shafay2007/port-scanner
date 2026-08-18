  GNU nano 8.7.1                                     port_scanner.py                                               
import socket
print("=" * 40)
print("   BlackSpider Port Scanner v2.0")
print("=" *  40)
services={21:"FTP",22:"SSH",23:"TELNET",80:"HTTP",443:"HTTPS",3389:"RDP",53:"DNS",25:"SMTP"}
target=input("enter target ip address: ")
starting_port=int(input("enter starting port number: "))
ending_port=int(input("enter ending port number: "))
print(f"\n[*] Scanning {target}...\n")

for port in range(starting_port,ending_port +1):
        s=socket.socket()
        s.settimeout(0.2)
        result=s.connect_ex((target,port))
        if result==0:
                service=services.get(port,"Unknown")
                print(f"port {port},--OPEN--{service}")
                with open("result_of_port_scanner.txt","a") as f:
                        f.write(f"Port {port} --OPEN-- {service}\n")
        s.close()
print("\n[*] Scan Completed...")





