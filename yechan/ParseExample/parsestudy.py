
# 명령창 에서 pip install argparse 를 한다.

import argparse

# 그 후 파서를 선언하고 명령행 인자를 파싱하는 메소드를 이용하여 파싱을 수행한다.

parser = argparse.ArgumentParse()
parser.add_argument("echo")
args=parser.parse_args()
print (args.echo)

# python test.py -h or --help 를 통해 명령행 인자와 그에 대한 설명을 확인 할 수 있다.

#명령행 인자를 추가한 경우, 아무 인자가 주어지지 않았을때에 에러가 출력된다. help 를 통해 설명을 함께 출력할 수 있다.

parser.add_argument("echo",  help = "ehco the string you use here")

# 기본적으로 인자의 타입은 스트링으로 지정이 되는데 인자의 타입을 스트링이 아닌 다른 타입으로 지정하고 싶은경우에는 다음과 같이 지정할 수 있다.

parser.add_argument("square", help ="display a square of a given number", type = int)
args = parser.parse_args()
print(args.square**2)

# 위치 인자가 아닌 선택인자는 다음과 같이 추가한다.

parser.add_argument("--verbosity", help ="increase output verbosity")
if args.verbosity:
    print("verbosity turned on")


#python test.py--verbosity 1 -> verbosity turned on