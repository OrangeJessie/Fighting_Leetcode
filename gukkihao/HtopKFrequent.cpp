// 桶排序，不是一种很严格的排序算法，只能用于整数
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int, int> m;//用于找某个元素出现的次数
        vector<vector<int> >tmp(nums.size()+1);//+1的原因是因为0-num.size()一共有n+1个数字
        vector<int> ans;
        for(int num : nums)   m[num]++;
        for(auto a: m)
        {
            tmp[a.second].push_back(a.first);//桶排序的主要排序，每一行只有一个元素，存放的是元素值。行值为出现的次数
        }
        for(int i=nums.size();i>=0;i--)
        {
            for (int j=0;j<tmp[i].size();j++)
            {
                ans.push_back(tmp[i][j]);
                if(ans.size()==k) return ans;
            }
        }
        return ans;
    }
};
//思想上和上面一样，采用了一个priority_queue的数据结构
//priority_queue<Type,Container,Functional>Type表示数据类型，Containner 表示
//保存数据的容器,必须是用数组实现的容器，例如pair, vector, deque不能用list,STL默认为vector
// Functional 为元素的比较方式,默认为operator <
//由以上可知，priority_queue的默认队列就是降序(大顶堆)
//https://www.cnblogs.com/Deribs4/p/5657746.html
class Solution {
    public: 
    vector <int> topKFrequent(vector<int> nums, int k) {
        unordered_map<int,int> m;
        vector<int>ans;
        for(int num : nums) m[num]++;
        priority_queue<pair<int,int> >q;
        for(auto a : m) q.push({a.second,a.first});
        for(int i=0;i<k;i++)
        {
            ans.push_back(q.top().second);
            q.pop();
        }
        return ans;
    }
};
