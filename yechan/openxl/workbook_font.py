from openpyxl.styles import Font, Alignment
from openpyxl improt Workbook

wb = Workbook()
ws1 =wb.active

ws1.title ="font practice"

ca1 = ws1['A1']

ca1.font =Font(name ='맑은 고딕'.decode('cp949'), size=15, bold=True)

