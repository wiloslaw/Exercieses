#Write a python program to get the path and name of the file that is currently executing.


import os


os.system("pwd")


print('     ')
print('To jest linia rozdzielajaca')
print('     ')

print("Current File Name : ",os.path.realpath(__file__))