import os


def remove_log_files(log_path):
    root_log_files = os.listdir(log_path)
    for file in root_log_files:
        if file.endswith(".log"):
            os.remove(log_path + "/" + file)


if __name__ == "__main__":
    log_path_list = []
    log_path_list.append("C:/Users/Administrator/AppData/LocalLow/24Entertainment/Naraka/")
    log_path_list.append("C:/Program Files (x86)/Steam/steamapps/common/NARAKA BLADEPOINT/")
    log_path_list.append("C:/Program Files (x86)/Steam/steamapps/common/NARAKA BLADEPOINT/NarakaBladepoint_Data/1.4.2/d90")
    log_path_list.append("C:/Program Files (x86)/Steam/steamapps/common/NARAKA BLADEPOINT/NarakaBladepoint_Data/1.4.6/d90")
    log_path_list.append("C:/Program Files (x86)/Steam/steamapps/common/NARAKA BLADEPOINT/logs")

    for log_file_path in log_path_list:
        remove_log_files(log_file_path)

    print("All log file deleted")



