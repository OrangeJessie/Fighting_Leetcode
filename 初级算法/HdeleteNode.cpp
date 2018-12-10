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
    void deleteNode(ListNode* node) {
        node->val=node->next->val;//把下一节点的值赋值给node
        node->next=node->next->next;//删除node的下一个节点，因为只关心val     
    }
};
//题目只给出了要删除的节点，所以无法对要操作的链表判断
