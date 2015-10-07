.open reuters.db
.output part_f.txt

select
	count(*)
from(
	select
		docid
	from Frequency
	where term = 'transactions') as l
inner join (
	select
		docid
	from Frequency
	where term = 'world') as r
on l.docid = r.docid;