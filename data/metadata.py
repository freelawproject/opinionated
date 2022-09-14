"Our main tool for processing opinionated data"
import argparse
import datetime
import json
from glob import glob
from typing import Dict, Union, List


def update_metadata_file(options: Dict[str, str]) -> None:
    """Update or generate metadata file

    :param options: The options to use
    :return: None
    """

    metadata_file: Dict[str, Union[List[str], str]] = {}

    repo = options["repository"]
    file_list = glob(f"data/{repo}/*/*.json")
    file_list = [file.replace("data/harvard/", "") for file in file_list]

    metadata_file["updated"] = datetime.date.today().isoformat()
    metadata_file["files"] = file_list
    metadata_file["files"].sort()

    with open(f"data/{repo}/missing-files.json", "w", encoding="utf8") as file:
        json.dump(metadata_file, file, indent=4, sort_keys=False)


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
        required=False,
        default="update",
    )
    parser.add_argument(
        "-r",
        "--repository",
        help="The repository to generate the metadata for.",
        required=False,
        default="harvard",
    )

    args = vars(parser.parse_args())
    VALID_ACTIONS[args["action"]](options=args)
