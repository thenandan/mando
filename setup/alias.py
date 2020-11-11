import os
import click


def create_alias(args):
    cwd = os.getcwd() + '/' + args[0]
    with open(os.path.expanduser('~/.bashrc')) as bash:
        lines = ''.join(bash.readlines())
        is_alias_exists = 'alias mando=' in lines

    with open(os.path.expanduser("~/.bashrc"), 'at') as bashrc:
        if is_alias_exists:
            click.secho('Alias mando already exists. Please remove and try again.', fg='green')
        else:
            bashrc.write("\n # Added By Mando \n")
            bashrc.write("alias mando='python3 " + cwd + "'")
