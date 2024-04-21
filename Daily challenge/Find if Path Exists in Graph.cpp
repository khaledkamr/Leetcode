class Solution 
{
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) 
    {
        if(n == 1) return true;
        vector<bool> vi(n, false);
        vi[source] = true;
        bool flag = true;
        while(flag)
        {
            flag = false;
            for(int i = 0; i < edges.size(); i++)
            {
                if(vi[edges[i][0]] != vi[edges[i][1]])
                {
                    vi[edges[i][0]] = true;
                    vi[edges[i][1]] = true;
                    flag = true;
                }
                if(vi[destination]) return true;
            }
        }
        return false;
    }
};