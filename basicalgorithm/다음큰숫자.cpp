#include<iostream>
#include <math.h>
using namespace std;

int nextBigNumber(int n)
{
	
	int jisu = 0;
	while (1) {
		if (n - pow(2,jisu) == 0) { break; }
		else if (n - pow(2, jisu) < 0) { jisu--; break; }
		jisu++;
	}
	int count = 1;
    int temp = n - pow(2, jisu);
	for (int i = jisu - 1; i >= 0; i--) {
		if (temp - pow(2, i)< 0) {
			if (temp != 0) continue;
			else if (temp == 0) break;
		}
		else if (temp - pow(2, i) > 0) {
			count++;
			temp -= pow(2, i);
		}
		else if (temp - pow(2, i) == 0) { count++;
		break; }
	}

	int count2 = 0;
	int jisu2 = 0;
	int newint = n;
	while (count != count2) {
		newint++;
		count2 = 0;
		jisu2 = 0;
		while (1) {
			if (newint - pow(2, jisu2) == 0) { break; }
			else if (newint - pow(2, jisu2) < 0) { jisu2--; break; }
			jisu2++;
		}
		count2 = 1;
		int temp2 = newint - pow(2, jisu2);
		for (int i = jisu2 - 1; i >= 0; i--) {
			if (temp2 - pow(2, i) < 0) {
				if (temp2 != 0) continue;
				else if (temp2 == 0) break;
			}
			else if (temp2 - pow(2, i) > 0) {
				count2++;
				temp2 -= pow(2, i);
			}
			else if (temp2 - pow(2, i) == 0) {
				count2++;
				break;
			}

		}
	}
	return newint;
}
/*int main()
{
	int n = 78;

	//아래는 테스트 출력을 위한 코드입니다.
	cout << nextBigNumber(n);
}*/