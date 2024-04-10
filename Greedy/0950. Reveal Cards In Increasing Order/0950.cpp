#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        sort(deck.begin(),deck.end(),greater<int>());
        deque<int>dq;

        for(int i=0; i<deck.size(); ++i){
            if(!dq.empty()){
                dq.push_front(dq.back());
                dq.pop_back();
            }
            dq.push_front(deck[i]);
        }
        
        vector<int>res(dq.begin(),dq.end());
        return res;
    }
};