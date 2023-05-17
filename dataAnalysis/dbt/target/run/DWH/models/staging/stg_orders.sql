
  create view "Northwind"."STAGE"."stg_orders__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."orders"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );