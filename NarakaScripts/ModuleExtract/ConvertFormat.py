# coding=gbk
import subprocess
import os

def convert_format(quickbms_path, bms_script_path, target_file_path):
    # wav文件转为wem文件
    shell_text = quickbms_path + ' -w ' + bms_script_path + ' ' + target_file_path 
    decode_process = subprocess.Popen(shell_text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(decode_process.communicate()[0])


def convert_one(target_file_path):
    ModuleExtractPath = "C:/Users/Administrator/PycharmProjects/mods/NarakaBladepoint/ModuleExtract/"
    quick_bms_path = ModuleExtractPath + "quickbms.exe"
    bms_script_path = ModuleExtractPath + "naraka_convert_v2.bms"
    convert_format(quick_bms_path,bms_script_path,target_file_path)


def convert_all(target_folder_path):
    for i in os.listdir(target_folder_path):  
        file_data = target_folder_path + "/" + i
        if os.path.isfile(file_data):  
            convert_one(file_data)
        else:
            convert_all(file_data)
    pass


if __name__ == "__main__":
    # streaming_assets_folder = "D:\\Desktop\\test"
    streaming_assets_folder = "C:/StreamingAssetsDecrepted"
    convert_all(streaming_assets_folder)
    # convert_one(target_path)