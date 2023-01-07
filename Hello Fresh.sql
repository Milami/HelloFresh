--1
select product_sku
from subscription s
inner join customer c on c.id_customer = s.fk_customer
inner join product p on p.id_product= s.fk_product_subscribed_to
where email like 'fancygirl83@hotmail.com'
			and s.status = 'active'

--2
select c.id_customer, c.first_name,c.last_name
from subscription s 
inner join customer c on c.id_customer=s.fk_customer
inner join product p on p.id_product= s.fk_product_subscribed_to
inner join product_family pf on pf.id_product_family = p.fk_product_family
where s.status = 'active'
and pf.product_family_handle = 'classic-box'

--3
select s.id_subscription, SUM(o.id_order)
from subscription s 
inner join orders o on o.fk_subscription = s.id_subscription
where s.status = 'paused'
group by s.id_subscription
having SUM(o.id_order) = 1

--4
select fk_customer, AVG(id_subscription)
from subscription
group by fk_customer

--5
;with cte5 as (
select c.id_customer, count(distinct o.fk_product) as distinct_count_of_products
from customer c
left join subscription s on s.fk_customer=c.id_customer
left join orders o on o.fk_subscription=s.id_subscription
group by c.id_customer
having count(distinct o.fk_product) > 1
)
select COUNT(id_customer)
from cte5
--6
wit cte6 as(
select  fk_customer,id_subscription,count(fk_product) number_of_producst
from subscription s
left join orders o on o.fk_subscription = s.id_subscription
group by fk_customer,id_subscription
having count(fk_product) > 1
)
, cte6_1 as (select fk_customer,count(id_subscription)
from cte6
group by fk_customer
)
select count(fk_customer) from cte6_1

--7
select id_customer, first_name, last_name,
	(select c.id_customer, count(o.id_order)
	from customer c
	inner  join subscription s on s.fk_customer=c.id_customer
	inner join orders o on o.fk_subscription = s.id_subscription 
	where DATEDIFF(WEEK,o.delivery_date,GETDATE()) < 2
	group by c.id_customer)
from customer c
inner  join subscription s on s.fk_customer=c.id_customer
inner join orders o on o.fk_subscription = s.id_subscription  
where DATEDIFF(WEEK,delivery_date,GETDATE()) = 2

