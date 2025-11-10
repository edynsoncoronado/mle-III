from feast import Entity, FeatureView, Field
from feast.types import Float32, Int64, String
from data_source import bank_source

# Entidad
customer = Entity(name="customer_id", join_keys=["customer_id"])

# Definición de features
bank_feature_view = FeatureView(
    name="bank_features",
    entities=[customer],
    ttl=None,
    schema=[
        Field(name="age", dtype=Int64),
        Field(name="balance", dtype=Float32),
        Field(name="duration", dtype=Float32),
        Field(name="campaign", dtype=Int64),
        Field(name="previous", dtype=Int64),
        Field(name="job", dtype=String),
        Field(name="marital", dtype=String),
        Field(name="education", dtype=String),
        Field(name="default", dtype=String),
        Field(name="housing", dtype=String),
        Field(name="loan", dtype=String),
        Field(name="contact", dtype=String),
        Field(name="month", dtype=String),
        Field(name="poutcome", dtype=String),
    ],
    source=bank_source,
)
