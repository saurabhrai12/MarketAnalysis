with source as (

    select * from "Northwind"."STAGE"."customer"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source