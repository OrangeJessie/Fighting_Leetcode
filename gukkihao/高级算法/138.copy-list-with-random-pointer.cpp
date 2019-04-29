/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node *copyRandomList(Node *head) {
        if(!head) return NULL; 
        Node *ans = new Node(head->val,NULL,NULL);
        Node *node = ans;
        Node *cur = head->next;
        unordered_map<Node*, Node*> m;
        m[head] = ans;
        while (cur) {
            Node *tmp = new Node(cur->val,NULL,NULL);
            node->next = tmp;
            m[cur] = tmp;
            node = node->next;
            cur = cur->next;
        }
        node = ans;
        cur = head;
        while (cur) {
            if(!cur->random) node->random=NULL;
            node->random = m[cur->random];
            node = node->next;
            cur = cur->next;
            //}
        }
        return ans;
    }
};
