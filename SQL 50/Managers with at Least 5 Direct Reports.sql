SELECT name FROM Employee
WHERE id IN
(SELECT managerId From Employee
GROUP BY managerId
HAVING COUNT(id) >= 5)
