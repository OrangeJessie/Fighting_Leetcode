/*
 * @lc app=leetcode id=23 lang=cpp
 *
 * [23] Merge k Sorted Lists
 *
 * https://leetcode.com/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (33.93%)
 * Total Accepted:    373.7K
 * Total Submissions: 1.1M
 * Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
 *
 * Merge k sorted linked lists and return it as one sorted list. Analyze and
 * describe its complexity.
 * 
 * Example:
 * 
 * 
 * Input:
 * [
 * 1->4->5,
 * 1->3->4,
 * 2->6
 * ]
 * Output: 1->1->2->3->4->4->5->6
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/*
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty()) return NULL;
        int n = lists.size();
        while(n > 1) {
            int k = (n+1) /2;
            for(int i =0; i<n/2; ++i) {
                lists[i] = mergeTwoLists(lists[i],lists[i+k]);
            }
            n=k;
        }
        return lists[0];
        
    }
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy=new ListNode(-1),*cur=dummy;
        while(l1 && l2) {
            if(l1->val < l2->val) {
                cur->next = l1;
                l1 = l1->next;
            }
            else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        if(l1) cur->next=l1;
        if(l2) cur->next=l2;
        return dummy->next;
    }
};//分治
*/
class Solution {  
    public:  
        //Merge k Sorted Lists : heap sort  
        struct cmp {  
            bool operator() (ListNode *a,ListNode *b) {  
                return a->val > b->val;  
            }  
        };  
        ListNode *mergeKLists(vector<ListNode *> &lists) {  
            priority_queue<ListNode*,vector<ListNode*>,cmp> queue;  
            for(int i=0;i<lists.size();i++) {  
                if(lists[i]!=NULL) {  
                    queue.push(lists[i]);  
                }  
            }  
            ListNode *head=NULL,*prev=NULL,*temp;  
            while(!queue.empty()) {  
                temp=queue.top();  
                queue.pop();  
                if(prev==NULL) {  
                    head=temp;  
                }else {  
                    prev->next=temp;  
                }  
                prev=temp;  
                if(temp->next!=NULL) {  
                    queue.push(temp->next);  
                }  
            }  
            return  head;  
        }    
    };  //堆排序算法，最小堆

