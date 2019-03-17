/*
注意两个相同种类的任务之间至少有长度为n的冷却时间，因此至少有连续n个单位时间内CPU在执行不同的任务或者在待命状态
*/
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int>cnt(26,0);
        for(char task : tasks)
        {
            ++cnt[task-'A'];
        }
        sort(cnt.begin(),cnt.end());
        int i=25,mx=cnt[25],len=tasks.size();
        while(i>=0&&mx==cnt[i]) --i;
        return max(len,(mx-1)*(n+1)+25-i);
    }
};
