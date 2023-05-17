
  create view "Northwind"."STAGE"."stg_inventory_transactions__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."inventory_transactions"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );