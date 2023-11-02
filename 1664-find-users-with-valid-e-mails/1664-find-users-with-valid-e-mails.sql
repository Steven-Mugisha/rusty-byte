# Write your MySQL query statement below
SELECT * FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zAZ0-9_.-]*@leetcode[.]com'
