with source as (

    select * from "Northwind"."STAGE"."employee_privileges"
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source