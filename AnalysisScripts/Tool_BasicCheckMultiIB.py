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
from BasicConfig import *


if __name__ == "__main__":
    # Use a extra basic_check.ini is troublesome,but global check will get a huge FPS decrease in some game.
    basic_check_filename = LoaderFolder + "Mods/basic_check.ini"

    # Create a new basic_check.ini
    file = open(basic_check_filename, "w+")
    file.write("")
    file.close()

    vertex_shader_list = []
    # all VertexShader will show in IndexBuffer related files.
    for draw_ib in draw_ibs:
        ib_files = get_filter_filenames(draw_ib, ".txt")
        # Get all VertexShader need to check

        for filename in ib_files:
            vs = filename.split("-vs=")[1][0:16]
            if vs not in vertex_shader_list:
                vertex_shader_list.append(vs)

    print(vertex_shader_list)


    # Add texcoord VertexShader check
    texcoord_check_slots = ["vb1", "ib"]
    action_check_slots = ["vb0"]

    # output str
    output_str = ""
    output_str = output_str + ";Texcoord Check List:" + "\n" + "\n"
    for vs in sorted(vertex_shader_list):
        section_name = "[ShaderOverride_VS_" + vs + "_Test_]"
        print("add section :" + section_name)

        output_str = output_str + section_name + "\n"
        output_str = output_str + "hash = " + vs + "\n"
        output_str = output_str + "if $costume_mods" + "\n"
        for slot in texcoord_check_slots:
            output_str = output_str + "  checktextureoverride = " + slot + "\n"
        output_str = output_str + "endif" + "\n"
        output_str = output_str + "\n"


    # Finally save the config file.
    output_file = open(basic_check_filename, "w")
    output_file.write(output_str)
    output_file.close()


