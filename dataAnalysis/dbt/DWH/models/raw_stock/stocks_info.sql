with source as (

    select * from {{ source('securities', 'stock_info') }}
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
