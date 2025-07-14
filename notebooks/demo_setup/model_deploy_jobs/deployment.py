# Databricks notebook source
# MAGIC %md
# MAGIC This notebook should only be run in a Databricks Job, as part of MLflow 3.0 Deployment Jobs.

# COMMAND ----------

dbutils.widgets.text("model_name", "")
dbutils.widgets.text("model_version", "")

# COMMAND ----------

model_name = dbutils.widgets.get("model_name")
model_version = dbutils.widgets.get("model_version")

#remove the catalog_name
model_name_parts = model_name.split(".")
short_model_name = ".".join(model_name_parts[1:])

# TODO: Enter serving endpoint name
serving_endpoint_name = short_model_name.replace('.', '-') + "-serving-endpoint"

# COMMAND ----------

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import (
  ServedEntityInput,
  EndpointCoreConfigInput
)
from databricks.sdk.errors import ResourceDoesNotExist
w = WorkspaceClient()  # Assumes DATABRICKS_HOST and DATABRICKS_TOKEN are set
served_entities=[
  ServedEntityInput(
    entity_name=model_name,
    entity_version=model_version,
    workload_size="Small",
    scale_to_zero_enabled=True
  )
]

# Update serving endpoint if it already exists, otherwise create the serving endpoint
try:
  w.serving_endpoints.update_config(name=serving_endpoint_name, served_entities=served_entities)
except ResourceDoesNotExist:
  w.serving_endpoints.create(name=serving_endpoint_name, config=EndpointCoreConfigInput(served_entities=served_entities))

# COMMAND ----------

from databricks.sdk.service.iam import PermissionLevel, AccessControlRequest

endpoint_id = w.serving_endpoints.get(name=serving_endpoint_name).id

# Define the permission rule and apply it to the endpoint.
# This grants all users in the workspace the ability to query the endpoint.
w.serving_endpoints.update_permissions(
    serving_endpoint_id=endpoint_id,
    access_control_list=[
        AccessControlRequest(
            group_name="users",
            permission_level=PermissionLevel.CAN_QUERY
        )
    ]
)
