"""Into the Breach Desktop — Keep Into the Breach data folders on disk: dated copies of config and export files before a patch."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='into_the_breach_desktop',
        description='Keep Into the Breach data folders on disk: dated copies of config and export files before a patch.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Into the Breach Desktop')
    print('Archive Into the Breach files on this machine before you change the install.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
