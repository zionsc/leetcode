#pragma GCC optimize('0fast', 'unroll-loops')

class Solution {
public:
    bool dfs(int r, int c, int i, string& word, vector<vector<char>>& board, set<pair<int,int>>& path){
        if(i==word.size()){
            return true;
        }

        if(r<0 || r>=board.size() || c<0 || c>=board[0].size() || board[r][c]!=word[i] || path.find({r,c})!=path.end()){
            return false;
        }

        path.insert({r,c});

        bool res=(
            dfs(r+1,c,i+1,word,board,path) || 
            dfs(r-1,c,i+1,word,board,path) || 
            dfs(r,c+1,i+1,word,board,path) || 
            dfs(r,c-1,i+1,word,board,path)
        );

        path.erase({r,c});

        return res;
    }

    bool exist(vector<vector<char>>& board, string word) {
        ios_base::sync_with_stdio(0);
        cout.tie(0);
        cin.tie(0);

        set<pair<int,int>> path;

        for(int r=0; r<board.size(); ++r){
            for(int c=0; c<board[0].size(); ++c){
                if(dfs(r,c,0,word,board,path)){
                    return true;
                }
            }
        }
        return false;
    }
};