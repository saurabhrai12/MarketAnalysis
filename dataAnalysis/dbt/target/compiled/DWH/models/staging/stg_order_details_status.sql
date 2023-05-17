with source as (

    select * from "Northwind"."STAGE"."order_details_status"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source