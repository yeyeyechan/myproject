# parse ����

1. u"���ڿ�" :�ѱ� ��°����ϰ� ���ִ�

2. argparse().Argumentparse(description= , usage= , formatter_class=argparse.RawTextHelpFormatter)

description: ���α׷��� ����(���ڿ�)
usage: usage �޼����� ���?
formatter_class :������ ��� 

3. argparse.ArgumentParser().add_argument():
add_argument("-db", default=None, help=u"DB ���ϸ�, e.g.) DB�˻�_2017_0703_17")d: default : ����������� �־��� ��
help : �긮�� ����

argparse.ArgumentParser().add_argument("�����̸� �� ����", type=����Ÿ��, help="��µǴ¼���")

argparse.ArgumentParser().add_argument("-v Ȥ�� --��¼��": ������ ����ġ,[(type=����Ÿ��, choices =[1,2,3]:���⼭�� �̾��ش� �ȱ׷� ����), action : -v --��¼�� ī��Ʈ �Ѵ� �Է½ô� -vv -vvv] , help="��µǴ¼���")


group = parser.add_mutually_exclusive_group(): ��ȣ ��Ÿ�ɼ� �߰��Ҷ�
ex):group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

[-v | -q], which tells us that we can either use -v or -q, but not both at the same time:



# excell_class:

1. open_exc_doc(self,__file) : ������ �޾� openpyxl �� ��ũ���� �ε��ϰ� ���µǾ����� �˸� return �ش� ��ũ��

2. read_vertical(self, __file): ����? ��Ʈ��(������ column[m]:column[n]) �޾� ���� ������ �Ʒ��� ���� ����Ʈ�� �־� return[[row1],[row2]....]

# check_form(__buf):

__itter : __buf�� ����

__list :

1. __buf�� ù �� �ڸ��� 20�� �ƴϸ� �տ� 20�� �߰��Ѵ�.

2. __buf �����ε� buf�� ���̰� 12 �̸� ���� -01(12,13,14)�� �߰��Ѵ�.

3. ���� ���̰� 12 �̻��ϰ�� 1) 13��°��(index 12)�� -�� �ִٸ� 

2) �״��� index 13�� 0�� �ƴѰ�� �׼��ڸ� -0�������� ���δ�(__buf ���̴� �Ƹ��� 12 �ƴϸ� 15 (20�� ���� ���� 10�ϼ���) �ε�)


��� : �ᱹ ���� __buf�� ������ :20----------'-01' or'-0x'�� ����� __list�� �־� �ش�.



# color_list(__class, target, db):

1. db_sheets : db.get_sheet_names() :db �� ��ũ��Ʈ (��Ʈ ��ü �̸�) ����Ʈ ��ȯ

