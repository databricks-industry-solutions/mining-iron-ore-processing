# Databricks notebook source
# MAGIC %pip install mlflow
# MAGIC dbutils.library.restartPython() 

# COMMAND ----------

# MAGIC %run ../../00.set_variables

# COMMAND ----------

from pathlib import Path

# TODO: Update these values as necessary


# TODO: Create notebooks for each task and populate the notebook path here, replacing the INVALID PATHS LISTED BELOW.
# These paths should correspond to where you put the notebooks templated from the example deployment jobs template notebook
# in your Databricks workspace.

current_notebook_path = dbutils.entry_point.getDbutils().notebook().getContext().notebookPath().get()
# Use pathlib to handle path manipulation robustly
current_notebook_dir = Path(current_notebook_path).parent

evaluation_notebook_path = f"{current_notebook_dir}/evaluation"
approval_notebook_path = f"{current_notebook_dir}/approval"
deployment_notebook_path = f"{current_notebook_dir}/deployment"

# COMMAND ----------

# Create job with necessary configuration to connect to model as deployment job
from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs
import mlflow
from mlflow.tracking.client import MlflowClient

client = MlflowClient(registry_uri="databricks-uc")
w = WorkspaceClient()

def create_deployment_job(model_element:str):
    model_name = f"{catalog_name}.{schema_name}.{model_element}_model" # The name of the already created UC Model
    job_name = f"demo_mining_processing_{model_element}_model_deploy" # The desired name of the deployment job
    job_settings = jobs.JobSettings(
        name=job_name,
        tasks=[
            #TODO: fix up evaluation
            # jobs.Task(
            #     task_key="Evaluation",
            #     notebook_task=jobs.NotebookTask(notebook_path=evaluation_notebook_path),
            #     max_retries=0,
            # ),
            jobs.Task(
                task_key="Approval_Check",
                notebook_task=jobs.NotebookTask(
                    notebook_path=approval_notebook_path,
                    base_parameters={"approval_tag_name": "{{task.name}}"}
                ),
                #depends_on=[jobs.TaskDependency(task_key="Evaluation")],
                max_retries=0,
            ),
            jobs.Task(
                task_key="Deployment",
                notebook_task=jobs.NotebookTask(notebook_path=deployment_notebook_path),
                depends_on=[jobs.TaskDependency(task_key="Approval_Check")],
                max_retries=0,
            ),
        ],
        parameters=[
            jobs.JobParameter(name="model_name", default=model_name),
            jobs.JobParameter(name="model_version", default=""),
        ],
        queue=jobs.QueueSettings(enabled=True),
        max_concurrent_runs=1,
    )

    created_job = w.jobs.create(**job_settings.__dict__)

    print(f"job created with id: {created_job.job_id}")
    print(f"applying to model {model_name}")
    try:
        if client.get_registered_model(model_name):
            client.update_registered_model(model_name, deployment_job_id=created_job.job_id)
            print("Model updated")
    except mlflow.exceptions.RestException:
        print("Model does not exist")
        client.create_registered_model(model_name, deployment_job_id=created_job.job_id)

    print(f"Deployment Job {job_name} Created for Model: {model_name}")

#create the two model deployment jobs
for model_name in ["fe", "si"]:    create_deployment_job(model_name)


