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
import os


def remove_log_files(log_path):
    root_log_files = os.listdir(log_path)
    for file in root_log_files:
        if file.endswith(".log"):
            os.remove(log_path + "/" + file)


if __name__ == "__main__":
    '''
    用于删除永劫无间日志文件，但是其实删了也没啥用，因为日志在记录完成的那一刻就已经上传到服务端了。
    '''
    log_path_list = []
    log_path_list.append("C:/Users/Administrator/AppData/LocalLow/24Entertainment/Naraka/")
    log_path_list.append("C:/Program Files (x86)/Steam/steamapps/common/NARAKA BLADEPOINT/")
    log_path_list.append("C:/Program Files (x86)/Steam/steamapps/common/NARAKA BLADEPOINT/NarakaBladepoint_Data/1.4.2/d90")
    log_path_list.append("C:/Program Files (x86)/Steam/steamapps/common/NARAKA BLADEPOINT/NarakaBladepoint_Data/1.4.6/d90")
    log_path_list.append("C:/Program Files (x86)/Steam/steamapps/common/NARAKA BLADEPOINT/logs")

    for log_file_path in log_path_list:
        remove_log_files(log_file_path)

    print("All log file deleted")



