import json

from airflow import DAG
from datetime import datetime
from airflow.decorators import task, dag

with DAG(
    dag_id="client_1_hetdev",
    start_date=datetime(2022, 1, 1),
    schedule="0 0 * * *",
    tags=["hetdev"],
):

    @task()
    def extract():
        """
        #### Extract task
        Extract task get the data['results'] from input/data.json
        """

        json_file = open("./input/data.json")

        # returns JSON object as
        # a dictionary
        data_dict = json.load(json_file)

        # Closing file
        json_file.close()

        return data_dict["results"]

    @task(multiple_outputs=True)
    def transform(data_list: list):
        """
        #### Transform task
        Transform task to get all the winners from the incoming data
        """

        data_list_iterator = iter(data_list)
        winners = []

        for item in data_list_iterator:
            winners.append(list(filter(lambda x: x["Winner"], item["films"]))[0])

        return {"winners": winners}

    @task()
    def load(data: dict):
        """
        #### Load task
        Load task to save the data as a client_1.json file
        """

        json_object = json.dumps(data, indent=4)

        # Writing to client_1.json
        with open("./output/client_1.json", "w") as outfile:
            outfile.write(json_object)
            return

    data_dict = extract()
    winners_data = transform(data_dict)
    load(winners_data)
