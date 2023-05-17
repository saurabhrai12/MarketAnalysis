with source as (

    select * from "Northwind"."STAGE"."orders"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source