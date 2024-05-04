SELECT "High Salary" AS category, SUM(income > 50000) AS accounts_count
FROM Accounts
UNION 
SELECT "Low Salary", SUM(income < 20000) 
FROM Accounts
UNION
SELECT "Average Salary", SUM(income <= 50000 and income >= 20000)
FROM Accounts