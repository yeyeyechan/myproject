#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;
long long gcd(long long a, long long b) {
	if (b == 0) {
		return a;
}
	else {
		gcd(b, a%b);
	}

}
long long nlcm(vector<int> num)
{
	int number;
	long long answer = num[0];
	long long high;
	long long low;
	int numsize = num.size();
	for (int i = 1; i < numsize; i++) {
		number = num[i];
		high = fmax(answer, number);
		low = fmin(answer, number);
		answer = high * low / gcd(high, low);
	}

	return answer;
}

int main()
{
	vector<int> test{ 2,6,8,14 };

	// 아래는 테스트로 출력해 보기 위한 코드입니다.
	cout << nlcm(test);
}
