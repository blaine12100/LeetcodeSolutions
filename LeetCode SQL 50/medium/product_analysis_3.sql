/*
https://leetcode.com/problems/product-sales-analysis-iii/?envType=study-plan-v2&envId=top-sql-50

For the first part, create a CTE with dense_rank over product_id, order by year asc where dense_rank = 1 to get the earliest year

Then from this CTE, join to table on product_id, year and get quantity and price (Not sure about this one)
*/

with abc as (
    select product_id, year, row_number() over(partition by product_id order by year) as unique_rank from sales
)

select a.product_id, a.year as first_year, s.quantity, s.price from abc as a left join sales as s on a.product_id = s.product_id and a.year = s.year where a.unique_rank = 1