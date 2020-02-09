#include <iostream>
using namespace std;

int main(){
    int n,k,q;
    cin >> n >> k >> q;
    int s[n];
    int d[n];
    int c=0;
    int act[k];

    int min,mindex;
    min = -9;

    for(int i=0;i<n;i++){
        cin >> s[i];
        d[i]=0;
        if(i<k)act[i]=-1;
    }

    for(int i=0;i<q;i++){
        int qu,id;
        cin >> qu >> id;
        if(qu==1){
            if(min==-9){
                d[id-1]=1;
                min = s[id-1];
                mindex = 0;
                act[c]=id-1;
                c++;
            }
            else if(c<k){
                d[id-1]=1;
                act[c]=id-1;
                c++;
                if(min>s[id-1]){
                    min = s[id-1];
                    mindex = id-1;
                }
            }
            else if(min < s[id-1] && c>=k){
                d[mindex]=0;
                act[mindex]=id-1;
                d[id-1]=1;
                int temp = s[act[0]];
                for(int p=0; p<k; p++) {
                    if(temp>s[act[p]] && act[p]!=-1) {
                        min=s[act[p]];
                        mindex=act[p];
                    } 
                    }
            }
        }

        if(qu==2){
            if(d[id-1]==0)cout<<"NO\n";
            if(d[id-1]==1)cout<<"YES\n";
        }
    }
    return 0;
}
