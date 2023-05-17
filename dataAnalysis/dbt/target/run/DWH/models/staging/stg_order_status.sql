
  create view "Northwind"."STAGE"."stg_order_status__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."orders_status"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );