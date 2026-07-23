SELECT
    CASE
      WHEN SUM(unit_price * quantity) > 50000
      THEN SUM(unit_price * quantity) * 0.9
      ELSE SUM(unit_price * quantity) 
      END AS final_price 
      FROM order_items;