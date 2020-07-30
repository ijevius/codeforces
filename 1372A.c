#include <stdio.h>
 
int main ()
{
    int t;
    int t_counter;
    scanf("%d", &t);

	int n;
    for (t_counter=0; t_counter<t; t_counter++){
        scanf("%d", &n);
        int array[n];
        int n_c;
        
        int temp;
        for(n_c=0; n_c<n; n_c++){     	        	
        	array[n_c] = 1;
		}
		
		for(n_c=0; n_c<n; n_c++){
        	printf("%d", array[n_c]);
        	if (n_c!=n-1){
        		printf(" ");
			}else{
				printf("\n");
			}
		}		
    }
 
    return 0;
}
