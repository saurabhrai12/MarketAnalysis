
  create view "Northwind"."STAGE"."stg_suppliers__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."suppliers"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );