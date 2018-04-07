#include<iostream>
#include<vector>
using namespace std;

vector<vector<int> > sumMatrix(vector<vector<int> >A, vector<vector<int> >B)
{
	vector<vector<int> > answer (A.size(), vector<int>(A[0].size())) ;
	if (A.size() == B.size() && !A.empty()) {
		for (int i = 0; i<A.size(); i++) {
			for (int j = 0; j<A[0].size(); j++) {
				answer[i][j] = A[i][j] + B[i][j];
			}
		}
	}

	return answer;
}
/*int main()
{
	vector<vector<int> > a{ { 1,2 },{ 2,3 } }, b{ { 3,4 },{ 5,6 } };
	vector<vector<int> > answer = sumMatrix(a, b);
	cout << a.size();
	cout << a[0].size();
	for (int i = 0; i<answer.size(); i++)
	{
		for (int j = 0; j<answer[0].size(); j++)
		{
			cout << answer[i][j] << " ";
		}
		cout << "\n";
	}
}*/
