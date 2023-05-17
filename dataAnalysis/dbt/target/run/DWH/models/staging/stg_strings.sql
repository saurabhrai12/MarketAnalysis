
  create view "Northwind"."STAGE"."stg_strings__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."strings"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );