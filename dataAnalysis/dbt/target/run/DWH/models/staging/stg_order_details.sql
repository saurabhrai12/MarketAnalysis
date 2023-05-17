
  create view "Northwind"."STAGE"."stg_order_details__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."order_details"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );