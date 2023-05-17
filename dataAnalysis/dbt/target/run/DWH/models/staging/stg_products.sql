
  create view "Northwind"."STAGE"."stg_products__dbt_tmp"
    
    
  as (
    with source as (
    select cast(supplier_ids as integer) as supplier_id,
           id,
           product_code,
           product_name,
           description,
           standard_cost,
           list_price,
           reorder_level,
           target_level,
           quantity_per_unit,
           discontinued,
           minimum_reorder_quantity,
           category,
           attachments
    from "Northwind"."STAGE"."products"
    where supplier_ids not like '%;%'
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );