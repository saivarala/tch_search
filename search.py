import click
import json
from csv_loader import CsvData

@click.command()
@click.argument('filter')
def cli(filter):
    """
    Search module to find data in data.csv.
    
    1. return a list[dict] with column name and filter value \n
            like ' python search.py "city = New York " ' \n
    2. return a list[dict] with filter on city and state \n
            like 'python search.py "city = New York & state = NY" '
    
    """

    if '&' not in filter:
        column, filter_value = filter.split('=')
        csv_data = CsvData()
        res = csv_data.filter_by_col(column.strip().title(), str(filter_value).strip())
        if len(res):
            click.echo(f"Results found\n")
            click.echo(json.dumps(res))    
        else:
            click.echo(f"No results found for {column} : {filter_value}")
        

    else:
        
        filter1 , filter2 = filter.split("&")
        city_column, city = filter1.split('=')
        state_column , state = filter2.split('=')## use regex group to get 

        ## conditon to make only ## city and state are keyed

        if city_column.lower() == 'city' and state_column.lower() == 'state':     
            csv_data = CsvData()
            res = csv_data.filter_city_state(str(city).strip(), str(state).strip())
            if len(res):
                click.echo(f"Results found\n")
                click.echo(json.dumps(res))    
            else:
                click.echo(f"No results found for City : {city} and State : {state}")
        else:
            click.echo("Please check city and state parameter names. & can be used only for city & state combo")
if __name__ == "__main__":
    cli()


