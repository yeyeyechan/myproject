/*#include <iostream>

using namespace std;

int main() {


	int count;
	int number;
	int sum;
	bool check;
	cin >> count;
	for (int i = 0; i < count; i++) {
		sum = 0;
		check = true;

		cin >> number;
		for (int j = 1; j <= number; j++) {
			if (check) { sum += j; 			check = false; }
			else { sum -= j;			check = true; }

		}
		cout << '#' << i + 1 << ' ' << sum << endl;
	}
	return 0;
}*/