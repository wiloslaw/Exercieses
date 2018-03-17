import os

path = "/var/"

if os.path.exists(path):
    print('katalog istnieje')
else:
    print('katalog nie istnieje')

import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))
