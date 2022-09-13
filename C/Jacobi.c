#include <stdlib.h>
#include <stdio.h>

#define NUMROWS 3
#define NUMCOLS 4

void print_matrix(double m[NUMROWS][NUMCOLS])
{
    for (int i = 0; i < NUMROWS; i++)
    {
        for (int j = 0; j < NUMCOLS; j++)
        {
            printf("%.8f\t", m[i][j]);
        }
        printf("\n");
    }
}
void jacobi(double E[NUMROWS][NUMCOLS], double chute[NUMROWS], int n)
{
    int iterations[] = {4, 6, 8, 12, 13, 14, 16 , 19};
    int i2 = 0;
    int achou = 0;
    FILE *fp = fopen("out.txt", "w+");
    for (int i = 0; i < n; i++)
    {
        double resp[NUMROWS] = {};
        for (int j = 0; j < NUMROWS; j++)
        {
            double bj = E[j][NUMCOLS - 1];
            double soma = 0;
            for (int k = 0; k < NUMCOLS - 1; k++)
            {
                if (k != j)
                {
                    soma += E[j][k] * chute[k];
                }
            }
            double xj = (bj - soma) / E[j][j];
            resp[j] = xj;
            if (i+1 == iterations[i2])
            {
                fprintf(fp, "%.16f,\t", xj);
                achou = 1;
            }
        }
        if (achou == 1)
        {
            i2 += 1;
            achou = 0;
        }
        printf("\n");
        for (int i = 0; i < NUMROWS; i++)
        {
            chute[i] = resp[i];
        }
    }
}

int main(void)
{

    double E[NUMROWS][NUMCOLS] =
        {-7.57, -1.42, 4.15, -1.71,
         0.66, 6.13, 3.49, 0.04,
         0.29, 2.42, -4.7, 4.51};
    print_matrix(E);

    double chute[NUMROWS] = {2.1,0.79,3.6};
    jacobi(E, chute, 30);
    print_matrix(E);
    return 0;
}