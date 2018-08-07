/*#include <iostream>

using namespace std;

int main() {
	int case_number;

	int fee_of_A, fixed_fee_of_B, limited_liter_B, overfee_of_B, total_usage;

	cin >> case_number;
	for (int i = 0; i < case_number; i++) {

		cin >> fee_of_A >> fixed_fee_of_B >> limited_liter_B >> overfee_of_B >> total_usage;
		if (limited_liter_B <= total_usage) {
			if (fee_of_A*total_usage >= fixed_fee_of_B + overfee_of_B * (total_usage - limited_liter_B)) {
				cout << '#' << i + 1 << ' ' << fixed_fee_of_B + overfee_of_B * (total_usage - limited_liter_B )<< endl;
			}
			else {
				cout << '#' << i + 1 << ' ' << fee_of_A * total_usage  << endl;

			}
		}
		else {
			if (fee_of_A*total_usage >= fixed_fee_of_B ) {
				cout << '#' << i + 1 << ' ' << fixed_fee_of_B  << endl;
			}
			else {
				cout << '#' << i + 1 << ' ' << fee_of_A * total_usage << endl;

			}
		}
	}

}*/