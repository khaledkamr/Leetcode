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
    bool isPalindrome(ListNode* head) 
    {
        vector<int>vec;
        vector<int>rev;

        while(head)
        {
            vec.push_back(head->val);
            head = head->next;
        }

        rev = vec;
        reverse(rev.begin(), rev.end());

        for(int i = 0; i < vec.size()-1; i++)
        {
            if(vec.at(i) != rev.at(i))
            {
                return false;
            }
        }
        return true;
    }
};