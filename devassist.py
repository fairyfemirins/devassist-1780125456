#!/usr/bin/env python3
"""
DevAssist: AI-Powered Developer Assistant CLI
"""

import click
import requests
import subprocess
import json
from typing import Optional


@click.group()
def cli():
    """DevAssist: Your AI-powered developer assistant."""
    pass


@cli.command()
def version():
    """Show the version of DevAssist."""
    click.echo("DevAssist v0.1.0")


@cli.command()
@click.argument("query", type=str)
def explain(query: str):
    """Explain errors or concepts from natural language queries."""
    # TODO: Integrate with LLM or error database
    click.echo(f"Analyzing query: {query}")
    click.echo("This feature will use an LLM to explain errors or concepts.")


@cli.command()
@click.argument("library", type=str)
def docs(library: str):
    """Fetch documentation for a library or framework."""
    # TODO: Integrate with official docs (e.g., Python, requests, Django)
    click.echo(f"Fetching docs for: {library}")
    click.echo("This feature will fetch official documentation.")


@cli.command()
@click.argument("pattern", type=str)
def search(pattern: str):
    """Search local codebase for functions, variables, or patterns."""
    try:
        result = subprocess.run(
            ["rg", "--json", pattern],
            capture_output=True,
            text=True,
            check=True,
        )
        matches = [json.loads(line) for line in result.stdout.splitlines()]
        for match in matches:
            if match["type"] == "match":
                path = match["data"]["path"]["text"]
                line_num = match["data"]["line_number"]
                text = match["data"]["lines"]["text"]
                click.echo(f"{path}:{line_num} - {text.strip()}")
    except subprocess.CalledProcessError:
        click.echo("No matches found or `ripgrep` not installed.")
    except FileNotFoundError:
        click.echo("Error: `ripgrep` (rg) is not installed. Install it from https://github.com/BurntSushi/ripgrep")


if __name__ == "__main__":
    cli()