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
class Solution {
public:
    ListNode* frequenciesOfElements(ListNode* head) {
        map<int,int> freq;
        ListNode* curr = head;
        while (curr) {
            freq[curr->val]++;
            curr = curr->next;
        }
        ListNode* dummy = new ListNode();
        curr = dummy;
        for (auto itr : freq) {
            ListNode* newNode = new ListNode(itr.second, nullptr);
            curr->next = newNode;
            curr = curr->next;
        }
        return dummy->next;
    }
};