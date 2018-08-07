/*#include <iostream>
#include <string>
using namespace std;
void make_clap(int number) {
	string clap;
	int divide = number / 10;
	int left = number % 10;
	do {
		if (left == 3 || left == 6 || left == 9) {
			clap = clap + "-";
		}
		left = divide % 10;
		divide = divide / 10;

	} while ((left != 0 || divide != 0));
	if (clap == "") {
		cout << number<<' ';
	}
	else {
		cout << clap<< ' ';
	}

}

/*int main() {

	int last;
	string clap;
	cin >> last;
	for (int i = 1; i <= last; i++) {
		make_clap(i);
	}

	return 0;
}*/
\
