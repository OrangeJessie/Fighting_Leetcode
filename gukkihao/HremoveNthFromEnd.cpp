/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* slow=head;
        ListNode* fast=head;
        while(n-->0)
        {
            fast=fast->next;
        }
        if(!fast) return head->next;//判断快指针是否到达链表最后
        while(fast->next)
        {
            fast=fast->next;
            slow=slow->next;
        }
        slow->next=slow->next->next;
        return head;
        
    }
};
//本题的主要方法还是快慢指针，但是注意一点快指针向前移动后
//一定要判断快指针时候是否到达链表最后，因为会出现这种情况
//链表长度为5,要删除的是倒数第5个节点。
