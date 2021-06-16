import json

import typer
from psaw import PushshiftAPI

import psawyer.utils as utils

api = PushshiftAPI()

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help", "help"]}

app = typer.Typer(context_settings=CONTEXT_SETTINGS)


@app.command(hidden=True)
def help(ctx: typer.Context):
    print(ctx.parent.get_help())


@app.command()
def submissions():
    gen = api.search_submissions(**utils.get_kwargs())
    typer.echo(json.dumps([x._asdict() for x in gen]))


@app.command()
def comments():
    gen = api.search_comments(**utils.get_kwargs())
    typer.echo(json.dumps([x._asdict() for x in gen]))


if __name__ == "__main__":
    app()
