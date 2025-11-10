from feast import FileSource
from datetime import timedelta

bank_source = FileSource(
    path="data/bank_marketing.parquet",
    timestamp_field="event_timestamp"
)
