import os.path
import os
def read_into_buffer(filename):
    if(os.path.exists(filename)==False):
        print(filename+"is not exists.")
        return None
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

def compare_file_data(filename1, filename2):
    buf1 = read_into_buffer(filename1)
    buf2 = read_into_buffer(filename2)
    return (buf1==buf2)



def compare_directory_data(directory1,directory2):
    unequal_file_info_list =[]
    filenames = [name for name in os.listdir(directory1)
                 if os.path.isfile(os.path.join(directory1,name))]
    dirnames = [name for name in os.listdir(directory1)
                 if os.path.isdir(os.path.join(directory1,name))]
    for name in filenames:
        isequal = compare_file_data(os.path.join(directory1,name),os.path.join(directory2,name))
        if(isequal==False):
            unequal_file_info_list.append(os.path.join(directory1,name)+" and "+os.path.join(directory2,name)+" is not equal")
    for name in dirnames:
        unequal_file_info_list.extend(compare_directory_data(os.path.join(directory1,name),os.path.join(directory2,name)))
    return unequal_file_info_list