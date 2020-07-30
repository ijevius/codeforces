#include <iostream>
 
using namespace std;
long x; 
 
void palindrome(long num) {
   int rev=0,val;
   val = num;
   while(num > 0) {
      rev = rev * 10 + num % 10;
      num = num / 10;
   }
   if(val==rev)
   cout<<"YES\n";
   else
   cout<<"NO\n";
}
 
int main(int argc, char *argv[])
{
	cin >> x;
	while (x%10==0){
		x /= 10;
	}
	palindrome(x);
}