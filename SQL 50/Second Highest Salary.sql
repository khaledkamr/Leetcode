SELECT salary AS SecondHighestSalary
FROM Employee
WHERE salary NOT IN (
    SELECT MAX(salary) FROM Employee
)
ORDER BY salary DESC
LIMIT 1;