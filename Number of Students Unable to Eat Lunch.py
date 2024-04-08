class Solution(object):
    def countStudents(self, students, sandwiches):
        stud = deque(students)
        sand = deque(reversed(sandwiches))
        count = 0
        while stud:
            if count == len(stud):
                return len(stud)
            if stud[0] == sand[-1]:
                stud.popleft()
                sand.pop()
                count = 0
            else:
                stud.append(stud.popleft())
                count += 1
                
        return 0