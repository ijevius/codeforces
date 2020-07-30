#include <iostream>
using namespace std;
int n, res;

int main(int argc, char *argv[])
{
	cin>>n;
	int arr[n];
	for(int n_c=0; n_c<n; n_c++){
		cin>>arr[n_c];
	}
	for (int k=1; k<n-1; k++){
		if ((arr[k-1]>arr[k] && arr[k+1]>arr[k])||
		(arr[k-1]<arr[k] && arr[k+1]<arr[k])){
			res+=1;
		}
	}
	cout<<res<<"\n";
}