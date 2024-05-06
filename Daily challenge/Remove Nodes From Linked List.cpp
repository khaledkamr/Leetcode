class Solution {
public:
    ListNode* reverse(ListNode* head)
    {
        ListNode* prev = NULL;
        auto curr = head;
        while(curr)
        {
            auto temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }

    ListNode* removeNodes(ListNode* head) 
    {
        head = reverse(head);
        ListNode* curr = head;
        ListNode* temp = curr->next;
        while(curr->next)
        {
            if(temp->val < curr->val)
            {
                curr->next = temp->next;
                temp = temp->next;
            }
            else
            {
                curr = curr->next;
                temp = curr->next;
            }
        }
        return reverse(head);
    }
};