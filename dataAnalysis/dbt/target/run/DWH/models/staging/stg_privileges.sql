
  create view "Northwind"."STAGE"."stg_privileges__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."privileges"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );