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
    work = WorkSpace(name=name)
    work.add_child(WorkSpace(name="python"))
    work.add_child(WorkSpace(name="js"))
    work.add_child(WorkSpace(name="ruby"))
    work.build()
    if work.was_created:
        click.echo("Se creó exitosamente!")


if __name__ == "__main__":
    workspace()
