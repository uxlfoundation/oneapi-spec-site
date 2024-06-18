import os
import tempfile
import zipfile

import click
import requests
import yaml


def download_file(url):
    with requests.get(url, stream=True) as r:
        click.echo(f"Downloading {url}...", nl=False)
        r.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False) as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
            local_filename = f.name
        click.echo("done.")
    return local_filename


def patch_files(site_dir: str, old: str, new: str):
    for root, dirs, files in os.walk(site_dir):
        for file in files:
            if file.endswith(".html"):
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                content = content.replace(old, new)
                with open(os.path.join(root, file), "w") as f:
                    f.write(content)


def extract_release(site_dir: str, url: str):
    file = download_file(url)
    with zipfile.ZipFile(file, "r") as zip_ref:
        zip_ref.extractall(site_dir)
    os.remove(file)
    patch_files(
        site_dir,
        "https://spec.oneapi.com/releases/index.html",
        "https://oneapi-spec.uxlfoundation.org/",
    )


def extract_site(update: bool, site_dir: str, tree: dict):
    for key, value in tree.items():
        dir = os.path.join(site_dir, key)
        exists = os.path.exists(dir)
        try:
            os.makedirs(dir, exist_ok=update)
        except Exception as e:
            raise click.ClickException(
                f"Could not create directory {dir}: {e}"
            )
        if isinstance(value, str):
            if not exists:
                extract_release(dir, value)
        elif isinstance(value, dict):
            extract_site(update, dir, value)
        else:
            raise click.ClickException(f"Invalid value for {key}: {value}")


@click.group()
def cli():
    pass


@cli.command()
@click.option("--update", is_flag=True, help="Update the site.")
@click.option(
    "--dir", type=click.Path(), default="dist", help="Site directory."
)
@click.option(
    "--config",
    type=click.Path(),
    default="site.yaml",
    help="Site configuration.",
)
def build(update, dir, config):
    """Build the site."""

    # get configuration from site.yaml
    try:
        with open(config) as f:
            c = yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        raise click.ClickException(
            f"Could not load site configuration from {config}: {e}"
        )

    try:
        os.makedirs(dir, exist_ok=update)
    except Exception as e:
        raise click.ClickException(
            f"Site directory {dir} could not be created: {e}"
        )

    extract_site(update, dir, c["site"])


if __name__ == "__main__":
    cli()
