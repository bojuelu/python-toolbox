# coding: utf-8

import traceback
import os


def that_local_file_service_url():
    return "http://192.168.1.110:9487"


def that_local_file_service_execute_abs_path():
    return os.path.join(os.path.expanduser("~"), 'Services', 'pure-file-service')


def copy_file(source_file_path, destn_file_name, destn_dir):
    """
    :param source_file_path:
        The source file abs path. ex: /home/mifly/Service/cherrypyservice/tmp/PNGYYGBB/tmp1478523698.jpg

    :param destn_file_name:
        The destination file name. ex: hammer1.jpg

    :param destn_dir:
        The destination directory, it will be create under the local file service path, and put the destn file in it.

    :return:
        Url, the file can be download via this url. Null or empty means copy failed.
    """

    file_url = ''
    try:
        with open(source_file_path, 'r') as source_ptr:
            destn_full_dir = os.path.join(that_local_file_service_execute_abs_path(), destn_dir)

            if not os.path.exists(destn_full_dir):
                os.makedirs(destn_full_dir)
                pass

            dest_file_path = os.path.join(destn_full_dir, destn_file_name)
            print('dest_file_path ', dest_file_path)

            with open(dest_file_path, 'wb') as destn_ptr:

                source_size = int(os.path.getsize(source_file_path))

                buff_size = 1024

                destn_file_size = 0

                while True:
                    buff = source_ptr.read(buff_size)
                    destn_file_size += len(buff)
                    if not buff:
                        break
                    destn_ptr.write(buff)
                    pass  # while True
                pass  # with open(dest_file_path ...
            pass  # with open(source_file_path ...
        file_url = that_local_file_service_url() + '/' + destn_dir + '/' + destn_file_name
        pass
    except:
        file_url = ''
        print(traceback.format_exc())
        pass
    return file_url


def del_file(url):
    result = ''
    try:
        path = url.replace(that_local_file_service_url(), that_local_file_service_execute_abs_path())

        print('del path: ', path)

        if os.path.exists(path):
            os.remove(path)
            result = 'ok'
        else:
            result = 'file not found'
        pass
    except:
        print(traceback.format_exc())
        result = 'exception occur'
        pass
    return result
