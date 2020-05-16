#include <stdio.h>

int minusone(long f){
  if(f%10==0){
    return f/10;
  }else{
    return f-1;
  }
}

int main(int argc, char** argv) {
	long n, k;
	long m, res;
	scanf("%d", &n);
	scanf("%d", &k);
	res = n;
	for (m=0; m<k; m++){
          res = minusone(res);
	}
	printf("%d",res);
	return 0;
}
