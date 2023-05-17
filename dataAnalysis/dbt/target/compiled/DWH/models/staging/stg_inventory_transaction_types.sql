with source as (

    select * from "Northwind"."STAGE"."inventory_transaction_types"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source