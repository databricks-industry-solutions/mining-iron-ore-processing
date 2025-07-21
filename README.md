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

That's it! 🚀 
