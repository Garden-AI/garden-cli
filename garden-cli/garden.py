import typer
from typing import List, Optional
from garden_ai import Garden
import json
import datetime

app = typer.Typer()

def create_garden(name: str, authors: List[str], description: str):
    garden = {
        "title": name,
        "authors": authors,
        "description": description
    }
    with open(f"garden.json", "w") as f:
        json.dump(garden, f, indent=4)
    typer.echo(f"Garden {name} created successfully.")

@app.command()
def create(
    name: str = typer.Option(None),
    authors: list[str] = typer.Option(None),
    description: str = typer.Option(None),
):
    """Create a Garden entity."""
    if not name:
        name = typer.prompt("Enter garden name: ")
    if not authors:
        authors = typer.prompt("Enter authors: ", type=str)
    if not description:
        description = typer.prompt("Enter description: ")
    create_garden(name, authors, description)

@app.command()
def other(test=True):
    """Other command."""
    typer.echo(f"Other command called with test={test}")

if __name__ == "__main__":
    app()