"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Msadministrator Package Test."""


if __name__ == "__main__":
    main(prog_name="msadministrator-package-test")  # pragma: no cover
