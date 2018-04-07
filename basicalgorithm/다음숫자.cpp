#include<iostream>
using namespace std;

int nextBigNumber(int n)
{
	int answer = 0;
	int jisu = 0;
	while (1) {
		if (n - 2 ^ (jisu) == 0) { break; }
		else if (n - 2 ^ jisu < 0) { jisu--; break; }
		jisu++;
	}
	int count = 1;
	int temp = n - 2 ^ (jisu);
	for (int i = jisu - 1; i >= 0; i--) {
		if (temp - 2 ^(i)< 0) {
			if (temp != 0) continue;
			else if (temp == 0) break;
		}
		else if (temp - 2 ^(i) > 0) { count++; temp -= 2 ^(i); }
		else if (temp - 2 ^(i) == 0) { count++; break; }
	}
	


	return count;
}
int main()
{
	int n = 78;

	//아래는 테스트 출력을 위한 코드입니다.
	cout << nextBigNumber(n);
}