/*//날짜를 계산 하는 거란 다 

#include <iostream>

using namespace std;

int main() {

	int days_arrays[] = { 31,28,31,30,31,30, 31,31,30,31,30,31 }; // 날짜수를 담은 리스트 입니다.
	
	int case_number;
	cin >> case_number;
	int first_month, first_day, sec_month, sec_day;
	int  fir_days;
	int sum_days;
	for (int i = 0; i < case_number; i++) {

		cin >> first_month >> first_day >> sec_month >> sec_day;
		sum_days = 0;
		if (first_month == sec_month) {
			cout << '#' << i + 1 << ' ' << sec_day - first_day + 1 << endl;
		}
		else {
			fir_days = days_arrays[first_month - 1] + 1 - first_day;
			if(sec_month- first_month==1){ cout << '#' << i + 1 << ' ' << fir_days +sec_day<< endl; }
			else {
				for (int j =0; j < sec_month - first_month-1; j++) {
					sum_days += days_arrays[first_month+ j];
				}
				sum_days = sum_days + fir_days + sec_day;
				cout << '#' << i + 1 << ' ' << sum_days << endl;
			}
			
		}
	}

}*/