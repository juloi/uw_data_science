.open reuters.db
.output part_h.txt

select
	sum(a.count * b.count) as value
from frequency as a
left join frequency as b
on a.term = b.term
where a.docid = '10080_txt_crude' and b.docid = '17035_txt_earn';