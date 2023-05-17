
  create view "Northwind"."STAGE"."stg_customer__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."customer"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );