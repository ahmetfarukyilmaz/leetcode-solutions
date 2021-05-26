
--https://leetcode.com/problems/employees-earning-more-than-their-managers/

select e1.Name as Employee
from Employee e1 join Employee e2 
on e1.managerId=e2.Id 
and e1.Salary>e2.Salary