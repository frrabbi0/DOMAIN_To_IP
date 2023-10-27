#domain_to_ip


import socket as s

import pyfiglet as p

import time as t

from tqdm import tqdm

from termcolor import colored as c


print ('''┌────────────────────────────────────────┐''')


b = c ( p.figlet_format('IP Check'),'red')

print (b)
print (c( ('            Develper BY F R Rabbi'),'green'))
print ('''└────────────────────────────────────────┘''')

print ('')
r = input (c(('Enter your target domain : '),'yellow'))

ip = s.gethostbyname(r)

print ('')
for i in tqdm (range(100),
    desc ='Loading...',
    ascii = False,ncols =70):
    
    t. sleep (0.05)
    
print ('')

print (c(('[1] Domain Name :'+r),'green'))

print ('')

print (c(('[2] Damain Ip :'+ip), 'green'))

