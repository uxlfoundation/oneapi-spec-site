import os
import tempfile
import zipfile

import click
import yaml
import requests

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

def extract_release(releases_dir, url):
    file = download_file(url)
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(releases_dir)
    os.remove(file)

def extract_releases(update, site_dir, config):
    releases_dir = os.path.join(site_dir, 'versions')
    os.makedirs(releases_dir, exist_ok=update)
    for release in config['releases']:
        if update and os.path.exists(os.path.join(releases_dir, release['name'])):
            continue
        f = extract_release(releases_dir, release['url'])

    latest = os.path.join(releases_dir, 'latest')
    if update and os.path.exists(latest):
        os.remove(latest)
    try:
        os.symlink(config['latest'], latest)
    except Exception as e:
        raise click.ClickException(f"Could not create latest link: {e}")

@click.group()
def cli():
    pass

@cli.command()
@click.option("--update", is_flag=True, help="Update the site.")
@click.option('--dir', type=click.Path(), default="dist")
def build(update, dir):
    """Build the site."""

    # get configuration from site.yaml
    try:
        with open('site.yaml') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    except Exception as e:
        raise click.ClickException(f"Could not load site configuration: {e}")

    try:
        os.makedirs(dir, exist_ok=update)
    except Exception as e:
        raise click.ClickException(f"Site directory {dir} could not be created: {e}")

    extract_releases(update, dir, config)

if __name__ == '__main__':
    cli()
