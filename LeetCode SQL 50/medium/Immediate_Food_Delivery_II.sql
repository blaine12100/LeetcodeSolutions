"""
https://leetcode.com/problems/immediate-food-delivery-ii/
If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

"""

# Write your MySQL query statement below
-- With window function, we can rank the orders based on order date and
-- identify the first order for each customer. Then after identifying that,
-- create a column for scheduled orders by comparing the dates of the orders.
-- After that, we can take a sum of all orders which are immediate to first orders (After labelling both of them in the previous steps)

With abc as (
    select customer_id, order_date, customer_pref_delivery_date as pref_delivery, ROW_NUMBER() OVER(partition by customer_id order by order_date) as rn from Delivery
),

def as (select *, case when order_date = pref_delivery then 'immediate' else 'scheduled' end as order_status, case when rn = 1 then 'first' else '' end as first_order from abc)

select round((sum(case when first_order='first' and order_status='immediate' then 1 else 0 END) / (sum(case when first_order='first' then 1 else 0 END)) * 100), 2) as immediate_percentage from def