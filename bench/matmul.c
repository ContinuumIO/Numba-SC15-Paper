void c_matmul(double matA[], double matB[], double matC[], int m, int n, int p)
{
  int i, j, k;
  for ( i=0; i < m; ++i ) {
    for ( j=0; j < n; ++j ) {
      double tmp = 0;
      for ( k=0; k < p; ++k ) {
        tmp += matA[i * m + k] * matB[k * p + j];
      }
      matC[i * m + j] = tmp;
    }
  }
}
