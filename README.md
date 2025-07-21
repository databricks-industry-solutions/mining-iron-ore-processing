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
   - Open the file databricks.yml from the root of the git repo
   - Select the DABs icon in the side menu tray
   - **PR cleanup**: Resources automatically cleaned up when PR is closed

## What Gets Deployed

- **Workflow**: `Databricks Demo Deployment Example - Two Simple Notebooks` 
- **Notebooks**: `notebook1.ipynb` → `notebook2.ipynb` (sequential execution)
- **Dashboard**: `Demo Dashboard` (deployed alongside notebooks)
- **App**: `demo-app` (Simple Streamlit app)
- **Location**: `/Workspace/Users/your-email@company.com/dbx-dabs-demo-dev/`

## Manual Commands (if you prefer)

```bash
databricks bundle validate    # Check configuration
databricks bundle deploy      # Deploy to workspace
databricks bundle run demo_workflow # Run the demo workflow
databricks bundle summary     # See what's deployed
databricks bundle destroy     # Remove everything
```

## Customizing for Your Project

1. Update `databricks.yml` with your job/notebook names
2. Replace `notebooks/notebook1.ipynb` and `notebooks/notebook2.ipynb` with your notebooks
3. Modify the workspace `host` and `root_path` as needed

## Project Structure

```
├── databricks.yml           # Main DABs configuration
├── notebooks/
│   ├── notebook1.ipynb      # First notebook
│   └── notebook2.ipynb      # Second notebook (runs after first)
├── dashboards/
│   └── dashboard_example.lvdash.json  # Demo dashboard
├── apps/
│   └── demo_app/
│       ├── app.py                     # Streamlit app
│       └── app.yaml                   # App configuration
└── scripts/
    ├── deploy.sh           # Automated deployment
    └── cleanup.sh          # Automated cleanup
```

That's it! 🚀 
