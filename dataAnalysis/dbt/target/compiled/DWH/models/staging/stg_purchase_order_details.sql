with source as (

    select * from "Northwind"."STAGE"."purchase_order_details"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source