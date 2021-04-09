import click

from workspace.core import WorkSpace


@click.group("workspace")
def workspace():
    """Una Herramienta para construir mi espacio de trabajo."""
    pass


@workspace.command()
@click.option(
    "--name",
    default="dev",
    type=click.STRING,
    help="Nombre que quieras darle a tu workspace",
)
def build(name):
    workspace = WorkSpace(name=name)
    workspace.build()
    if workspace.was_created:
        click.echo("Se creó exitosamente!")


if __name__ == "__main__":
    workspace()
