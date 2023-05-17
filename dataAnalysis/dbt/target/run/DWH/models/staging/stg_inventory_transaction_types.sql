
  create view "Northwind"."STAGE"."stg_inventory_transaction_types__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."inventory_transaction_types"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );