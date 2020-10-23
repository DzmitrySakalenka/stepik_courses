select good.name, category.name from category_has_good
	inner join good on category_has_good.good_id = good.id
	inner join category on category_has_good.category_id = category.id
order by good.name, category.name;

select client.first_name, client.last_name, COUNT(*) as new_sale_num from client
	inner join sale on client.id = sale.client_id
	inner join status on sale.status_id = status.id where status.name = 'new'
group by client.first_name, client.last_name;

select good.name, category.name from category_has_good
	left outer join category on category_has_good.category_id = category.id
	right outer join good on category_has_good.good_id = good.id;

select good.name, category.name from category_has_good
	left outer join category on category_has_good.category_id = category.id
	right outer join good on category_has_good.good_id = good.id
union
select good.name, category.name from category_has_good
	right outer join category on category_has_good.category_id = category.id
	left outer join good on category_has_good.good_id = good.id;

select source.name, sum(sale.sale_sum) from source
	left outer join client on source.id = client.source_id
	left outer join sale on client.id = sale.client_id
group by source.name;

select good.name from good
	left join category_has_good on good.id = category_has_good.good_id
	left join category on category_has_good.category_id = category.id WHERE category.name = 'Cakes'
union
select good.name from good
	left join sale_has_good on sale_has_good.good_id = good.id
	left join sale on sale_has_good.sale_id = sale.id
	left join status ON status.id = sale.status_id where status.name = 'delivering';

select category.name, count(sale.id) from category
	left outer join category_has_good on category.id = category_has_good.category_id
	left outer join good on good.id = category_has_good.good_id
	left outer join sale_has_good on good.id = sale_has_good.good_id
	left outer join sale on sale.id = sale_has_good.sale_id
	group by category.name;

select source.name from source 
    where not exists (
        select * from client 
            where client.source_id = source.id)
union
select source.name from source
	inner join client on client.source_id = source.id
	inner join sale on sale.client_id = client.id
	inner join status on status.id = sale.status_id 
    where status.name = 'rejected';