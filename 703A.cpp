#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{

    int n,a,b;
    int ca=0,cb=0;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>a>>b;
        if(a>b)ca++;
        else if(b>a)cb++;

    }

    if(ca>cb)cout<<"Mishka";
    else if(cb>ca)cout<<"Chris";
    else if(ca==cb)cout<<"Friendship is magic!^^";

    return 0;


}
