with source as (

    select * from {{ source('securities', 'stock_daily_valuations') }}
)
select 
    *,
    current_timestamp as ingestion_timestamp
from source
