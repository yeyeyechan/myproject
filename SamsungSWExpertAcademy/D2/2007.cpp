/*#include <iostream>
#include <string>
using namespace std;

int main() {
	int count;
	cin >> count;
	for (int j = 0; j < count; j++) {
		int numbers;
		cin >> numbers;
		int** arrays = new int*[numbers];
		cout << '#' << j + 1 << endl;
		for (int i = 0; i < numbers; i++) {
			arrays[i] = new int[i + 1];
			if (i == 0) { arrays[i][0] = 1; cout << 1 << endl; }
			else if (i == 1) { arrays[i][0] = 1; arrays[i][1] = 1; cout << 1 << ' ' << 1 << endl; }
			else {
				for (int k = 0; k < i + 1; k++) {
					if (k == 0) { arrays[i][k] = 1; cout << 1 << ' '; }
					else if (k == i) {
						arrays[i][k] = 1; cout << 1 << ' ' << endl;
					}
					else {
						arrays[i][k] = arrays[i - 1][k - 1] + arrays[i - 1][k];
						cout << arrays[i][k] << ' ';
					}
				}
			}



		}
		for (int i = 0; i < numbers; i++) {
			delete[] arrays[i];
	}
		delete[] arrays;

	}
	return 0;
}*/
