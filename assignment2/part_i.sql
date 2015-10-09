.open reuters.db
.output part_i.txt

with freq as (
	select * from frequency
	union
	select 'q' as docid, 'washington' as term, 1 as count
	union
	select 'q' as docid, 'taxes' as term, 1 as count
	union
	select 'q' as docid, 'treasury' as term, 1 as count
	)

select c.count from (
	select
		b.docid,
		sum(b.count) as count
	from freq as a
	left join freq as b
	on a.term = b.term
	where a.docid = 'q'
	group by 1
	order by 2 desc
	limit 1) as c;


-----