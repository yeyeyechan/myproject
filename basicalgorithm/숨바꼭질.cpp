/*#include <iostream>
#include <math.h>
using namespace std;
int n;
int m;
int G[100001];
int recursive(int a) {
	int min;
	if (a < 0) return 0;
	if (a == n) return 0;
	if (G[a]) return G[a];
	min = fmin(recursive(a - 1) + 1, recursive(a + 1) + 1);
	if (a % 2 == 0) { min = fmin(min, recursive(a / 2)+1); }
	G[a] = min;

	return min;
}

int main() {

	cin >> n;
	cin >> m;
	cout << recursive(m);


}*/