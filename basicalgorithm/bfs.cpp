#include<iostream>
#include<queue>
#include <vector>

/*using namespace std;
int qmatrix[100][100];
int visit[100];
queue<int> q;
int n;
int number = 0;
int virus() {
	int front = 1;
	q.push(front);
	visit[1] = 1;
	while (!q.empty()) {
		front = q.front();
		q.pop();
		for (int i = 1; i <= n; i++) {
			if (qmatrix[front][i] == 1 && !visit[i]) {
				visit[i] = 1;
				q.push(i);
				number++;
			}
		}

	}
	return number;
}
int main()
{

	int m;
	queue<int> q;
	cin >> n;
	cin >> m;
	int x;
	int y;
	for (int i = 0; i < m; i++) {
		cin >> x >> y;
		qmatrix[x][y] = 1;
		qmatrix[y][x] = 1;
	}

	cout << virus();


}*/