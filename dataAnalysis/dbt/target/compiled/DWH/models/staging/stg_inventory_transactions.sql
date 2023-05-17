with source as (

    select * from "Northwind"."STAGE"."inventory_transactions"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source