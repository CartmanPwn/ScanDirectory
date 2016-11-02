import utils

def read_into_buffer_unit_test():
    filename = "E:\\compare\\classes-local\\difxapi.dll"
    buf = utils.read_into_buffer(filename)
    print(buf[0])


def compare_file_data_unit_test():
    filename1 = "E:\\compare\\classes-local\\difxapi.dll"
    filename2 = "E:\\compare\\classes-web\\difxapi.dll"
    ret = utils.compare_file_data(filename1,filename2)
    print(ret)