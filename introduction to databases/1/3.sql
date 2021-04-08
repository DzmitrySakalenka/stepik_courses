select count(project_name) from project;

select category, count(product_name)
from store
group by category;

select category, sum(sold_num*price) as prf
from store
group by category
order by prf desc 
limit 5;

select count(project_name),
       sum(budget),
       avg(datediff(project_finish, project_start))
from project;