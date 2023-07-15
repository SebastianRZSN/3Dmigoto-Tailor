"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import configparser
import os
import glob
import shutil
import re


global_config = configparser.ConfigParser()
global_config.read("Configs/global_config.ini", "utf-8")
config_folder = global_config["Global"]["config_folder"]

preset_config = configparser.ConfigParser()
preset_config.read(config_folder + "/preset.ini", "utf-8")

OutputFolder = preset_config["General"]["OutputFolder"]
LoaderFolder = preset_config["General"]["LoaderFolder"]
FrameAnalyseFolder = preset_config["General"]["FrameAnalyseFolder"]
mod_name = preset_config["General"]["mod_name"]


draw_ibs = preset_config["Merge"]["draw_ibs"].split(",")


def get_latest_folder():
    filenames = os.listdir(LoaderFolder)
    FA_filenames = []
    for filename in filenames:
        if filename.startswith("FrameAnalysis-"):
            FA_filenames.append(filename)

    FA_filenames.sort()
    return FA_filenames[-1]


if FrameAnalyseFolder == "latest":
    FrameAnalyseFolder = get_latest_folder()

WorkFolder = LoaderFolder + FrameAnalyseFolder
print("FrameAnalyseFolder: " + FrameAnalyseFolder)


def get_filter_filenames(in_str, end_str,target_folder=WorkFolder):
    filtered_filenames = []
    filenames = os.listdir(target_folder)
    for filename in filenames:
        if in_str in filename and filename.endswith(end_str):
            filtered_filenames.append(filename)
    return filtered_filenames

