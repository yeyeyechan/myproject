#include <iostream>
#include <vector>
using namespace std;
int n, m;
vector<vector<int>> fifo(n,vector<int>(m));
vector<vector<int>> check(n, vector<int>(m));
vector<int> wall;
int matrix[8][8];
vector<pair<int, int>> thelist;



void checking() {
	vector<pair<int,int>>::iterator iter;
	int row, col;
	for (iter =  thelist.begin(); iter != thelist.end(); iter++) {
		
		
	}

}

int main() {
	cin >> n;
	cin >> m;
	for (int i = 0; i < n; i++) {

		for (int j = 0; j < m; j++) {

			cin >> matrix[i][j];
			if (matrix[i][j] == 2) thelist.push_back(i, j);
		}
	}
	vector<pair<int,int>>::iterator iter;
	iter = thelist.begin();
	cout << *iter;


}