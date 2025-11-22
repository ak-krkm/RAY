import click
import os
from ray_model import runInference
@click.command()
@click.argument("query", type=str)
@click.option("-f", "--file", type=click.Path(exists=True), help="Path to an auxiliary file (optional).")
def main(query, file):
    """
    Ray is a CLI based tool, built to help penetration testers and students in finding web-based vulberabilities

    QUERY is the mandatory text argument.
    Use -f FILE for an optional file.
    """
    content = ""
    click.echo(f"Query: {query}")
    if file:
        try:
            with open(file,'r') as file:
                content = file.read()
        except Exception as e:
            click.echo(f"error reading tht file : {e}")
            return

    response = runInference(query,content)
    click.echo(response)
if __name__ == "__main__":
    main()