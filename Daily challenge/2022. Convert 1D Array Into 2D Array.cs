public class Solution 
{
    public int[][] Construct2DArray(int[] original, int m, int n) 
    {
        if(original.Length != m * n)
        {
            return [];
        }
        int[][] res = new int[m][];
        for(int i = 0; i < m; i++)
        {
            int start = i * n;
            int end = start + n;
            res[i] = original[start..end];
        }
        return res;
    }
}