class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow=head;
        ListNode *fast=head;
        while(fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if (slow==fast) return true;
        }
        return false;
        
    }
};
//快慢指针的典型用法，如果有环，则快慢指针会相等
//若不相等，则快指针会率先到达终点并结束循环
