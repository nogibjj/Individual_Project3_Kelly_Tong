# IDS 706 Individual Project 3

This repository is for IDS706 Individual Project 3. 

## Purpose 
This repository includes the python code for creating a Data Processing Pipeline that can operate in Databricks. 
This pipeline includes functions in extracting, transforming and loading, as well as a query fuction that generate a visualization.
This entire repository can be clone in Databricks to perform job run and editing in workspace. 
Both python libraries and Databricks are used to facilitate efficient data processing and analysis job. 
More building process and query results are included in sectons below. 
    
## Important Things included are:
- ``.devcontainer`` includes a Dockerfile and devcontainer.json.
                The 'Dockerfile' within this folder specifies how the container should be built

- ``workflows`` includes CI.yml, which contain configuration files for setting up automated build, test, and deployment pipelines

- ``.gitignore`` is used to specify which files or directories should be excluded from version control when using Git.

- ``Makefile`` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

- ``README.md`` is the instruction file for the readers.

- ``main.py`` is a Python file. This specific main.py gets the python versions and operation system names. 

- ``requirements.txt`` is to specify the dependencies (libraries and packages) required to run the project.

- ``test_main.py`` is a test file for main.py

- ``setup.py`` setup the local packages for python, specify the dependencies required in the package. This executes the ETL streamline commands which can be called by a Makefile commnd. 

- ``mylib`` includes ``extract.py`` ``transform_load.py`` and ``query_viz.py`` which are used to extract
  a csv from an url, clean it and return a db file.

- ``run_job.py`` is included in a makefile command ``Makefile`` and in ``CI.yml`` to perform automatic run of the databrick job when Github Action is triggered through push. 

## Github actions
Status badges for CI.yml
`CI.yml`
[![CI](https://github.com/nogibjj/Individual_Project3_Kelly_Tong/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Individual_Project3_Kelly_Tong/actions/workflows/CI.yml)

## Key Functions

**Data Extraction:**
- Initiates a process to download the `women_stem.csv` dataset, which contains data on women's participation in STEM (Science, Technology, Engineering, and Mathematics) fields, through HTTP requests.
- Once downloaded, the dataset is stored in the Databricks FileStore, setting the stage for its subsequent processing and analysis.

**Databricks Environment Variables:**
- Configures the Databricks environment by setting critical environment variables, such as `SERVER_HOSTNAME` and `ACCESS_TOKEN`. These variables are essential for authenticating and establishing secure connections to the Databricks services.
- Ensures the environment is tailored to handle the specific requirements of processing and analyzing the women in STEM dataset.

**Data Transform and Load:**
- Processes the raw `women_stem.csv` data by converting it into a Spark dataframe. This step is crucial for leveraging Spark's powerful data processing capabilities.
- Transforms the Spark dataframe into a Delta Lake Table. This transformation allows for better management and versioning of the dataset, facilitating more efficient and reliable data operations within the Databricks environment.

**Data Query, Analysis and Visualization:**
- Conducts comprehensive data analysis on the transformed dataset using Spark SQL. This analysis aims to uncover insights about women's participation and trends in STEM fields.
- Employs various data visualization techniques to represent the analytical findings graphically. These visualizations aid in interpreting the data more intuitively and effectively, highlighting key patterns and trends.

**Data Validation: File Path Testing:**
- Incorporates a function in `test_main.py` to verify the existence of specific file paths within the Databricks FileStore. This step is vital to ensure that the necessary data files are available and accessible for processing.
- Includes testing protocols to validate the connection to the Databricks API, thereby ensuring the reliability and functionality of the entire data pipeline.

**Automation (Automated Trigger):**
- Implements an automated trigger mechanism using the Databricks API. This mechanism is designed to initiate a pipeline run automatically in response to a new push event in the associated GitHub repository.
- This automation enhances the pipeline's efficiency, allowing for seamless updates and integrations of new data or code changes into the analysis workflow.
- `run_job.py` is included in `CI.yml` as "run databricks job" to automatically run databricks jobs when Github action is triggered through push. 
- Automation is also achieved by creating a job workflows in databricks to allow running extract, transform_load and query_viz in one job environment. 

## Preparation
**1. Establish a Databricks Workspace:**
    Initiate a Databricks workspace within a cloud environment, such as Azure, to leverage its data processing and analytics capabilities.

**2. GitHub Integration:**
    Link your GitHub account with the Databricks Workspace to facilitate seamless code management and version control.

    
<img width="795" alt="Link Account Databrick" src="https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/cf3aea9d-2b40-4f15-a564-2ccbbde29db6">

    
**3. Initialization Script Setup:**
    In your Databricks cluster, implement a global initialization script. This script should define necessary environment variables, ensuring a consistent runtime environment.

**4. Cluster Configuration for PySpark:**
    Configure and activate a Databricks cluster that is optimized for running PySpark applications, enabling efficient processing of large-scale data with Spark and Python.

**5. Repository Cloning:**
    Directly clone your project’s repository into the Databricks workspace. This step brings your codebase into the Databricks environment for execution and further development.

<img width="1182" alt="clone" src="https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/0117bb7e-c6bb-4485-9a52-1e5805a6bf99">


**6. Job Automation:**
    Create and configure a Databricks job. This job will automate the execution of your data pipeline, streamlining the process and ensuring regular, reliable operation.

## Visualizations

![visual](https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/cef9a6a0-05a1-44c6-8fbf-790954483f22)

## Data Source, Data Sink (Delta Lake), and ETL Pipeline

`Extraction` : Data Source (Individual_Project3_Kelly_Tong/mylib/extract.py) 

`Transform_load`: Data Sink (Delta Lake) (Individual_Project3_Kelly_Tong/mylib/transform_load.py) 

`Query_viz`: perform query and generate visualization task (Individual_Project3_Kelly_Tong/mylib/query_viz.py) 

Job pipeline in Databricks Workflows: 

<img width="765" alt="Individual3 Job Run" src="https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/4375882b-a94e-4e1c-ba57-808f4087f45e">

## Data Source Storing in DBFS

DBFS: 

<img width="1159" alt="DBFS" src="https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/348dc611-d298-4361-a73b-ebf5d1ecae63">

Catalog: 

<img width="1202" alt="catalog data source" src="https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/a138d5db-3ac3-45cb-aab1-730e820b522e">

## Conclusion and Recommendation

The visualization (in visualizations section above) demonstrates that Biology is the most popular discipline with the higest total population (men and women in total) among all selected major. This is, however, different from data included in all_ages.csv. Further research into all_ages and grad_students data have suggested other more popular discipline/major for men and women. This could be caused by the limited majors included in this dataset. Potential recommendation on expanding the sample size and range could benefit the data accuracy and provide more careful and meaningful conclusion. This could also be due to the fact that women_stem.csv is a subset of another dataset, meaning that not the complete view is being provided here. A comparison between women_stem dataset with the original full pictured dataset could be an improvement and extension of the currently approached discovery. 

## Building Process

All required dependencies are included in `requirements.txt` file and will be downloaded through `make install` command. 
These dependencies are also added onto each job run task in Databricks to support automatic job run workflow. 

Github Actios such as  `make lint` `make format` `make test` are also included and performed

<img width="565" alt="make lint" src="https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/e9f92033-c271-4400-99a9-77646477db3b">

<img width="418" alt="make format" src="https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/b812c5b2-d6cf-4e94-9bd6-b2029dc5c66d">

<img width="949" alt="make test" src="https://github.com/nogibjj/Individual_Project3_Kelly_Tong/assets/142815940/68081ddb-48dc-4d71-be25-485f793943e0">

