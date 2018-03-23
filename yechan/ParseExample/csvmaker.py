#-*- coding: utf-8 -*-
import sys
import random
reload(sys)
sys.setdefaultencoding('utf-8')
from openpyxl.compat import range


f=open("csvmaker.csv",'w')

for row in range(1,40):
    for col in range(1,40):
        f.write(str(random.randrange(1,40))+','+' ')


f.close()

f=open("csvmaker.csv",'r')

for row in range(1,40):
    for col in range(1,40):
        data =f
        print data,

f.close()