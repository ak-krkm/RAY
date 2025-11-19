import click
import os

@click.command()
@click.argument("query", type=str)
@click.option("-f", "--file", type=click.Path(exists=True), help="Path to an auxiliary file (optional).")
def main(query, file):
    """
    Ray is a CLI based tool, built to help penetration testers and students in finding web-based vulberabilities

    QUERY is the mandatory text argument.
    Use -f FILE for an optional file.
    """
    click.echo(f"Query: {query}")
    if file:
        click.echo(f"Auxiliary file: {file}")


  

        
    # TODO: Here you would call your AI model, e.g.:
    # from ai_model.model import run_inference
    # result = run_inference(query, image, file)
    # click.echo(result)

if __name__ == "__main__":
    main()
