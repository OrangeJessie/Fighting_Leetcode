/*
分别把进位和不带进位的和相加，直到得到的进位为０，注意，负数的最高位是１，进行左移操作时会发生溢出现象
*/
class Solution {
public:
    int getSum(int a, int b) {
        int sum;
        int carry;
        carry=a&b;
        sum=a^b;
        while(carry){
            int temp=sum;
            carry=carry&(INT_MAX); //最高位为1即负数左移会报错, 使carry最高位永远为0
            sum=sum^(carry<<1);
            carry=temp&(carry<<1);
        }
        return sum;
    }
};
