/*解法一，定义一个当前节点和当前节点的上一节点和下一节点
pnow pnext ppre;pnext和ppre负责记录pnow的上下节点便于pnow
移动
*/
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode*pnow=head;//定义当前节点指针
        ListNode*pnext=NULL;//定义前驱节点指针
        ListNode*ppre=NULL;//定义后继节点指针
        ListNode*tail=NULL;//定义尾指针
        while(pnow!=NULL)//开始遍历链表
        {
            pnext=pnow->next;//如果当前指针不是空指针，那么初始化pnext指针
            if(pnext==NULL)
            {
                tail=pnow;//如果找到尾节点，初始化tail指针
            }
            pnow->next=ppre;//翻转链表，当前节点的next指针指向前一个节点，实现链表方向反转，发生断链
            ppre=pnow;//处理断链情况，pre后移一个节点
            pnow=pnext;//pnow后移一个节点
        }
        return  tail;
    }
};
/*解法二，在head前面添加dummy节点，把head后的节点一次加到dummy后
*/
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head) return head;
        ListNode* dummy=new ListNode(-1);
        dummy->next=head;//定义dummy节点，后继节点为head
        ListNode* cur=head;//定义head节点别名
        while(head->next)//head如果后面节点为空，说明完成遍历
        {
            ListNode* tmp=cur->next;//定义原head->next节点别名
            cur->next=tmp->next;//head节点后继节点改为后继的后继
            tmp->next=dummy->next;//将原head->next的后继节点改为head
            dummy->next=tmp;//将原head->next的前驱节点改为dummy;
            
        }
        return dummy->next;
    }
};
/*方法三*/
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
       if(!head||!head->next) return head;
        ListNode* p=head;
        head=reverseList(p->next);//先翻转后面的链表，并走到链表的后面
        p->next->next=p;//将当前节点设为下一节点的后续节点
        p->next=NULL;//
        return head;
    }
};
/*关于递归的操作其实分两部分，首先类似于栈的先进后出FILO原则执行递归操作
一直到达链表的最末尾也就是if语句判断部分，进去之后然后拿出来的时候需要执
行翻转操作，翻转操作可以参考博客https://www.cnblogs.com/kubixuesheng/p/4394509.html*/

