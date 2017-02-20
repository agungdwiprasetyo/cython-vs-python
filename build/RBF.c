#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main()
{
	int N = 1000;
	int D = 5;
	int theta = 10;
	double r = 0;
	double X[N][D];
	double beta[N];
	double Y[N];
	for (int i = 0; i < N; i++){
		for (int j = 0; j < D; j++){
			X[i][j] = (rand() % 1000)/1000.0;
		}
		beta[i] = (rand()%1000)/1000.0;
		Y[i] = 0;
	}

	// start rbf
	clock_t mulai = clock(); // mulai timer
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++){
			r = 0;
			for (int d = 0; d < D; d++){
				r += pow((X[j][d] - X[i][d]),2);
			}
			r = sqrt(r);
			Y[i] += beta[j] * exp(-pow((r * theta),2));
		}
	}
	clock_t finish = clock(); // stop timer
	double T = (double)(finish - mulai) / CLOCKS_PER_SEC;
	printf("%f\n", T);
	return 0;
}