/*
class Solution {
public:
    double myPow(double x, int n) {
        if(n<0) return double (1/power(x, -n));
        return power(x,n);
    }
    double power(double x,int n)
    {
        if(n==0) return 1;
        if(x==1) return 1;
        double half=power(x,n/2);
        if(n%2==0) return half*half;
        else return x*half*half;
    }
};
*/
class Solution {
public:
    double myPow(double x, int n) {
       if(x==1||n==0) return 1;
       int tmp=n/2;
        double half= myPow(x,tmp);
        if(n%2==0)
        {
            return half*half;
        }
        if(n>0)
        {
            return half*half*x;
        }
        return half*half/x;
    }
};
