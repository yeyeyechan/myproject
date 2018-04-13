/*#include <iostream>
#include <queue>
#include <utility>
using namespace std;
int visit[1000001] = { false };
int fin;
int cur;
pair<int,int> befor;
queue<pair<int, int>> q;
int move(int from, int to) {
	int cnt = 0;
	q.push({ from, cnt });
	while (!q.empty()) {
		befor = q.front();
		q.pop();
		cur= befor.first;
		cnt = befor.second;
		if (cur < 0 || cur>100000) continue;
		if (visit[cur]) continue;
		visit[cur] = true;
		if (cur == to)return  cnt;

		q.push({ cur - 1, cnt + 1 });
		q.push({cur + 1, cnt + 1});
		q.push({ cur*2, cnt + 1 });



	}


}
int main() {
	int n;
	int m;
	cin >> n;

	cin >> m;

	cout << move(n, m);
}*/