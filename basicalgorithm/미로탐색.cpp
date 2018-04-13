/*#include<iostream>
#include<queue>
#include <string>
using namespace std;
int n;
int m;
int qmatrix[101][101];
int visit[101][101];
typedef struct moving {
	int x;
	int y;
}mv;

int move() {
	queue<mv> q;
	mv index = { 1,1 };
	mv temp;
	q.push(index);
	visit[index.x][index.y] = 1;
	while (!q.empty()) {
		index = q.front();
		q.pop();
		if (index.x + 1 <= n && visit[index.x + 1][index.y] != 1 && qmatrix[index.x + 1][index.y] == 1) {
			qmatrix[index.x + 1][index.y] += qmatrix[index.x][index.y];
			temp = { index.x + 1 ,index.y };
			q.push(temp);
			//cout << index.x << index.y << "에서" << temp.x <<temp.y << "로" << endl;
		}
		if (index.x-1 >=1 && visit[index.x -1][index.y] != 1 && qmatrix[index.x-1][index.y] == 1) {
			qmatrix[index.x -1][index.y] += qmatrix[index.x][index.y];
			temp = { index.x -1 ,index.y };
			q.push(temp);
			//cout << index.x << index.y << "에서" << temp.x << temp.y << "로" << endl;
		}
		if (index.y-1 >=0 && visit[index.x ][index.y-1] != 1 && qmatrix[index.x][index.y-1] == 1) {
			qmatrix[index.x][index.y-1] += qmatrix[index.x][index.y];
			temp = { index.x ,index.y-1 };
			q.push(temp);
		}
		if (index.y+1<=m && visit[index.x ][index.y+1] != 1 && qmatrix[index.x][index.y+1] == 1) {
			qmatrix[index.x ][index.y+1] += qmatrix[index.x][index.y];
			temp = { index.x ,index.y +1};
			q.push(temp);
		}
	}
	return qmatrix[n][m];
}

int main() {

	int x;
	cin >> n;
	cin >> m;
	string line;

	for (int i = 1; i <= n; i++) {
		cin >> line;
		for (int k = 1; k <= line.length(); k++) {
			if(line[k-1]=='1') {qmatrix[i][k] = 1;}
			else{qmatrix[i][k]=0;}
			




		}
	}
	cout << move();


}*/