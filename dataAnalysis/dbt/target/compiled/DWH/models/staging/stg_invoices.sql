with source as (

    select * from "Northwind"."STAGE"."invoices"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source