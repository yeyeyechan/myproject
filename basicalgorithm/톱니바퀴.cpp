/*#include <iostream>
#include <list>
#include<algorithm>
#include<math.h>
#include<utility>
#include <vector>
#include <string>
using namespace std;

vector<pair<int, int> >movelist;
vector<vector<int>> circle(4,vector<int>(8));



void check(int index, int direc) {
	movelist.push_back( make_pair(index , direc));
	int temp = index ;
	int temp2 = -1*direc;
	while (temp >= 1) {
		if (circle[temp][6] == circle[temp - 1][2]) {
			break;
		}
		else if (circle[temp][6] != circle[temp - 1][2]) {
			movelist.push_back( make_pair(temp-1,temp2));
			temp--;
			temp2 = temp2 * (-1);

		}
	}
	temp = index;
	temp2 = -1 * direc;
	while (temp <= 2) {
		if (circle[temp][2] == circle[temp+1][6]) {
			break;
		}
		else if (circle[temp][2] != circle[temp + 1][6]) {
			movelist.push_back(make_pair(temp+1, temp2));
			temp++;
			temp2 = temp2 * (-1);

		}

	}
}
void move(int index, int direc) {
	int temp;
	vector<int> ::iterator iter;
	if (direc == -1) {
	
		temp =circle[index][0];
		circle[index].erase(circle[index].begin());
		circle[index].push_back(temp);
	}
	else if (direc == 1) {
		iter = circle[index].begin();
		temp = circle[index][7];
		circle[index].pop_back();
		circle[index].insert(iter, temp );
	}
}

int main() {
	string x[4];
	for (int i = 0; i < 4; i++) { 
	cin >> x[i];
	
	for (int j = 0; j < 8; j++) {
		if (x[i][j] =='1') {
			circle[i][j] = 1;
		}
		else {
			circle[i][j] = 0;
		}
		}
	
	}

	int num;
	cin >> num;
	int index;
	int size;
	int direc;
	for (int i = 0; i < num; i++) {
		cin >> index;
		cin >> direc;
		check(index - 1, direc);
		size = movelist.size();
		/*for (int i = 0; i < size; i++) {
			move(movelist[i].first, movelist[i].second);
		}
		
		movelist.clear();
	}

	int total = 0;
	for (int i = 0; i < 4; i++) {

		if (circle[i][0] == 1)
		{
			if (i == 0)total += 1;

			else if (i == 1)total += 2;
			else if (i == 2) total += 4;
			else if (i == 3)total += 8;

		}

	}
	cout << total;
}*/