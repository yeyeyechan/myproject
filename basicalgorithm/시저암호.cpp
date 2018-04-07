#include<iostream>
#include<string>
using namespace std;

string caesar(string s, int n)
{
	string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	int alphasize = alpha.size();
	string answer = "";
	int ssize = s.size();
	for (int i = 0; i < ssize; i++) {
	
		if (s[i] == ' ') { continue; }
		else {
			int index1 = alpha.find(s[i]);
			int index2 = index1 + n;
			if (index1<=25) {
				if (index2 > 25) {
					s[i] = alpha[index2 % 26];
				}
				else {
					s[i] = alpha[index2];
				}

			}
			else if(index1 >=26) {
				if ((index2 - 26) <= 25) {
					s[i] = alpha[index2];
				}
				else {
					s[i] = alpha[(index2-26)%26+26];

				}
			}

		}

		
	}
	return s;
}
/*int main()
{
	string text = "a B z";
	int testNo = 4;

	string testAnswer = caesar(text, testNo);

	cout << testAnswer;
}*/