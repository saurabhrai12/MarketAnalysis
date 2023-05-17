
  create view "Northwind"."STAGE"."stg_shippers__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."shippers"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );