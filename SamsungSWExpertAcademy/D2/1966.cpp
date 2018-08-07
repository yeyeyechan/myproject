/*#include <iostream>

using namespace std;
void make_line(int* arrays, int size) {
	int compare;
	int tmp;
	for (int i = 0; i < size; i++) {
		compare = arrays[i];
		for (int j = i+1; j < size; j++) {
			if (compare > arrays[j]) {
				arrays[i] = arrays[j];
				arrays[j] = compare;
				compare = arrays[i];
			}
		}
	}
}

int main() {


	int case_number;
	cin >> case_number;
	int numbers_line;
	int **arrays = new int*[case_number];
	for (int i = 0; i < case_number; i++) {
		cin >> numbers_line;
		arrays[i] = new int[numbers_line];
		for (int j = 0; j < numbers_line; j++) {
			cin >> arrays[i][j];
		}
		make_line(arrays[i], numbers_line);
		cout << '#' << i + 1 << ' ';
		for (int j = 0; j < numbers_line; j++) {
			cout << arrays[i][j]<< ' ';
		}
		cout << endl;
		
		
	}
	for (int i = 0; i < case_number; i++) {
		delete[] arrays[i];
	}
	delete[]arrays;
	return 0;
}*/