from datetime import timedelta

from feast import BigQuerySource, Entity, Feature, FeatureView, Field
from feast.types import Float32, Int64, String

driver_locations_source = BigQuerySource(
    table="qe-project-340220.testDataset.yellow_cab",
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
)

driver = Entity(
    name="driver",
    description="driver id",
)

driver_locations = FeatureView(
    name="driver_locations",
    entities=[driver],
    ttl=timedelta(days=1),
    schema=[
        Field(name="lat", dtype=Float32),
        Field(name="lon", dtype=String),
        Field(name="driver", dtype=Int64),
    ],
    source=driver_locations_source,
)
