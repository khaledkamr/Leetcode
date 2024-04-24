SELECT ROUND(SUM(order_date = customer_pref_delivery_date) * 100 / COUNT(*), 2) AS immediate_percentage
FROM Delivery 
where (customer_id, order_date) in (
  Select customer_id, min(order_date) 
  from Delivery
  group by customer_id
);