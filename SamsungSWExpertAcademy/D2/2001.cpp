/*#include <iostream>

using namespace std;

int main() {
	int testnum;
	cin >> testnum;
	int size;
	int tapsize;
	int sum , max ;
	int height;
	for (int i = 0; i < testnum; i++)
	{
		cin >> size >> tapsize;
		int** arrays = new int* [size];
		for (int j = 0; j < size; j++) {
			arrays[j] = new int[size];
			for (int k = 0; k < size; k++) {
				cin >> arrays[j][k];
			}
		}


		max = 0;
		for (int j = 0; j <= size-tapsize; j++) {
			for (int k = 0; k <= size - tapsize; k++) {
				sum = 0;
				height = 0;
				while (height !=tapsize) {
					for (int z = k; z < k + tapsize; z++) {
						sum += arrays[j+height][z];
					}
					height++;
				}
				if (max < sum) max = sum;
			}
		}
		cout << '#' << i + 1 << ' ' << max << endl;
		for (int j = 0; j < size; j++) {
			delete[] arrays[j];
		}
		delete[] arrays;


	}



	return 0; 
}*/