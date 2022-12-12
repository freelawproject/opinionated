"Our main tool for processing opinionated data"
import argparse
import datetime
import json
from glob import glob
from typing import Dict


def update_metadata_file(options: Dict[str, str]):
    """Update or generate metadata file

    :param options: The
    :return:
    """

    metadata_file = {}
    repo = options["repository"]
    metadata_file["updated"] = datetime.date.today().isoformat()
    file_list = glob(f"data/{repo}/*/*.json")
    file_list = [file.replace("data/harvard/", "") for file in file_list]

    metadata_file["files"] = sorted(file_list)

    with open(f"data/{repo}/missing-files.json", "w", encoding="utf8") as file:
        json.dump(metadata_file, file, indent=4)


class Command:
    """Generate metadata file"""

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
