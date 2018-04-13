#include <iostream>
using namespace std;

int main() {
	int big = 45;
	int numbers[10] = { 45 ,20,60,35,10,55,90,85,75,25 };
	for (int i = 0; i < 10; i++) {
		if (big < numbers[i]) big = numbers[i];
	}

	cout << big;
	system("pause");
}