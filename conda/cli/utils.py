import os
import sys
from os.path import abspath, expanduser, join

from conda.config import ROOT_DIR, config


default_prefix = config().default_environment


def add_parser_prefix(p):
    npgroup = p.add_mutually_exclusive_group()
    npgroup.add_argument(
        '-n', "--name",
        action = "store",
        help = "name of environment (directory in %s/envs)" % ROOT_DIR,
    )
    npgroup.add_argument(
        '-p', "--prefix",
        action = "store",
        help = "full path to environment prefix (default: %s)" %
                        default_prefix,
    )


def get_prefix(args):
    if args.name:
        return join(ROOT_DIR, 'envs', args.name)

    if args.prefix:
        return abspath(expanduser(args.prefix))

    return default_prefix


def add_parser_yes(p):
    p.add_argument(
        "--yes",
        action = "store_true",
        default = False,
        help = "do not ask for confirmation",
    )
    p.add_argument(
        "--dry-run",
        action = "store_true",
        default = False,
        help = "only display what would have been done",
    )


def confirm(args):
    if args.dry_run:
        sys.exit(0)
    if args.yes:
        return
    proceed = raw_input("Proceed (y/n)? ")
    if proceed.strip().lower() in ('y', 'yes'):
        return
    sys.exit(0)


def add_parser_quiet(p):
    p.add_argument(
        '-q', "--quiet",
        action = "store_true",
        default = False,
        help = "do not display progress bar",
    )
