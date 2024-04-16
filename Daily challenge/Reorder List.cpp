/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution 
{
public:
    void reorderList(ListNode* head) 
    {
        stack<ListNode*>stack;
        ListNode* curr = head;
        while(curr)
        {
            stack.push(curr);
            curr = curr->next;
        }
        curr = head;
        ListNode* last;
        ListNode* next;
        unordered_map<ListNode*, bool>visited;

        while(true)
        {
            last = stack.top();
            next = curr->next;
            visited[curr] = true;
            if(visited[last]){curr->next = NULL; break;};
            curr->next = last;
            curr = curr->next;
            visited[curr] = true;
            if(visited[next]){curr->next = NULL; break;};
            curr->next = next;
            curr = curr->next;
            stack.pop();
        }
    }
};