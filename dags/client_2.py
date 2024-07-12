import csv
import json

from airflow import DAG
from datetime import datetime
from airflow.decorators import task, dag

with DAG(
    dag_id="client_2_hetdev",
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
        Transform task to get all the data films released after 1994.
        """

        data_list_iterator = iter(data_list)
        films = []

        def filter_by_year(item):
            year = int(((item["year"]).split(" "))[0])
            if year > 1994:
                return True
            else:
                return False

        for item in data_list_iterator:
            if filter_by_year(item):
                films = films + item["films"]

        return {"films": films}

    @task()
    def load(data: dict):
        """
        #### Load task
        Load task to save the data as a client_2.csv file
        """

        fields = [
            "Detail URL",
            "Film",
            "Producer(s)",
            "Production Company(s)",
            "Wiki URL",
            "Winner",
        ]

        # name of csv file
        filepath = "./output/client_2.csv"
        with open(filepath, "w") as csvfile:
            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            # writing headers (field names)
            writer.writeheader()

            # writing data rows
            writer.writerows(data["films"])

            return

    data_dict = extract()
    films_data = transform(data_dict)
    load(films_data)
