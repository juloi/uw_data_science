.open reuters.db
.output part_e.txt

select
	count(*)
from (
	select
		docid,
		count(term) as term_count
	from Frequency
	group by 1) as c
where term_count > 300;