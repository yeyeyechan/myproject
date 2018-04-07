#include<vector>
#include<iostream>

using namespace std;
vector<int> gcdlcm(int a, int b)
{
	vector<int> answer;
	int oria = a;
	int orib = b;
	int temp;
	if (a == b) { answer.push_back(a); answer.push_back(b); }
	else {
		while (1) {
			if (a > b&& a != 0 && b != 0) {
				temp = a - b;
				a = temp;
			}
			else if (b > a&& a != 0 && b != 0) {
				temp = b - a;
				b = temp;
			}
			else if (a == b) {
				answer.push_back(a);
				answer.push_back(oria / a * orib / a * a);
				break;

			}
		}
	}

	return answer;
}

/*int main()
{
	int a = 3, b = 12;
	vector<int> testAnswer = gcdlcm(a, b);

	cout << testAnswer[0] << " " << testAnswer[1];
}*/