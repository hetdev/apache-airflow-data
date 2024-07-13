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

### Tests client_3 GZIP
```python
def client3_check():
    filepath = "./output/client_3.csv.gz"
    with gzip.open(filepath, 'rt') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

client3_check()
```

### Scalability 

1. Multi-Tenancy

Separate DAGs for Different Customers:

	•	Create separate DAGs for each customer to isolate workflows and prevent cross-customer interference.
	•	Use a naming convention to identify DAGs belonging to specific customers (e.g., customer_a_data_pipeline, customer_b_data_pipeline).

Parameterized DAGs:

	•	Use Airflow’s parameterization capabilities to create a single template DAG that can be parameterized for different customers.
	•	Pass customer-specific parameters such as data source credentials, processing requirements, and delivery endpoints.

2. Modular and Reusable Tasks

Task Reusability:

	•	Define reusable tasks and operators that can be used across multiple DAGs. For instance, tasks like data extraction, transformation, and loading (ETL) can be standardized.
	•	Use custom operators to encapsulate common logic, making it easier to maintain and extend.

3. Scalability with Dynamic DAGs

Dynamic DAG Generation:

	•	Dynamically generate DAGs based on customer configurations stored in a database or configuration file. This allows for easy addition of new customers without manual DAG creation.
	•	Use a factory pattern to create DAGs on the fly based on customer requirements.

4. Resource Management and Scheduling

Resource Pools:

	•	Use Airflow’s resource pools to manage and limit the number of concurrent tasks for each customer to ensure fair resource allocation and prevent any single customer from monopolizing resources.

Prioritization:

	•	Set priorities for different tasks and DAGs to ensure that high-priority customer workflows are executed first.
	•	Use Airflow’s SLA (Service Level Agreement) feature to monitor and manage task completion times, ensuring timely delivery according to customer requirements.

5. Monitoring and Alerts

Granular Monitoring:

	•	Implement detailed monitoring and logging for each DAG to track the performance and status of customer workflows.
	•	Use Airflow’s built-in alerting mechanism to notify stakeholders of failures or delays in specific customer DAGs.

6. Horizontal and Vertical Scaling

Horizontal Scaling:

	•	Scale out the Airflow infrastructure by adding more worker nodes to handle increased workload, ensuring that multiple customer DAGs can run concurrently.
	•	Use a distributed executor like Celery to distribute tasks across multiple worker nodes.

Vertical Scaling:

	•	Scale up individual components (e.g., increasing CPU and memory for the scheduler or database) to handle larger DAGs and more tasks.

7. Custom Plugins and Extensions

Custom Plugins:

	•	Develop custom plugins to extend Airflow’s capabilities for specific customer needs, such as custom data connectors or specialized processing tasks.
	•	Plugins can encapsulate complex logic and make it reusable across multiple customer DAGs.





