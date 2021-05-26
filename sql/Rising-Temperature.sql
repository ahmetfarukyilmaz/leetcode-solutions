
--https://leetcode.com/problems/rising-temperature/

select w2.id
from Weather w1 join Weather w2 on
datediff(w2.recordDate,w1.recordDate)=1
and w2.Temperature>w1.Temperature