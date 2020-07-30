#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int ar [n][n];
    int i,j;
    int d;
    for (i=0; i<n; i++){
        for(j=0; j<n; j++){
            scanf("%d", &ar[i][j]);
        }
    }
    int total = 0;
    for (d=0; d<n; d++){
        total = total + ar[d][d]+ar[d][n-1-d] + ar[((n+1)/2)-1][d] + ar[d][((n+1)/2)-1];
    }

    printf("%d", total-(3*ar[((n+1)/2)-1][((n+1)/2)-1]));
    return 0;
}
