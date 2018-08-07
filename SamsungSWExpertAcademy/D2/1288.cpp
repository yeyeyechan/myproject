/*#include <iostream>

using namespace std;

int check(int arrays[], int count, int the_number) {
	bool check = true;
	do {
		check = true;
		for (int i = 0; i < 10; i++) {
			if (the_number % 10 == arrays[i]) {
				check = false;
			}
		}
		if (check) {
			arrays[count] = the_number % 10;
			count++;
		}
		the_number = the_number / 10;

	} while (the_number!=0);
	return count;

}
int main() {

	int case_number;
	cin >> case_number;
	int the_number;
	int arrays[10] ;
	int count;
	int times;
	int new_number;
	for (int i = 0; i < case_number; i++) {
		for (int j = 0; j < 10; j++) {
			arrays[j] = -1;
		}
		count = 0;
		cin >> the_number;
		times = 1;
		while (count != 10) {
			new_number = the_number * times;
			times++ ;
			count = check(arrays, count, new_number);

		}
		cout << '#' << i + 1 << ' ' << new_number << endl;


	}
}*/