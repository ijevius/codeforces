#include <stdio.h>

int isPrime(int number) {
    int i;
    for (i=2; i<number; i++) {
        if (number % i == 0 && i != number) return 0;
    }
    return 1;
}

int main ()
{
    int t;
    int t_counter;
    scanf("%d", &t);

    for (t_counter=0; t_counter<t; t_counter++){
        unsigned long long x, y;
        unsigned long long k;
        scanf("%llu", &x);
        scanf("%llu", &y);
        //printf("x=%llu and y=%llu\n", x, y);
        if (x-1==y){
            printf("NO\n");
            continue;
        }
        if (y==1 && x%2==1){
            printf("YES\n");
            continue;
        }
        int found = 0;
        for(k=0; k<x; k++){
            if (isPrime(k))
            {
                if ((x - y)/k % 1 == 0)
                {
                    //print((x-y)/k %1)
                    printf("YES\n");
                    found = 1;
                    break;
                }
            }
        }
        if (found==0){
            printf("NO\n");
        }
    }

    return 0;
}
