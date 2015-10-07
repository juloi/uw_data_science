.open reuters.db
.output part_a.txt
select
	count(*)
from Frequency
where docid = '10398_txt_earn';