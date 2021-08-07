#include<bits/stdc++.h>
using namespace std;


int a[10000];
int stree[10000];


int build(int s,int e,int index)
{
    if(s==e)
    {
       stree[index]=a[s];
       return a[s];

    }

    int mid=s+(e-s)/2;

    int left=build(s,mid,index*2);
    int right=build(mid+1,e,index*2+1);

    stree[index]=min(left,right);

    return stree[index];

}


int query(int index,int s,int e,int ql,int qr)
{
    if(ql>=s and qr<=e)
        return stree[index];

     if(ql<s||qr>e)
        return INT_MAX;

    int mid=s+(e-s)/2;

    int left=query(index*2,s,mid,ql,qr);

    int right=query(index*2+1,mid+1,e,ql,qr);

    return min(left,right);

}


int main(){

        int t;
        cin>>t;

        int kase=0;

        while(t--)
        {
            int n,q;

            cin>>n>>q;


            for(int i=1;i<=n;i++)cin>>a[i];

            build(1,1,n);

            kase++;

            cout<<"Case "<<kase<<": "<<endl;

            for(int u=0;u<q;u++)
            {

               int a,b;

               cin>>a>>b;

               cout<<query(1,1,n,a,b)<<endl;
            }

        }

}
