
  create view "Northwind"."STAGE"."stg_purchase_orders__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."purchase_orders"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );