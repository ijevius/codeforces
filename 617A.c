#include <stdio.h>
 
int main(int argc, char** argv) {
	int x;
	scanf("%d", &x);
	int result = 0;
	int x5 = x/5;
	result = x5;
	if(x%5 != 0){
          result += 1;
	}
	printf("%d", result);
	return 0;
}
