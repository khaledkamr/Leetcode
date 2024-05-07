class Solution {
public:
    ListNode* reverse(ListNode* node)
    {
        auto curr = node;
        ListNode* prev = NULL;
        while(curr)
        {
            auto temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
    }

    ListNode* doubleIt(ListNode* head) 
    {
        head = reverse(head);
        auto curr = head;
        ListNode* prev = NULL;
        int carry = 0;
        while(curr)
        {
            int value = curr->val * 2 + carry;
            curr->val = value % 10;
            if(value > 9)
            {
                carry = 1;
            }
            else
            {
                carry = 0;
            }
            prev = curr;
            curr = curr->next;
        }
        
        if(carry)
        {
            prev->next = new ListNode(carry);
        }

        return reverse(head);
    }
};