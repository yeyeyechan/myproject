                count_date = count_date + 1
                # print str(db_company_nums[db_i])[0:8]
                break
설명 : 만약 값이 타겟값과 같다면 먼가 칠해주는거 같음 index값 다시 확인해보자. 그리고 c ount_date 에 1을 더해준다 그리고 해당 db값 8자리 출력


    target_sheet['F2'].fill = PatternFill("solid", fgColor="DDFFDD")
설명: 타겟의 해당 F2 인덱스 값(아마 F2 셀인듯 )들을 patternfill 로 solid 한 type 으로 색칠 (아마 같지않은것? 같은것?)


16: 나머지 밑의 2개 다 같고 색만다름 타겟의 E2 D2에 다른색으로 색칠 하고 break 
처음은 날짜비교(count date) 두번째는 12(count 12) 자리 비교 3번째는(count all) 그냥 다

17: 색칠된 target의 D2 에는 count_all(갯수)을 E2 에는 count_12digits-count_all을 F2에는 count_date - count_12digit
D2: 모든게 타겟과 일치 ('20170612 0000 -01)
E2: 12만 타겟과 일치    ('20170612 0000)
F2: 날짜만 일치     ('20170612 )
       

18:  __t = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S") 
__t 에 현재 날짜 시간을 위와 같은 형식으로

19: file_name = __t + '_colored_result_for_' + db_file + '.xlsx'
    target.save(file_name)
색칠된 타겟 파일을 날짜와 컬러榮鳴 이름 붙이고 저장.


# color_db(__class, company, db):

1. load db file
    db_sheets = db.get_sheet_names()
    db_sheet = db.get_sheet_by_name(db_sheets[0])
    db_company_nums = __class.read_vertical(db_sheet, 'b5', 'b1104')

설명: 타겟이랑 똑같이 맨 처음 시트를 db_sheet에 지정한다. 

그리고 db_company_nums 에 b5열부터 b1104까지 read_vertical 실시


2. load list file
    company_sheets = company.get_sheet_names()
    company_sheet = company.get_sheet_by_name(company_sheets[0])
    company_company_nums = __class.read_vertical(company_sheet, 'a2', 'a580')
설명 : company_company_nums 에 company 첫시트의 a2 부터 a580 까지 지정


3.  check_form(db_company_nums)
    check_form(company_company_nums)
형식 맞춰준다.


4.db data index
    dd = len(db_company_nums)
  company data index
    td = len(company_company_nums)

5. 
compare and color - 8 digits(date) are the same
    for db_i in range(0, dd):
        for company_i in range(0, td):
            if str(db_company_nums[db_i])[0:8] == str(company_company_nums[company_i])[0:8]:
                db_sheet['B' + str(db_i + 5)].fill = PatternFill("solid", fgColor="DDFFDD")
                # print str(db_company_nums[db_i])[0:8]

설명: 컴퍼니 시트와 db의 날짜 값이 같다면 db에 B6 ? 인가에 색칠하고 db 날짜값 출력

나머지 2개의 코드는 각각 12 자리 까지 그리고 전부 까지 색칠 근데 왜 index가 다같지? 여기 고쳐야하나?

그리고 시간 설정해서 색칠된 db 파일 저장.
