import argparse
import datetime
import json
from glob import glob


def update_metadata_file(options):
    """Update metadata file"""

    metadata_file = {}
    repo = options["repository"]
    metadata_file["updated"] = datetime.date.today().isoformat()
    file_list = glob(f"data/{repo}/*/*.json")

    metadata_file["files"] = file_list

    with open(f"data/{repo}/missing-files.json", "w") as f:
        json.dump(metadata_file, f, indent=4)


class Command(object):
    help = "Update metadata file for use with Courtlistener."

    VALID_ACTIONS = {
        "update": update_metadata_file,
    }

    parser = argparse.ArgumentParser(description="Generate the metadata file.")
    parser.add_argument(
        "-a",
        "--action",
        help="Must choose an action",
        required=True,
    )
    parser.add_argument(
        "-r",
        "--repository",
        help="The repository to generate the metadata for.",
        required=True,
    )

    args = vars(parser.parse_args())
    VALID_ACTIONS[args["action"]](options=args)
