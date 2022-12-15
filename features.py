from datetime import timedelta

from feast import BigQuerySource, Entity, Feature, FeatureView, Field
from feast.types import Float32, Int64, String

driver_locations_source = BigQuerySource(
    table="qe-project-340220.testDataset.yellow_cab",
    timestamp_field="dropoff_datetime",
    created_timestamp_column="pickup_datetime",
)

trip = Entity(
    name="yellow_cab",
    description="trip",
)

trip_costs = FeatureView(
    name="trip_costs",
    entities=[trip],
    ttl=timedelta(days=1),
    schema=[
        Field(name="fare_amount", dtype=Float32),
        Field(name="extra", dtype=Float32),
        Field(name="tip_amount", dtype=Float32),
        Field(name="tolls_amount", dtype=Float32),
    ],
    source=driver_locations_source,
)
