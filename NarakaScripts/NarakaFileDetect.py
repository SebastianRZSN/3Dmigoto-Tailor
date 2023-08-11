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

def get_file_sizes(directory):
    file_sizes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes.append((file_path, file_size))
    return file_sizes

def write_to_file(file_sizes, output_file):
    with open(output_file, 'w') as file:
        file.write("文件名\t\t\t\t\t\t文件路径\t\t\t\t\t\t文件大小\n")
        file.write("-----------------------------------------------------------\n")
        for file_path, file_size in file_sizes:
            file.write(f"{os.path.basename(file_path)}\t\t\t\t\t{file_path}\t\t\t\t\t{file_size} bytes\n")

def sort_file_sizes(file_sizes):
    return sorted(file_sizes, key=lambda x: x[1], reverse=True)

def main():
    directory = "C:/StreamingAssets"  # 替换为要遍历的目录路径
    output_file = 'file_sizes.txt'  # 输出结果的文件名

    file_sizes = get_file_sizes(directory)
    sorted_file_sizes = sort_file_sizes(file_sizes)
    write_to_file(sorted_file_sizes, output_file)

    print(f"结果已写入文件: {output_file}")

if __name__ == '__main__':
    '''
    用于从大到小排列永劫无间资源文件，可以在新版本更新的时候快速确定每个英雄的模型资源存储位置，
    假如版本更新时资源位置发生变动，这个脚本就派上用场了。
    '''
    main()