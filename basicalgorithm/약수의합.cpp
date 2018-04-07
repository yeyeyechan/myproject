#include<iostream>
#include<vector>
using namespace std;
vector<int> dp;
int sumDivisor(int n)
{
	int div, left;
	for (int i = 0; i < n; i++) {
		div = n / (i + 1);
		left = n % (i + 1);
		if (left == 0 && div >= (i + 1)) {
			if (div == (i + 1)) {
				dp.push_back(div);
				break;
			}
			dp.push_back(i + 1);
			dp.push_back(div);

		}
		else if (div<i + 1) {
			break;
		}

	}
	int sum = 0;
	for (int j = 0; j <dp.size(); j++) {
		sum = sum + dp[j];

	}
	return sum;
}

/*int main()
{
	int testCase = 46293;
	int testAnswer = sumDivisor(testCase);

	cout << testAnswer;
}*/