2. db_sheet: db.get_sheet_by_name(db_sheets[0]) db �� ��ũ��Ʈ ������ key�� sheet �� ��ȯ (wb["����"] �̶����� <���⼱ ù° ��Ʈ �� ��ȯ>

3. db_company_nums:__class.read_vertical(db_sheet, db_start_range, db_end_range)
 __class ����(�Ƹ� ����) �� read_vertical �Ѵ� �Ʊ� ���� db_sheet �� db_start_range ���� db_end_range �̰� ��� ���ǰ� �Ȱ���?

��� db ��ũ��Ʈ�� ù° ��Ʈ�� ������ ������ŭ ���η� �о ��ü�� ����Ʈ�� ��ȯ

4. target_sheets = target.get_sheet_names()
Ÿ�� ������ ��ũ��Ʈ�̸��� ����Ʈ�� ��ȯ

5.  target_sheet = target.get_sheet_by_name(target_sheets[0])
Ÿ�� ������ ��ũ��Ʈ ù° ���� ��ȯ

6. arget_company_nums = __class.read_vertical(target_sheet, list_start_range, list_end_range) 

llist ���� ���� ���� ����������(���ڱ� �� list_start_range?) �Ȱ��� Ÿ�� ��Ʈ�� ���� ��ȯ ����Ʈ��

12: check_form(db_company_nums)
    check_form(target_company_nums)
: ����Ʈ���� ������ check_form �Լ��� ���� ����� �����ش�.

13:dd = len(db_company_nums)

td = len(target_company_nums)

: �ּ��� ���� ���� db �� target �������� �ε��� ���̶� �Ѵ� (�Ʒ��� ���ϵ�)


14:
count_date = 0
count_12digits = 0
count_all = 0



15:
    for target_i in range(0, td):
        for db_i in range(0, dd):
            if str(db_company_nums[db_i])[0:8] == str(target_company_nums[target_i])[0:8]:

���� : Ÿ�ٰ��� db ���� ��ġ�� ������ ���Ѵ� ù 8��(index 7����)

                target_sheet['A' + str(target_i+int(list_start_range[1:]))].fill = PatternFill("solid", fgColor="DDFFDD")
                count_date = count_date + 1
                # print str(db_company_nums[db_i])[0:8]
                break
���� : ���� ���� Ÿ�ٰ��� ���ٸ� �հ� ĥ���ִ°� ���� index�� �ٽ� Ȯ���غ���. �׸��� c ount_date �� 1�� �����ش� �׸��� �ش� db�� 8�ڸ� ���


    target_sheet['F2'].fill = PatternFill("solid", fgColor="DDFFDD")
����: Ÿ���� �ش� F2 �ε��� ��(�Ƹ� F2 ���ε� )���� patternfill �� solid �� type ���� ��ĥ (�Ƹ� ����������? ������?)


16: ������ ���� 2�� �� ���� �����ٸ� Ÿ���� E2 D2�� �ٸ������� ��ĥ �ϰ� break 
ó���� ��¥��(count date) �ι�°�� 12(count 12) �ڸ� �� 3��°��(count all) �׳� ��

17: ��ĥ�� target�� D2 ���� count_all(����)�� E2 ���� count_12digits-count_all�� F2���� count_date - count_12digit
D2: ���� Ÿ�ٰ� ��ġ ('20170612 0000 -01)
E2: 12�� Ÿ�ٰ� ��ġ    ('20170612 0000)
F2: ��¥�� ��ġ     ('20170612 )
       

18:  __t = datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S") 
__t �� ���� ��¥ �ð��� ���� ���� ��������

19: file_name = __t + '_colored_result_for_' + db_file + '.xlsx'
    target.save(file_name)
��ĥ�� Ÿ�� ������ ��¥�� �÷���ٰ� �̸� ���̰� ����.


# color_db(__class, company, db):

1. load db file
    db_sheets = db.get_sheet_names()
    db_sheet = db.get_sheet_by_name(db_sheets[0])
    db_company_nums = __class.read_vertical(db_sheet, 'b5', 'b1104')

����: Ÿ���̶� �Ȱ��� �� ó�� ��Ʈ�� db_sheet�� �����Ѵ�. 

�׸��� db_company_nums �� b5������ b1104���� read_vertical �ǽ�


2. load list file
    company_sheets = company.get_sheet_names()
    company_sheet = company.get_sheet_by_name(company_sheets[0])
    company_company_nums = __class.read_vertical(company_sheet, 'a2', 'a580')
���� : company_company_nums �� company ù��Ʈ�� a2 ���� a580 ���� ����


3.  check_form(db_company_nums)
    check_form(company_company_nums)
���� �����ش�.


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

����: ���۴� ��Ʈ�� db�� ��¥ ���� ���ٸ� db�� B6 ? �ΰ��� ��ĥ�ϰ� db ��¥�� ���

������ 2���� �ڵ�� ���� 12 �ڸ� ���� �׸��� ���� ���� ��ĥ �ٵ� �� index�� �ٰ���? ���� ���ľ��ϳ�?

�׸��� �ð� �����ؼ� ��ĥ�� db ���� ����.