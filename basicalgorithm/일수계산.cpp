#include<iostream>
#include<string>
using namespace std;

string getDayName(int a, int b)

{
	int d = 0;
	int days[] = { 31, 28 , 31,30,31,30,31,31,30,31,30,31 };
	string dayss[] = { "SUN","MON","TUE","WED","THU","FRI","SAT" };
	for (int i = 0; i < a - 1; i++) {
		d += days[i];

	}
	int totald = d + b;
	int left = totald % 7;


	string answer = dayss[left];

	return answer;
}
/*int main()
{
	int a = 5, b = 24;

	//아래는 테스트 출력을 위한 코드입니다.
	cout << getDayName(a, b);
}*/
