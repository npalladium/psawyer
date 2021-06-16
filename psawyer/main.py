import typer

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help", "help"]}

app = typer.Typer(context_settings=CONTEXT_SETTINGS)


@app.command(hidden=True)
def help(ctx: typer.Context):
    print(ctx.parent.get_help())


@app.command()
def submissions():
    typer.echo("Submissions.")


@app.command()
def comments():
    typer.echo("Comments.")


if __name__ == "__main__":
    app()
