with source as (

    select * from "Northwind"."STAGE"."employees"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source