/*#include <iostream>
#include <queue>
#include <string>
#include <utility>
using namespace std;
queue<pair<int , int>> q;
int n;
int m;
int countday = 0;
int totalcount = 0;
int totalsize = 0;
int startroat = 0;
int startfresh = 0;
int qmatrix[1001][1001];
int visit[1001][1001];
int virus() {
	if (startroat == totalcount) return 0;
	pair<int,int> front;
	int size = q.size();
	while (!q.empty()) {
		size = q.size();
		totalsize += size;
		if (totalcount == totalsize) { return countday; }
		while (size != 0) {
			front = q.front();
			q.pop();
			if (front.first - 1 >= 1 && qmatrix[front.first - 1][front.second] == 0 && visit[front.first - 1][front.second] != 1) {
				visit[front.first - 1][front.second] = 1;
				q.push(make_pair(front.first - 1, front.second));

			}
			if (front.second - 1 >= 1 && qmatrix[front.first][front.second - 1] == 0 && visit[front.first][front.second - 1] != 1) {
				visit[front.first][front.second - 1] = 1;
				q.push(make_pair(front.first, front.second - 1));

			}
			if (front.first + 1 <= m && qmatrix[front.first + 1][front.second] == 0 && visit[front.first + 1][front.second] != 1) {
				visit[front.first + 1][front.second] = 1;
				q.push(make_pair(front.first + 1, front.second));

			}
			if (front.second + 1 <= n && qmatrix[front.first][front.second + 1] == 0 && visit[front.first][front.second + 1] != 1) {
				visit[front.first][front.second + 1] = 1;
				q.push(make_pair(front.first, front.second + 1));

			}
			size--;
			

		}
		countday++;
		
	

	
	}
	return -1;

}
int main() {
	cin >> n;
	cin >> m;
	int x;

	for (int i = 1; i <= m; i++) {
		for (int k = 1; k <= n; k++) {
			cin >> x;
			qmatrix[i][k] = x;
			if (x == 1) { startroat += 1; q.push(make_pair(i, k)); }
			else if (x == 0) { startfresh += 1; }
		}
	}
	totalcount = startfresh + startroat;

	cout << virus();
}*/