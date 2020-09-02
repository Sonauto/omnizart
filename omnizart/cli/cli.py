"""The entry point of the ``omnizart`` command.

Sub-commands are also added here.

Examples
--------
.. code-block:: bash

    omnizart --help
    omnizart music --help
"""

import click

from omnizart.cli.music import music


@click.group()
def entry():
    pass


entry.add_command(music)

if __name__ == "__main__":
    entry()