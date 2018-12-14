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
    bool isPalindrome(ListNode* head) {
        if(!head||!head->next) return true;
        ListNode* fast=head;
        ListNode* slow=head;
        while(fast->next&&fast->next->next)
        {
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode*last=slow->next,*pre=head;
        while(last->next)
        {
            ListNode*tmp=last->next;
            last->next=tmp->next;
            tmp->next=slow->next;
            slow->next=tmp;
        }
        while(slow->next)
        {
            slow=slow->next;
            if(pre->val!=slow->val) return false;
            pre=pre->next;
        }
        return true;
        
    }
};
//三部分，一部分找到链表终点位置，一部分对后半部分进行翻转，最后一部分进行比较
