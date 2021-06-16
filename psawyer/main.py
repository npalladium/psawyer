import typer

import psawyer.utils as utils

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help", "help"]}

app = typer.Typer(context_settings=CONTEXT_SETTINGS)


@app.command(hidden=True)
def help(ctx: typer.Context):
    print(ctx.parent.get_help())


@app.command()
def submissions():
    typer.echo(utils.get_kwargs())


@app.command()
def comments():
    typer.echo(utils.get_kwargs())


if __name__ == "__main__":
    app()
