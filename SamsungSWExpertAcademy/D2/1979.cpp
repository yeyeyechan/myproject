/*#include <iostream>

using namespace std;

enum { black = 0, white };

int main() {

	int count;

	cin >> count;
	int size, len;
	int lengths;
	int height;
	int numbers;
	for (int i = 0; i < count; i++) {
		cin >> size >> len;
		int** arrays = new int*[size];
		for (int j = 0; j < size; j++) {
			arrays[j] = new int[size];
			for (int k = 0; k < size; k++) {
				cin >> arrays[j][k];
			}
		}
		height = 0;
		lengths = 0;
		numbers = 0;
		while (height < size) {
			lengths = 0;
			for (int k = 0; k < size; k++) {
				lengths = 0;
				if (arrays[height][k] == white) {
					lengths = 0;
					for (int z = k; z < size; z++) {

						if (arrays[height][z] == white) { lengths++; }
						else if (arrays[height][z] != white) { k = z; break; }


					}
				}
				if (lengths == len) {
					numbers++;
					if (k == size - len)
					{
						break;
					}
				}
				else {
					if (arrays[height][k] != white && k >= size - len) { break; }
					else if (arrays[height][k] == white) { break; }
				}


			}
			lengths = 0;
			for (int k = 0; k < size; k++) {
				lengths = 0;
				if (arrays[k][height] == white) {
					lengths = 0;

					for (int z = k; z < size; z++) {

						if (arrays[z][height] == white) { lengths++; }
						else if (arrays[z][height] != white) { k = z; break; }


					}
				}

				if (lengths == len) {

					numbers++;
					if (k == size - len) { break; }
				}
				else {
					if (arrays[k][height] != white && k >= size - len) { break; }
					else if (arrays[k][height] == white) { break; }
				}

			}
			height++;
		}
		cout << '#' << i + 1 << ' ' << numbers << endl;

		for (int j = 0; j < size; j++) {
			delete[] arrays[j];
		}
		delete[] arrays;

	}

	return 0;
}*/