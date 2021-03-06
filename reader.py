"""

"""
from collections import defaultdict
import json
import os

from bs4 import BeautifulSoup
from lxml import etree
import yaml


def get_root(filename):
    parser = etree.XMLParser(load_dtd=True, no_network=False)
    tree = etree.parse(filename, parser=parser)
    return tree.getroot()


def get_entries(filename):
    root = get_root(filename)
    lemmata = set()
    d = {}
    for entry in root.findall(".//entry"):
        lemma = entry.get("key", "")
        entry_bs = BeautifulSoup(etree.tostring(entry), features="lxml")
        d[lemma] = entry_bs.text.strip()
        lemmata.add(lemma)
    return d


def save_yaml(data, filename):
    with open(filename, "w") as f:
        yaml.dump(data, f)


def read_yaml(filename):
    with open(filename, "r") as f:
        return yaml.safe_load(f)


def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def read_json(filename):
    with open(filename, "r") as f:
        json.load(f)


def save_json_by_letter(data, directory_name, ):
    """
    >>> entries = read_yaml("lewis.yaml")
    >>> save_json_by_letter(entries, "entries")

    :param data:
    :param directory_name:
    :return:
    """
    first_letters = set()
    entries_by_letter = defaultdict(list)
    for entry in data:
        first_letters.add(entry[0])
        entries_by_letter[entry[0].lower()].append({entry: data[entry]})
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    if os.path.exists(directory_name):
        for i in entries_by_letter:
            with open(os.path.join(directory_name, str(i) + ".json"), "w") as f:
                json.dump(entries_by_letter[i], f)


if __name__ == "__main__":
    # entries = get_entries("lewis.xml")
    # save_yaml(entries, "lewis.yaml")
    entries = read_yaml("lewis.yaml")
    # save_json(data, "lewis.json")
