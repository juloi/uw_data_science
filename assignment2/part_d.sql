.open reuters.db
.output part_d.txt

select
count(*)
from (
	
select
	docid,
	term
from Frequency
where term = 'law' or term = 'legal'
group by 1) as c;