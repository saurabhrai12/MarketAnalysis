with source as (

    select * from "Northwind"."STAGE"."order_details"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source