/*#include <iostream>
#include<algorithm>
#include<vector>

using namespace std;


int day;
int daypay[15][2];

vector<long long> list1;

void cal(int index, long long max) {
	

	for (int i = index; i <= day; i++) {
		if (i == day) {

		 list1.push_back(max);
		break;

			
		}
		else if (i < day) {
			if (i + daypay[i][0] < day) {
				max += daypay[i][1];

				i += daypay[i][0];
				cal(i, max);
			}
			else if (i + daypay[i][0] == day) {
		
					max += daypay[i][1];
					list1.push_back(max);
					break;
				
			}
			else if (i+ daypay[i][0] > day) {
				list1.push_back(max);
				break;
			}
		}
	}
	
}

int main() {
	int x;
	cin >> day;
	long long max;
	for (int i = 0; i < day; i++)
	{
		for (int j = 0; j < 2; j++) {
			cin >> x;
			daypay[i][j] = x;
		}
	}
	for (int i = 0; i < day; i++) {
		max = daypay[i][1];
		if (daypay[i][0] + i <= day) {
			cal(daypay[i][0] + i, max);
		}
		else if (daypay[i][0] + i > day) {
			list1.push_back(0);
		}
	}
	sort(list1.begin(), list1.end());

	cout << list1.back();

}*/