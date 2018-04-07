#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int getMinSum(vector<int> A, vector<int> B)
{
	int answer = 0;
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	int bsize = B.size();
	for (int i = 0; i < bsize; i++) {
		answer += A[i] + B[bsize - (i + 1)];

	}

	return answer;
}
/*int main()
{
	vector<int> tA{ 1,2 }, tB{ 3,4 };

	//�Ʒ��� �׽�Ʈ ����� ���� �ڵ��Դϴ�.
	cout << getMinSum(tA, tB);
}*/