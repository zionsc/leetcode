#pragma GCC optimize("Ofast", "inline", "fast-math", "unroll-loops", "no-stack-protector")

class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        unordered_set<string>dead_set(deadends.begin(),deadends.end());
        if(dead_set.find("0000")!=dead_set.end()){
            return -1;
        }

        deque<pair<string,int>>q;
        unordered_set<string>visited;
        q.push_back({"0000",0});
        visited.insert("0000");

        while(!q.empty()){
            string code=q.front().first;
            int step=q.front().second;
            q.pop_front();
            if(code==target){
                return step;
            }
            vector<string>nextCodes = nextStep(code);
            for(auto& nextCode : nextCodes){
                if(visited.find(nextCode)==visited.end() && dead_set.find(nextCode)==dead_set.end()){
                    q.push_back({nextCode,step+1});
                    visited.insert(nextCode);
                }
            }
        }
        return -1;
    }
private:
    vector<string> nextStep(string& code) {
        vector<string> result;
        for(int i=0; i<4; ++i){
            int x=code[i]-'0';
            for(int j=-1; j<2; j+=2){
                int y=(x+j+10)%10;
                string newCode=code;
                newCode[i]=y+'0';
                result.push_back(newCode);
            }
        }
        return result;
    }
};