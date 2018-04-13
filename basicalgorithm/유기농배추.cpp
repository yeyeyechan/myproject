#include <iostream>
#include<utility>
#include<queue>
using namespace std;
int graph[50][50];//queue 1개  배추심어져있
queue<pair<int, int>> q1;
queue<pair<int, int>> q2;
pair<int, int> front;
int count;
int checkcount;
int visit[50][50];
int move[4];
bool check(pair<int,int> a) {
	
}
int countt(){
	front = q1.front();
	q1.pop();
	q2.push(front);

	while (!q2.empty()) {
		q2.pop();
		// if break;
		for (int i = 0; i < 4; i++) {
			//front 초기화 thorough move (check를 통과 못할시 continue
			//if check graph==1 visit!=1
			//  visit =1 , push cekcount++
		}
	}



}
int main() {
	int testcase;
	cin >> testcase;
	int row;
	int col;
	int num;
	int x;
	for (int i = 0; i < testcase; i++) {
		cin >> row >> col >> num;
		for (int k = 0; k < row; k++ ) {

			for (int j = 0; j < col; j++) {
				cin >> x;
				graph[i][k] = x;
				if (x == 1) {
					q1.push({ i,k });
					count += 1;
				}
			}
		
		}
		cout << countt() << endl;

	}
}