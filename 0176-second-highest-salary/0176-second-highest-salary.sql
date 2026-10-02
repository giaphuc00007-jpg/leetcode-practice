# Write your MySQL query statement below
with dk as (
select salary, 
dense_rank() over(
    order by salary desc
) as rank_
from Employee
)
select  max(salary)as SecondHighestSalary
from dk 
where rank_ = 2
