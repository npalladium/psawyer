import json
from typing import List, Optional

import typer
from psaw import PushshiftAPI

from psawyer.utils import get_kwargs, SortOption


CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help", "help"]}

app = typer.Typer(context_settings=CONTEXT_SETTINGS)


@app.command(hidden=True)
def help(ctx: typer.Context):
    print(ctx.parent.get_help())


@app.command()
def submissions(
    query: str = typer.Option(None, "--query", "-q"),
    subreddit: str = typer.Option(None, "--subreddit", "-s"),
    author: str = typer.Option(None, "--author", "-a"),
    sort: SortOption = typer.Option("desc", "--sort", "-s", case_sensitive=False),
    fields: Optional[List[str]] = typer.Option(None, "--field", "-f"),
    filter: Optional[List[str]] = typer.Option(None, "--filter", "-r"),
    limit: int = typer.Option(10, "--limit", "-l"),
):
    """Retrieve submissions."""
    api = PushshiftAPI()
    gen = api.search_submissions(**get_kwargs())
    typer.echo(json.dumps([x._asdict() for x in gen]))


@app.command()
def comments(
    query: str = typer.Option(None, "--query", "-q"),
    subreddit: str = typer.Option(None, "--subreddit", "-s"),
    author: str = typer.Option(None, "--author", "-a"),
    sort: SortOption = typer.Option("desc", "--sort", "-s", case_sensitive=False),
    fields: Optional[List[str]] = typer.Option(None, "--field", "-f"),
    filter: Optional[List[str]] = typer.Option(None, "--filter", "-r"),
    limit: int = typer.Option(10, "--limit", "-l"),
):
    """Retrieve comments."""
    api = PushshiftAPI()
    gen = api.search_comments(**get_kwargs())
    typer.echo(json.dumps([x._asdict() for x in gen]))


if __name__ == "__main__":
    app()
