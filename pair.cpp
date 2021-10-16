
#include<cstdio>
#include<algorithm>
using namespace std;


int main()
{
    register long long n;

    scanf("%lld",&n);

    register long long as[n];

    for(long long i=0;i<n;i++)scanf("%lld",&as[i]);

    long long cnt=0;

    long long mina=*min_element(as,as+n);

    for(long long i=1;i<=mina;i++)
    {
        bool yk=true;
      for(long long j=0;j<n;j++)
      {


        if(as[j]%i!=0)
        {
            yk=false;
            break;
        }

      }
        if(yk==true)
            cnt++;

    }


    printf("%lld\n",cnt);

}
