#include <vector>
#include<algorithm>
#include <iostream>
#include <queue>

using namespace std;
int m;
int n;
int graph[50][50];
vector < vector<int>> check(50, vector<int>(50, 0));
//int check[50][50] = { {0,}, };
int move1[4][2] = { {0,-1},{-1,0},{0,1},{1,0} };
int x;
int y;
int count1 = 0;
int a;
int b;
int c;
int d;
pair<int,int> temp;
queue<pair<int, int>> q1;
vector<int> list1;

void checkfun() {
	if (check[x][y] != 1) {
		count1++;
		q1.push({ x, y });
		check[x][y] = 1;
		while (!q1.empty()) {
			temp = q1.front();
			q1.pop();
			a = graph[temp.first][temp.second] % 2;
			b = (graph[temp.first][temp.second] / 2) % 2;
			c = (graph[temp.first][temp.second] / 2) / 2%2;
			d = (graph[temp.first][temp.second] / 2) /2/ 2;
			if (a== 0) {
				if (check[move1[0][0] + temp.first][move1[0][1] + temp.second] != 1) {
					q1.push({ move1[0][0] + temp.first, move1[0][1] + temp.second});
					count1++;
					check[move1[0][0] + temp.first][move1[0][1] + temp.second] = 1;
				}
			}
			if (b== 0) {
				if (check[move1[1][0] + temp.first][move1[1][1] + temp.second] != 1) {
					q1.push({ move1[1][0] + temp.first, move1[1][1] + temp.second });
					count1++;
					check[move1[1][0] + temp.first][move1[1][1] + temp.second] = 1;
				}
			}
			if (c == 0) {
				if (check[move1[2][0] + temp.first][move1[2][1] + temp.second] != 1) {
					q1.push({ move1[2][0] + temp.first, move1[2][1] + temp.second });
					count1++;
					check[move1[2][0] + temp.first][move1[2][1] + temp.second] = 1;
				}
			}
			if (d== 0) {
				if (check[move1[3][0] + temp.first][move1[3][1] + temp.second] != 1) {
					q1.push({ move1[3][0] + temp.first, move1[3][1] + temp.second });
					count1++;
					check[move1[3][0] + temp.first][move1[3][1] + temp.second] = 1;
				}
			}
		}
	}
}
void checkif(int i, int j) {
	if (graph[i][j] / 2 != 0 || graph[i][j] % 2 != 0) {
		if(i==0 && j==0){}
		else if (i == 0 && j > 0&&j<m-1) {}
		else if (i == 0 && j==m - 1) {}
		else if (i >0 && j == 0 && i <n-1) {}
		else if (j == 0 && i ==n-1) {}
		else if (j == 0 && i == n - 1) {}
	}
}
int main() {
	cin >> m >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> graph[i][j];
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			x = i;
			y = j;
			checkfun();
			if (count1 != 0) {
				list1.push_back(count1);
			}
			count1 = 0;


		}
	}
	sort(list1.begin(), list1.end());
	cout << list1.back();
}