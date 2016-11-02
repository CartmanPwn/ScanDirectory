import os
import utils
import utilunittest
directory1 = "E:\\compare\\classes-local\\"
directory2 = "E:\\compare\\classes-web\\"

#utilunittest.read_into_buffer_unit_test()
#utilunittest.compare_file_data_unit_test()
unequal_file_info_list = utils.compare_directory_data(directory2,directory1)
print(unequal_file_info_list.__len__())
for unequal_file_info in unequal_file_info_list:
    print(unequal_file_info)