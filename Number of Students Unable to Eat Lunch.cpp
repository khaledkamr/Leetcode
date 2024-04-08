class Solution 
{
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) 
    {
        queue<int>stud;
        stack<int>sand;
        reverse(sandwiches.begin(), sandwiches.end());
        for(int i = 0; i < students.size(); i++)
        {
            stud.push(students[i]);
            sand.push(sandwiches[i]);
        }
        int count = 0;
        while(!stud.empty())
        {
            if(count == stud.size()) return stud.size();
            if(stud.front() == sand.top())
            {
                stud.pop();
                sand.pop();
                count = 0;
            }
            else
            {
                stud.push(stud.front());
                stud.pop();
                count++;
            }
        }
        return 0;
    }
};