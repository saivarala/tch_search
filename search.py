import click
import json
from csv_loader import CsvData

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('filter')
def find(filter):
    column, city = filter.split('=')
    print(column, city)
    print(city)
    csv_data = CsvData()
    res = csv_data.filter_col(column.strip().title(), str(city).strip())
    print(json.dumps(res))

if __name__ == "__main__":
    find()


