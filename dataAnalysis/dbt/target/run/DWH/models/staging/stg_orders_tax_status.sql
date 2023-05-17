
  create view "Northwind"."STAGE"."stg_orders_tax_status__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."orders_tax_status"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );