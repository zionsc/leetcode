/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) {
            return NULL;
        }
        Node* dummy = new Node(0,NULL,head,NULL);
        stack<Node*> nodeStack;
        nodeStack.push(head);
        Node* prev = dummy;

        while (!nodeStack.empty()) {
            Node* node = nodeStack.top();
            nodeStack.pop();
            node->prev = prev;
            prev->next = node;

            if (node->next) {
                nodeStack.push(node->next);
                node->next = NULL;
            } if (node->child) {
                nodeStack.push(node->child);
                node->child = NULL;
            }

            prev = node;
        }
        dummy->next->prev = NULL;
        return dummy->next;
        }
    };