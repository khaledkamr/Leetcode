int x[4] = {0,0,1,-1};
int y[4] = {1,-1,0,0};

class Solution 
{
public:
    bool outside(vector<vector<char>>& board, int i, int j)
    {
        if(i < 0 || i >= board.size() || j < 0 || j >= board[0].size())
        {
            return true;
        }
        return false;
    }

    bool dfs(vector<vector<char>>& board, int i, int j, string word, int pos)
    {
        if(pos == word.size())
        {
            return true;
        }
        if(outside(board, i, j) || board[i][j] != word[pos])
        {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '-';
        
        for(int k = 0; k < 4; k++)
        {
            int r = x[k] + i;
            int c = y[k] + j;
            if(dfs(board, r ,c, word, pos + 1))
            {
                return true;
            }
        }
        board[i][j] = temp;
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) 
    {
        int n = board.size();
        int m = board[0].size();

        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                if(board[i][j] == word[0] && dfs(board, i, j, word, 0))
                {
                    return true;
                }
            }
        }
        return false;
    }
};