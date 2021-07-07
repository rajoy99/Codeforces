#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int ar[100];
    for(int i=1;i<=n;i++)cin>>ar[i];

    for(int i=1;i<=n;i++)
    {
    for(int j=1;j<=n;j++)
        {

            if(ar[i]==j)
            {ar[j]=i;
            }
        }

    }

    for(int i=1;i<=n;i++)cout<<ar[i]<<" ";

    }













