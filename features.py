from datetime import timedelta

from feast import BigQuerySource, Entity, Feature, FeatureView, Field
from feast.types import Float32, Int64, String

trips_source = BigQuerySource(
    table="testDataset.yellow_cab",
    timestamp_field="dropoff_datetime",
    created_timestamp_column="pickup_datetime",
)

trip = Entity(
    name="yellow_cab",
    join_keys=["PU_LOCATION_ID"],
    description="yellow cab trip",
)

trip_costs = FeatureView(
    name="trip_costs",
    entities=[trip],
    ttl=timedelta(days=1),
    schema=[
        Field(name="fare_amount", dtype=Float32, tags={"production": "true"}),
        Field(name="extra", dtype=Float32, tags={"production": "false"}),
        Field(name="tip_amount", dtype=Float32, tags={"production": "true"}),
        Field(name="tolls_amount", dtype=Float32, tags={"production": "true"}),
    ],
    source=trips_source,
    description="trip costs feature view",
    tags={"production": "true"}
)
