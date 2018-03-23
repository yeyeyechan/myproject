#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import openpyxl
document =openpyxl.load_workbook('sample.xlsx')
docusheets = document.get_sheet_names()
print(u"docusheets 의 타입은", type(docusheets))
print(docusheets)
a=docusheets[0]
sheetFirst = document.get_sheet_by_name(docusheets[0])
print sheetFirst
print u"sheetFirst 의 타입은", type(sheetFirst)
print sheetFirst['A2'].value

print type(sheetFirst['A2'])

print sheetFirst['A2'].value


a=sheetFirst.rows
'''for i in a :
    print i, u'마지막 과 비슷한 형식?'
    for b in i:
        print b.value,
    print '\n'''
all_rows = sheetFirst.rows
if a == all_rows:
    
    print all_rows[:]


