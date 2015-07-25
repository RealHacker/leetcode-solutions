delete from Person where id not in
(select minid from
    (select min(Id) as minid, count(*) as cnt from Person group by Email) 
as temp)