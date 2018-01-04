# parse 정리

1. u"문자열" :한글 가능하게

2. argparse().Argumentparse(description= , usage= , formatter_class=argparse.RawTextHelpFormatter)

description: 프로그램의 설명(문자열)usage: usage 메세지를 계산?formatter_class :포메팅 방식 

3. argparse.ArgumentParser().add_argument():add_argument("-db", default=None, help=u"DB 파일명, e.g.) DB검색_2017_0703_17")d: default : 비어있을때 주어질 값 help : 브리프 설명

argparse.ArgumentParser().add_argument("변수이름 및 설명", type=변수타입, help="출력되는설명") 

argparse.ArgumentParser().add_argument("-v 혹은 --어쩌고": 일종의 스위치,[(type=변수타입, choices =[1,2,3]:여기서만 뽑아준다 안그럼 에러), action : -v --어쩌고를 카운트 한다 입력시는 -vv -vvv] , help="출력되는설명")

group = parser.add_mutually_exclusive_group(): 상호 배타옵션 추가할때ex):group.add_argument("-v", "--verbose", action="store_true")group.add_argument("-q", "--quiet", action="store_true")

[-v | -q], which tells us that we can either use -v or -q, but not both at the same time:

# excell_class:

1. open_exc_doc(self,__file) : 파일을 받아 openpyxl 로 워크북을 로드하고 오픈되었음을 알림 return 해당 워크북
2. read_vertical(self, __file): 엑셀? 시트를(범위는 column[m]:column[n]) 받아 행을 위에서 아래로 전부 리스트에 넣어 return[[row1],[row2]....]
# check_form(__buf):
__itter : __buf의 길이
__list :
1. __buf의 첫 두 자리가 20이 아니면 앞에 20을 추가한다.
2. __buf 숫자인듯 buf의 길이가 12 이면 끝에 -01(12,13,14)을 추가한다.
3. 만약 길이가 12 이상일경우 1) 13번째에(index 12)에 -가 있다면 
2) 그다음 index 13이 0이 아닌경우 그숫자를 -0다음으로 붙인다(__buf 길이는 아마도 12 아니면 15 (20이 없는 경우는 10일수도) 인듯)
결론 : 결국 받은 __buf를 형식을 :20----------'-01' or'-0x'로 만들어 __list에 넣어 준다.

# color_list(__class, target, db):

1. db_sheets : db.get_sheet_names() :db 의 워크시트 (시트 전체 이름) 리스트 반환

2. db_sheet: db.get_sheet_by_name(db_sheets[0]) db 의 워크시트 제목을 key로 sheet 를 반환 (wb["제목"] 이랑같음 <여기선 첫째 시트 만 반환>

3. db_company_nums:__class.read_vertical(db_sheet, db_start_range, db_end_range) __class 파일(아마 엑셀) 을 read_vertical 한다 아까 받은 db_sheet 의 db_start_range 부터 db_end_range 이건 어디서 정의가 된거지?

결론 db 워크시트중 첫째 시트의 정해진 범위만큼 가로로 읽어서 전체를 리스트로 반환

4. target_sheets = target.get_sheet_names()타겟 엑셀의 워크시트이름을 리스트로 반환

5.  target_sheet = target.get_sheet_by_name(target_sheets[0])타겟 엑셀의 워크시트 첫째 내용 반환

6. arget_company_nums = __class.read_vertical(target_sheet, list_start_range, list_end_range) 
llist 시작 범위 부터 끝범위까지(갑자기 왜 list_start_range?) 똑같이 타겟 시트의 내용 반환 리스트로

12: check_form(db_company_nums)    check_form(target_company_nums): 리스트안의 값들을 check_form 함수를 통해 모양을 갖춰준다.

13:dd = len(db_company_nums)
td = len(target_company_nums)
: 주석을 보면 각각 db 와 target 데이터의 인덱스 값이라 한다 (아래에 쓰일듯)

14:count_date = 0count_12digits = 0count_all = 0

15:    for target_i in range(0, td):        for db_i in range(0, dd):            if str(db_company_nums[db_i])[0:8] == str(target_company_nums[target_i])[0:8]:
설명 : 타겟값과 db 값의 수치가 같은지 비교한다 첫 8줄(index 7까지)
                target_sheet['A' + str(target_i+int(list_start_range[1:]))].fill = PatternFill("solid", fgColor="DDFFDD")                count_date = count_date + 1                # print str(db_company_nums[db_i])[0:8]                break설명 : 만약 값이 타겟값과 같다면 먼가 칠해주는거 같음 index값 다시 확인해보자. 그리고 c ount_date 에 1을 더해준다 그리고 해당 db값 8자리 출력
    target_sheet['F2'].fill = PatternFill("solid", fgColor="DDFFDD")설명: 타겟의 해당 F2 인덱스 값(아마 F2 셀인듯 )들을 patternfill 로 solid 한 type 으로 색칠 (아마 같지않은것? 같은것?)

16: 나머지 밑의 2개 다 같고 색만다름 타겟의 E2 D2에 다른색으로 색칠 하고 break 처음은 날짜비교(count date) 두번째는 12(count 12) 자리 비교 3번째는(count all) 그냥 다

17: 색칠된 target의 D2 에는 count_all(갯수)을 E2 에는 count_12digits-count_all을 F2에는 count_date - count_12digitD2: 모든게 타겟과 일치 ('20170612 0000 -01)E2: 12만 타겟과 일치    ('20170612 0000)F2: 날짜만 일치     ('20170612 )       

18:  __t = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S") __t 에 현재 날짜 시간을 위와 같은 형식으로

19: file_name = __t + '_colored_result_for_' + db_file + '.xlsx'    target.save(file_name)색칠된 타겟 파일을 날짜와 컬러됬다고 이름 붙이고 저장.

# color_db(__class, company, db):

1. load db file    db_sheets = db.get_sheet_names()    db_sheet = db.get_sheet_by_name(db_sheets[0])    db_company_nums = __class.read_vertical(db_sheet, 'b5', 'b1104')
설명: 타겟이랑 똑같이 맨 처음 시트를 db_sheet에 지정한다. 
그리고 db_company_nums 에 b5열부터 b1104까지 read_vertical 실시

2. load list file    company_sheets = company.get_sheet_names()    company_sheet = company.get_sheet_by_name(company_sheets[0])    company_company_nums = __class.read_vertical(company_sheet, 'a2', 'a580')설명 : company_company_nums 에 company 첫시트의 a2 부터 a580 까지 지정

3.  check_form(db_company_nums)    check_form(company_company_nums)형식 맞춰준다.

4.db data index    dd = len(db_company_nums)  company data index    td = len(company_company_nums)

5. compare and color - 8 digits(date) are the same    for db_i in range(0, dd):        for company_i in range(0, td):            if str(db_company_nums[db_i])[0:8] == str(company_company_nums[company_i])[0:8]:                db_sheet['B' + str(db_i + 5)].fill = PatternFill("solid", fgColor="DDFFDD")                # print str(db_company_nums[db_i])[0:8]
설명: 컴퍼니 시트와 db의 날짜 값이 같다면 db에 B6 ? 인가에 색칠하고 db 날짜값 출력
나머지 2개의 코드는 각각 12 자리 까지 그리고 전부 까지 색칠 근데 왜 index가 다같지? 여기 고쳐야하나?
그리고 시간 설정해서 색칠된 db 파일 저장.
