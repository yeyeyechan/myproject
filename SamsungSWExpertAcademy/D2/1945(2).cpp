/*#include<iostream>

using namespace std;


int main() {

	int case_number;
	cin >> case_number;
	int that_number;
	int left;
	int a, b, c, d, e;
	for (int i = 0; i < case_number; i++) {
		a = b = c = d = e = 0;
		cin >> that_number;
		while (that_number != 1) {
			if (that_number % 2 == 0) {
				a++;
				that_number = that_number / 2;
			}
			if (that_number % 3 == 0) {
				b++;
				that_number = that_number / 3;
			}
			if (that_number % 5 == 0) {
				c++;
				that_number = that_number / 5;
			}
			if (that_number % 7 == 0) {
				d++;
				that_number = that_number / 7;
			}
			if (that_number % 11 == 0) {
				e++;
				that_number = that_number / 11;
			}
		}
		cout << '#' << i + 1 << ' ' << a << ' ' << b << ' ' << c << ' ' << d << ' ' << e << endl;
	}
}*/