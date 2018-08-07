#include <iostream>

using namespace std;

int main() {
	int max;
	int maxint;
	int case_number;
	cin >> case_number;
	int case_count;
	int arrays[100];
	int case_index;
	for (int i = 0; i < case_number; i++) {
		for (int j = 0; j < 100; j++) {
			arrays[j] = 0;
		}
		cin >> case_count;
		for (int j = 0; j < 1000; j) {
			cin >> case_index;
			arrays[case_index - 1]++;
		}
		max = arrays[0];
		maxint = 0;
		for (int j = 1; j < 100; j++) {
			if (arrays[j] > max) {
				max = arrays[j];
				maxint = j;
			}
		}

		cout << '#' << case_count << ' ' << maxint + 1 << endl;
	}
}