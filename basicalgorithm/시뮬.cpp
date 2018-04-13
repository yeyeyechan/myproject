#include<iostream>
#include<math.h>
#include <cmath>
#include <time.h>
using namespace std;

#define _USE_MATH_DEFINES
double smps (double(*f)(double), double a, double b, int n) {
	int i;
	double h = (b - a) / n, sum = 0;
	for (int i = 0; i < n; i++)sum += (f(a + i * h) + 4 * f(a + i * h + h / 2) + f(a + (i + 1)*h))*h / 6;
	return sum;
}
double function(double x) {
	return (1 / sqrt(2 * (3.14159265358979323)))*exp(-1 * pow(x, 2) / 2);
}
double Integral_Montecarlo(double(*f)(double) ,double a, double b, long n) {
	double avg = 0;
	double x;
	long i;
	srand(time(NULL));
	for (i = 0; i<n; i++) {
		x = ((double)rand() / RAND_MAX)*(b - a) + a;
		avg += (1 / sqrt(2 * (3.14159265358979323)))*exp(-1 * pow(x, 2) / 2);
	}
	avg = avg / n;
	return avg * (b - a);
}

int main() {
	double x;
	double integral = smps( &function , -1, 1, 100000);
	double monte = Integral_Montecarlo(&function, 0, 1, 100);
	cout << "실제값" << integral;
	cout << " 카를로" << 2 * monte;
}