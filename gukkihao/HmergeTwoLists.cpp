/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//解法１
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* res=new ListNode(-1);
        ListNode* cur=res;
        while(l1&&l2)
        {
            if(l1->val < l2->val)//小于号，不是大于号
            {
                cur->next=l1;//不是cur->val=li->val,因为cur首先指向res这个空链表
                l1=l1->next;
            }
            else
            {
                cur->next=l2;
                l2=l2->next;
            }
            cur=cur->next;//注意cur指针是要移动的
        }
        cur->next=l1?l1:l2;
        return res->next;//不是返回res或者cur，cur一直在移动，res头结点是空的，没有用
        
    }
};
//主要就是对比当前l1对应的值和l2,然后移动链表，注意要新建一个链表
//
//解法2,采用递归的方法做
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL) return l2;
        if(l2==NULL) return l1;
        if(l1->val < l2->val)
        {
            l1->next=mergeTwoLists(l1->next,l2); 
            return l1;
        }
        else
        {
            l2->next=mergeTwoLists(l1,l2->next);
            return l2;
        }
        
    }
};
