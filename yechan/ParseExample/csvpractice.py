#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv

with open('egg.csv', 'wb') as csvfile:
    spamwriter =csv.writer(csvfile, delimiter=' ', quotechar='|', quoting =csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam']*5+['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam','wronderful spam'])

with open ('egg.csv','rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter= ' ', quotechar='|')
    for row in spamreader:
        a= ','.join(row)
        print type(a)
        print a