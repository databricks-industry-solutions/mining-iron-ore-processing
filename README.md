# Fe Concentrator Demo

This demo will deploy and end to end AI and Optimisation solution for an Iron Ore Concentrator. This demo will be deployed using Databricks Asset Bundles (DAB's). 

## Quick Start

## Workspace Setup

Firstly you will need to pull this Repo down into your Databricks Workspace as a Git Folder. 

1. **Clone Repo to Workspace**:
   - Workspace → Create → Git Folder
   - Paste in the Repo https location
   - click "Create"

2. **Deploy via DABS in the UI**:
   - **Edit DABs Config**- Open the file `databricks.yml` from the root of the git repo
   - In the `databricks.yml` file, you will need to enter your `Catalog` name and desired `Warehouse` name as shown:

   ![](notebooks/demo_setup/images/dabs_edit.png)
   - **DABs UI**- Select the DABs icon in the side menu tray, its a small Rocket Ship icon as shown:

   ![](notebooks/demo_setup/images/dabs_image.png)
   - **Deploy**- Click the "deploy" button on the DABs UI as shown:

   ![](notebooks/demo_setup/images/dabs_deploy.png)
   - **Run Workflow**- Once your artifacts are deployed, run the workflow here to set up and run models and Optimizations:

   ![](notebooks/demo_setup/images/dabs_run_job.png)

## What Gets Deployed

- **Workflow**: `deploy-iops-demo-workflow` This is a workflow to deploy the models, run ingestion pipelines and deploy our Databricks App 
- **Notebooks**: `notebooks/mining-iron-ore-processing/` → this director contains the main Demo notebooks and links to Demo content/objects
- **Dashboard**: `demo_dashboard` A simple dashboard of predictions vs actuals
- **App**: `demo-app` A streamlit app to simulate Fe and Si output based on Plant set levels + infeed
- **Pipeline**: `Mining Iron Ore Processing DLT Pipeline` a pipeline to ingest and transform our features
- **Models**: `fe_model` and `si_model` two models that will be labelled champion, trained to predict concentrator output based on infeed and plant settings 
- **Model Serving Endpoints**: Serving endpoints for the two models above, to be used by our Databricks App 
- **Model Deployment Jobs**: CICD model deployment attached to our two models with an approval deployment step ahead of serving the models 

## Project Structure

```
├── databricks.yml           # Main DABs configuration
├── notebooks/
│   ├── mining_iron_ore_processing      # Main Demo Entry Point (## go here to start ##)
│   └── demo_setup                      # helper functions and resources to deploy the demo
│   └── outputs                         # directory for model artifacts and outputs
├── dashboards/
│   └── Fe Concentrator Prediction Dashboard.lvdash.json  # Demo dashboard
├── apps/
│   └── src/
│       ├── app.py                     # Streamlit app
│       └── app.yaml                   # App configuration
└── scripts/
    ├── deploy.sh           # Automated deployment
    └── cleanup.sh          # Automated cleanup
```

`NOTE` the workflow to deploy will take ~20-25 minutes to finish, this is due to model training and optimization runs primarily. Please be patient and confirm the workflow has finished before your dive in!

The Demo is contained primarily in a series of Notebooks under the directory `notebooks/mining_iron_ore_processing_demo`, start at Notebook `00. Introduction and Configuration` and continue down from there. 

Make sure to always Run All in each notebook, as this will load demo cells and demonstrate normal workflows. 

That's it! 🚀🚀🚀🚀🚀 Enjoy the Demo! 🚀🚀🚀🚀🚀
