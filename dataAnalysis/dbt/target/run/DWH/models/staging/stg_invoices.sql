
  create view "Northwind"."STAGE"."stg_invoices__dbt_tmp"
    
    
  as (
    with source as (

    select * from "Northwind"."STAGE"."invoices"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
  );