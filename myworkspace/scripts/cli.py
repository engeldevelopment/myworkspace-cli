import click

from myworkspace.services import WorkspaceService


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
    service = WorkspaceService(name=name)
    work = service.build() 
    if work.was_created:
        click.echo("Se creó exitosamente!")


if __name__ == "__main__":
    workspace()
