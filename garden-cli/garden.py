import typer
import json
import datetime

app = typer.Typer()

def create_garden(name: str, date_created: str, description: str):
    garden = {
        "name": name,
        "date_created": date_created,
        "description": description
    }
    with open(f"garden.json", "w") as f:
        json.dump(garden, f)
    typer.echo(f"Garden {name} created successfully.")

@app.command()
def create(
    name: str = typer.Option(None),
    date_created: str = typer.Option(None),
    description: str = typer.Option(None),
):
    """Create a Garden entity."""
    if not name:
        name = typer.prompt("Enter garden name: ")
    if not date_created:
        date_created = typer.prompt("Enter date created (YYYY-MM-DD): ", type=str)
    while True:
        try:
            date_created = datetime.datetime.strptime(date_created, '%Y-%m-%d').strftime('%Y-%m-%d')
            break
        except ValueError:
            date_created = typer.prompt("Invalid date format. Enter date created (YYYY-MM-DD): ", type=str)
    if not description:
        description = typer.prompt("Enter description: ")
    create_garden(name, date_created, description)

@app.command()
def other(test=True):
    """Other command."""
    typer.echo(f"Other command called with test={test}")

if __name__ == "__main__":
    app()