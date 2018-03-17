

folder = '/tmp/'

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir(folder) if isfile(join(folder, f))]

print(files_list);


