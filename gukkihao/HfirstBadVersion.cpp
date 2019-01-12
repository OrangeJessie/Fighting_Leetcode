bool isBadVersion(int version);
//二分法
class Solution {
public:
    int firstBadVersion(int n) {
        int left=1,right=n;
        while(left<right)
        {
            int mid = left + (right-left)/2;//mid=(right-left)/2超时
            if(!isBadVersion(mid)) left=mid+1;
            else right=mid;
        }
        return left;
    }
};
