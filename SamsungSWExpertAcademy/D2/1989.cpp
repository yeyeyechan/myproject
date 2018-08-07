/*#include <iostream>
#include <string>
using namespace std;

int main() {

	int count;

	cin >> count;
	string lines;
	bool check ;
	for (int i = 0; i < count; i++) {
		check = true;
		cin >> lines;
		for (int j = 0; j < lines.size() / 2; j++) {
			if (lines.at(j) != lines.at(lines.size() - 1 - j)) {
					cout << '#' << i + 1 << ' ' << 0 << endl;
					check = false;
					break;
				}
			}
		if(check) cout << '#' << i + 1 << ' ' << 1 << endl;
		lines.clear();

		

	}


	return 0;
}*/