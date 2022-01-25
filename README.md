
# Opinionated

Opinionated is a repository of fixes for a large dataset of opinions.

Its main goal is to be a collection of fixes for the Harvard import data.

## Background

This repository is a collection of fixes for the Harvard import data and is to be used with
Courtlistener.com and the Harvard dataset.  You can learn more about courtlistener [here](https://github.com/freelawproject/courtlistener/)

## Quick Start

You can update the missing-files json, which is used to update data in the Harvard import by running the following command:

    python data/metadata.py -a update -r harvard


# Tests

Currently there is only one test which you can run by running the command:

    python -m unittest discover -s tests -p 'test_*.py'

This test simply validates that the data is in the correct format and updated.  Essentially, if you
add cases to the data source but don't update the missing-files.json it will throw an error.

## License

This repository is available under the permissive BSD license, making it easy and safe to incorporate in your own libraries.

Pull and feature requests welcome. Online editing in GitHub is possible (and easy!)
