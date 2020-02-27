import os

hostname = "www.itmorelia.edu.mx"
respuesta = os.system("ping -c 1 "+ hostname)
if respuesta == 0:
    print (hostname+ ": esta en funcionamiento1!")
else:
    print (hostname + ": No funciona")


red = "200.33.171.0/24"

os.system("nmap -sP " + red)

'''
Nmap scan report for mail.itmorelia.edu.mx (200.33.171.3)
Host is up (0.11s latency).
Nmap scan report for delfin2.itmorelia.edu.mx (200.33.171.11)
Host is up (0.27s latency).
Nmap scan report for 200.33.171.13
Host is up (0.043s latency).
Nmap scan report for dsc.itmorelia.edu.mx (200.33.171.20)
Host is up (0.072s latency).
Nmap scan report for libra.itmorelia.edu.mx (200.33.171.54)
Host is up (0.057s latency).
Nmap scan report for 200.33.171.63
Host is up (0.075s latency).
Nmap scan report for sagitario.itmorelia.edu.mx (200.33.171.65)
Host is up (0.073s latency).
Nmap scan report for 200.33.171.66
Host is up (0.073s latency).
Nmap scan report for denebvirtual.itmorelia.edu.mx (200.33.171.77)
Host is up (0.23s latency).
Nmap scan report for sappp.itmorelia.edu.mx (200.33.171.80)
Host is up (0.23s latency).
Nmap scan report for 200.33.171.85
Host is up (0.23s latency).
Nmap scan report for 200.33.171.97
Host is up (0.17s latency).
Nmap scan report for 200.33.171.98
Host is up (0.26s latency).
Nmap scan report for 200.33.171.99
Host is up (0.26s latency).
Nmap scan report for 200.33.171.115
Host is up (0.081s latency).
Nmap scan report for 200.33.171.118
Host is up (0.081s latency).
Nmap scan report for vinculacion.itmorelia.edu.mx (200.33.171.124)
Host is up (0.074s latency).
Nmap scan report for 200.33.171.125
Host is up (0.074s latency).
Nmap scan report for 200.33.171.127
Host is up (0.074s latency).
Nmap scan report for 200.33.171.128
Host is up (0.074s latency).
Nmap scan report for 200.33.171.160
Host is up (0.089s latency).
Nmap scan report for 200.33.171.254
Host is up (0.044s latency).
Nmap done: 256 IP addresses (22 hosts up) scanned in 17.43 seconds
'''
