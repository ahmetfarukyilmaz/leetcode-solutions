--https://leetcode.com/problems/swap-salary/

update Salary
set sex = case sex 
            when 'm' then 'f'
            when 'f' then 'm'
end

--ALTERNATIVE SOLUTION

update Salary
set sex = if(sex='m','f','m')