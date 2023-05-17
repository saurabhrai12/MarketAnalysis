with source as (

    select * from "Northwind"."STAGE"."strings"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source