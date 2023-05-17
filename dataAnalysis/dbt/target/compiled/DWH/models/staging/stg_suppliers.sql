with source as (

    select * from "Northwind"."STAGE"."suppliers"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source