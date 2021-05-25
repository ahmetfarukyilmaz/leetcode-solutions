--https://leetcode.com/problems/customers-who-never-order/

select Customers.Name as Customers
from Customers
where Customers.Id not in
(
    select CustomerId from Orders
)