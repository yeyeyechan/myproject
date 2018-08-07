/*#include <iostream> 
using namespace std;
int find_high(int * arrays, int up, int down) {
	int sum, max;
	if (up >= down) {
		for (int i = 0; i <= up - down; i++) {
			sum = 0;
			for (int j = 0; j <+down; j++) {
				sum += (arrays[i+j] * arrays[up + j]);
			}
			if (i == 0) max = sum;
			else if (sum > max) {
				max = sum;

			}
		}
	}

	else if (up < down) {
		for (int i = up; i <= down; i++) {
			sum = 0;
			for (int j = 0; j < up; j++) {
				sum += (arrays[j+i] * arrays[j]);
			}
			if (i == up) max = sum;
			else if (sum > max) {
				max = sum;

			}
		}

	}
	return max;

}
int main() {
	int max;

	int case_number;
	cin >> case_number;
	int up, down;
	int** arrays = new int *[case_number];
	for (int i = 0; i < case_number; i++) {
		cin >> up >> down;
		arrays[i] = new int[up + down];
		for (int j = 0; j < up + down; j++) {
			cin >> arrays[i][j] ;
		}

		max = find_high(arrays[i], up, down);
		cout << '#' << i + 1 << ' ' << max << endl;



	}
	for (int i = 0; i < case_number; i++) {
		delete[] arrays[i];
	}
	delete[] arrays;
}*/