/*#include <iostream>
#include <vector>
using namespace std;

vector<vector<vector<int>>> diceform = { {{ 1,4,3,5,2,6 },{ 1,2,5,4,3,6 },{ 1,5,2,3,4,6 },{ 1,3,4,2,5,6 } },
{ { 2,4,3,1,6, 5 },{ 2,6,1,4,3,5},{ 2,3,4,6,1, 5 },{ 2,1,6,3,4,5 }},{
	{3,2,5,1,6,4}, {3,6,1,2,5,4},{3,5,2,6,1,4},{3,1,6,5,2,4}},
{{4,6,1,5,2,3},{4,2,5,6,1,3},{4,1,6,2,5,3},{4,5,2,1,6,3}},
{{5,4,3,6,1,2},{5,1,6,4,3,2},{5,3,4,1,6,2},{5,6,1,3,4,2}},
{{6,4,3,2,5,1},{6,5,2,4,3,1},{6,3,4,5,2,1},{6,2,5,3,4,1}} };
vector<int> dice1= { 0,0,0,0,0,0 };
int distance2[4][2]={ {0,1},{ 0, -1 },{ -1,0 },{ 1,0 } };
int r;
int c;
int n;
int m;
int count1;
int top=1;
int beforetop;
int a = 0;
int direc;
int graph[20][20];

void move() {
	beforetop = top;


	if (graph[r][c] != 0) {
		top = diceform[top-1][a][direc];
		for (int i = 0; i < 4; i++) {
			if (diceform[top - 1][i][direc] == (7 - beforetop)) {
				a = i;
				break;
			}
		}
		dice1[diceform[top-1][a][5]-1] = graph[r][c];
		graph[r][c] = 0;

	}
	else if (graph[r][c] == 0) {
		top = diceform[top - 1][a][direc];
		for (int i = 0; i < 4; i++) {
			if (diceform[top - 1][i][direc] == (7 - beforetop)) {
				a = i;
				break;
			}
		}
		graph[r][c] = dice1[diceform[top - 1][a][5] - 1];
		
	}
}

bool checkgraph() {
	if (distance2[direc - 1][0] + r >= 0 && distance2[direc - 1][1] + c >= 0 && distance2[direc - 1][0] + r < n && distance2[direc - 1][1] + c < m) {
		r = r + distance2[direc - 1][0];
		c = c + distance2[direc - 1][1];
		return true;
	}
	else return false;
}

int main() {

	cin >> n;
	cin >> m;
	cin >> r;
	cin >> c;
	cin >> count1;
	int x;
	for (int i = 0; i < n; i++)
	{
		for (int k = 0; k < m; k++) {
			cin >> x;

			graph[i][k] = x;
		}
	}
	for (int i = 0; i < count1; i++) {

		cin >> direc;
		if (checkgraph())
		{
			move();
			
			cout << dice1[top - 1] << endl;
		}

	}
	
}*/
