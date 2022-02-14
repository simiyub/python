select name "Title",  total_quantity "Copies" from
product prod,
(
select product_id, sum(quantity) as total_quantity from orders
where dispatch_date >= curdate() - interval 1 year
) orders
where prod.product_id = orders.product_id
and SYSDATE - available_from < (curdate() - interval 1 month)
and total_quantity < 10
