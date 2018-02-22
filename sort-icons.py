#!/usr/bin/env python3

import sys
import os
import shutil
import json


class SortIcons:
    def __init__(self, path):
        self.path = path
        self.sorted_path = os.path.join(self.path, "sorted")
        self.categories = ("action", "alert", "av", "communication", "content", "device", "editor", "file",
                           "hardware", "image", "maps", "navigation", "notification", "places", "social", "toggle")
        if not self.verify_path():
            print("Valid Path\n")
            self.sort()
        else:
            print("Invalid Path!")
            return

    def sort(self):
        # make self.sorted_path/
        os.makedirs(self.sorted_path, exist_ok=True)
        for category in os.listdir(self.path):
            if category in self.categories:

                # make self.sorted_path/<category>/
                os.makedirs(os.path.join(self.sorted_path, category), exist_ok=True)

                # current dir: path/<category>/
                os.chdir(os.path.join(self.path, category))
                for size in os.listdir("."):
                    if os.path.isdir("."):

                        # current dir: path/<category>/<size>/
                        os.chdir(os.path.join(self.path, category, size))
                        for file in os.listdir("."):
                            if os.path.isfile(file):
                                # make self.sorted_path/<category>/<file_name>
                                os.makedirs(os.path.join(
                                    self.sorted_path,
                                    category,
                                    "_".join(file.split("_")[0:-1])
                                ), exist_ok=True)

                                # make self.sorted_path/<category>/<file_name>/<res>/
                                os.makedirs(os.path.join(
                                    self.sorted_path,
                                    category,
                                    "_".join(file.split("_")[0:-1]),
                                    file.split("_")[-1].split(".")[0]
                                ), exist_ok=True)

                                # make self.sorted_path/<category>/<file_name>/<res>/<size>
                                os.makedirs(os.path.join(
                                    self.sorted_path,
                                    category,
                                    "_".join(file.split("_")[0:-1]),
                                    file.split("_")[-1].split(".")[0],
                                    size
                                ), exist_ok=True)

                                # copy file to new dir
                                shutil.copy2(
                                    os.path.realpath(file),
                                    os.path.join(
                                        self.sorted_path,
                                        category,
                                        "_".join(file.split("_")[0:-1]),
                                        file.split("_")[-1].split(".")[0],
                                        size,
                                        file
                                    )
                                )

                                print("\"%s\"\tcopied to \t\"%s/\"" % (file, os.path.join(
                                    self.sorted_path,
                                    category,
                                    "_".join(file.split("_")[0:-1]),
                                    file.split("_")[-1].split(".")[0],
                                    size
                                )))

    def verify_path(self):
        try:
            with open(os.path.join(self.path, "package.json")) as open_data:
                data = json.loads(open_data.read())
                if data['repository']['url'] == "https://github.com/google/material-design-icons":
                    for category in self.categories:
                        for directory in os.listdir(self.path):
                            if category not in directory:
                                pass
                            else:
                                return True
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass

        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        SortIcons(sys.argv[1])
    else:
        epath = input("Enter path to icons: ")
        SortIcons(epath)
