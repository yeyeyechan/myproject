#include<iostream>
#include<vector>
using namespace std;

int numOfPrime(int n)
{
	int answer = 0;


	if (n <= 0) return 0;
	for (int i = 1; i < n + 1; i++) {
		int j = 1;
		int count = 0;
		while (count <= 2&& j<=i) {

			if (i%j == 0) { count++;
			
			}
			j++;
		}
		if (count <= 2) answer++;
	}

	return answer;
}

/*int main()
{
	int testCase = 10;
	int testAnswer = numOfPrime(testCase);

	cout << testAnswer;
}*/
