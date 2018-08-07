/*#include <iostream>

using namespace std;
int make_postive(int number) {
	if (number < 0) {
		return -1 * number;
	}
	else return number;
}
int main() {

	int case_number;
	cin >> case_number;
	int counts;
	int count2;
	int max;
	int compare;
	for (int i = 0; i < case_number; i++) {
		cin >> counts;
		count2 = 0;
		max = 0;
		for (int j = 0; j < counts; j++) {
			if (j == 0) {
				cin >> max;
				max = make_postive(max);
				count2++;
			}
			else {
				cin >> compare;
				compare = make_postive(compare);
				if (compare < max) {
					max = compare;
					count2 = 1;
				}
				else if (compare == max) {
					count2++;
				}
			}
		}
		cout << '#' << i + 1 << ' ' << max << ' ' << count2 << endl;

	}

}*/
