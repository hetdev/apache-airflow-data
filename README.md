# apache-airflow-data
This project expose 3 dags to retrieve, transform and load 
data base in different scenarios.

### Installation

Install virtual environment lib.

```
pip install virtualenv
```

Create a virtual environment.

```
python<version> -m venv <virtual-environment-name>
```

Activate the venv.

```
source env/bin/activate
```

Install the Apache Airflow Lib.
For more information go to [Apache docs](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)

```bash
pip install 'apache-airflow==2.9.2' \        
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.8.txt"

```

Setup the env variables.
```bash
export AIRFLOW_HOME="~/{project_directory}"}
```
For example:
```
export AIRFLOW_HOME="~/Desktop/apache-airflow-data"
```

### Startup

Execute the following command to start up the Airflow service
```
airflow standalone
```

The dags can be filter by tag "hetdev"



