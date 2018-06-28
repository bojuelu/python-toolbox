# coding: utf-8
# Power by Aliyun oss sdk: https://help.aliyun.com/document_detail/32027.html?spm=a2c4g.11186623.6.696.UGdHfc

import oss2


class OssAgent(object):
    def __init__(self):
        self.endpoint = 'abc-de-fghijkl.mnopqrst.uvw'
        self.access_key_id = 'ABCDEFGHIJKLMNO'
        self.access_key_secret = 'rpohgaierjglkjagnkajbrgjabnrgkjnarkgjna'
        self.bucket_name = 'kikirara'
        pass

    """
    Demo code:

    oss_agent = OssAgent()
    key = 'story_{}.txt'.format(time.time())
    str_content = 'hey hey taxi, ni kai wang he chu?'
    result = oss_agent.upload_string_file(key, str_content)
    if result == 200:
        url = 'https://{}.{}/{}'.format(oss_agent.bucket_name, oss_agent.endpoint, key)
    """

    def upload_string_file(self, key, str_content, progress_callback=None, public_read=True):
        """
        :param key: (str) Remote file path. ex: "folder1/folder2/abc.txt"
        :param str_content: (str) The string content
        :param progress_callback: (function) A function can get progress. eq: show_progress(uploaded_bytes, total_bytes)
        :param public_read: (bool). Can everybody download this file?
        :return: (int) HTTP status. 200 means success
        """
        auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        bucket = oss2.Bucket(auth, self.endpoint, self.bucket_name)

        key = str(key)
        key.replace(':', '')
        key.replace(' ', '')

        assert type(str_content) is str
        result = bucket.put_object(key, str_content, progress_callback=progress_callback)
        # print('http status: {0}'.format(result.status), type(result.status))
        # print('request_id: {0}'.format(result.request_id), type(result.request_id))
        # print('ETag: {0}'.format(result.etag), type(result.etag))
        # print('date: {0}'.format(result.headers['date']), type(result.headers['date']))
        if result is None:
            return 0
        if result.status != 200:
            return result.status

        if public_read is True:
            bucket.put_object_acl(key, oss2.BUCKET_ACL_PUBLIC_READ)

        return result.status

    """
    Demo code:

    oss_agent = OssAgent()
    with open('funapp_0420_1448.apk', 'rb') as fs:
        key = 'funapp_{}.app'.format(time.time())
        result = oss_agent.upload_bin_file(key, fs)
        if result == 200:
            url = 'https://{}.{}/{}'.format(oss_agent.bucket_name, oss_agent.endpoint, key)
        pass
    """

    def upload_bin_file(self, key, file_stream, progress_callback=None, public_read=True):
        """
        :param key: (str) Remote file path. ex: "folder1/folder2/abc.txt"
        :param file_stream: (_io.BufferedReader) Use this code: with open('file_path', 'rb') as fs. Pass the 'fs'
        :param progress_callback: (function) A function can get progress. eq: show_progress(uploaded_bytes, total_bytes)
        :param public_read: (bool). Can everybody download this file?
        :return: (int) HTTP status. 200 means success
        """
        auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        bucket = oss2.Bucket(auth, self.endpoint, self.bucket_name)

        key = str(key)
        key.replace(':', '')
        key.replace(' ', '')

        import _io
        assert type(file_stream) is _io.BufferedReader
        result = bucket.put_object(key, file_stream, progress_callback=progress_callback)
        if result is None:
            return 0
        if result.status != 200:
            return result.status

        if public_read is True:
            bucket.put_object_acl(key, oss2.BUCKET_ACL_PUBLIC_READ)

        return result.status

    """
    Demo code:

    oss_agent = OssAgent()
    print(oss_agent.get_file_stream('story_1529638614.427114.txt').read())
    """

    def get_file_stream(self, key):
        """
        :param key: (str) Remote file path. ex: "folder1/folder2/abc.txt"
        :return: (_io.BufferedReader) file_stream. ex: print(file_stream.read())
        """
        auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        bucket = oss2.Bucket(auth, self.endpoint, self.bucket_name)

        file_stream = bucket.get_object(key)
        return file_stream

    """
    Demo code:

    oss_agent = OssAgent()
    oss_agent.download_file('story_1529638614.427114.txt', 'story.txt')
    """

    def download_file(self, key, save_path):
        """
        :param key: (str) Remote file path. ex: "folder1/folder2/abc.txt"
        :param save_path: (str) Save to local file path
        :return: None
        """
        auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        bucket = oss2.Bucket(auth, self.endpoint, self.bucket_name)

        bucket.get_object_to_file(key, save_path)
        pass

    """
    Demo code:

    oss_agent = OssAgent()
    oss_agent.delete_file('story_1529578785.4971106.txt')
    """

    def delete_file(self, key):
        """
        :param key: (str) Remote file path. ex: "folder1/folder2/abc.txt"
        :return: (int) HTTP status. 204 means valid. But delete not exist key, status still 204
        """
        auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        bucket = oss2.Bucket(auth, self.endpoint, self.bucket_name)

        result = bucket.delete_object(key)
        # print('http status: {0}'.format(result.status), type(result.status))
        # print('request_id: {0}'.format(result.request_id), type(result.request_id))
        # print('date: {0}'.format(result.headers['date']), type(result.headers['date']))
        if result is None:
            return 0
        if result.status != 200:
            return result.status

        return result.status

    pass
