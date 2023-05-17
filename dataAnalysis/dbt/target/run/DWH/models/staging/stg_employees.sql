
  create view "Northwind"."STAGE"."stg_employees__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."employees"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );