#include <iostream>

using namespace std;

int main()
{
	int t, a_l, b_l;
	cin>>t;
	while(t--){
		cin>>a_l>> b_l;
		int a[a_l], b[b_l];
		for(int x=0; x<a_l; x++){
			cin >> a[x];
		}
		for(int x=0; x<b_l; x++){
			cin >> b[x];
		}
		bool found = false;
		for(auto x : a){
			for(auto y : b){
				if(x==y){
					found = true;
					cout<<"YES"<<endl;
					cout<< 1 << " " << x << endl;
					break;
				}
			}
			if(found){break;}
		}
		if(!found){
			cout<<"NO" <<endl;
		}
	}

    return 0;
}
