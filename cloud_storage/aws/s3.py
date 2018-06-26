# coding: utf-8

import boto3
import traceback

from .log import log_info, log_warning, log_error

s3_client = boto3.client('s3')


def list_buckets():
    buckets = list()
    try:
        s3_resp = s3_client.list_buckets()
        if s3_resp is not None:
            for dic in s3_resp['Buckets']:
                buckets.append(dic['Name'])
        pass
    except:
        log_error(traceback.format_exc())
        pass
    return buckets


def put_object(bucket_name, local_file_path, remote_folder_path, remote_file_name, bucket_location,
               local_file_is_binary=True, use_s3_accelerate=False):
    """
    :param bucket_name: (string) The bucket name ex: 'example.bucket.name'

    :param local_file_path: (string) Local file full path. ex: '/home/miflydesign/temp/lena_is_pretty.jpg'

    :param remote_folder_path: (string) Remote folder path at S3. ex: 'pretty-girl-collection/age-18-28'
                                        ps: folder will auto created if it was not existed.

    :param remote_file_name: (string) Remote file name at S3. ex: 'lena.jpg'
                                      The file at S3 will looks like:
                                      example.bucket.name/pretty-girl-collection/age-18-28/lena.jpg    

    :param bucket_location: (string) Where is the S3 bucket at. It is a part of the return URL.
                                 ex: 'ap-southeast-1'
                                 Valid Values: [ us-west-1 | us-west-2 | ca-central-1 | EU or eu-west-1 | eu-west-2 | eu-central-1 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ap-northeast-1 | ap-northeast-2 | sa-east-1 | empty string (for the US East (N. Virginia) region) | us-east-2]
    
    :param local_file_is_binary: (bool) How to tread the local file. If True, open file with 'rb', else: 'r'
    
    :param use_s3_accelerate: (bool) If the bucket has enable S3-Accelerate, set the flag True,
                                     you will get the file accelerate URL.

    :return: (string) The public download-able URL
    """

    object_url = ''
    try:
        remote_folder_path = remote_folder_path.strip('/')
        remote_file_name = remote_file_name.strip('/')
        remote_key = remote_folder_path + '/' + remote_file_name

        if local_file_is_binary is True:
            open_file_mode = 'rb'
        else:
            open_file_mode = 'r'

        put_success = False

        with open(local_file_path, open_file_mode) as file_handler:
            s3_resp = s3_client.put_object(
                Bucket=bucket_name,
                Key=remote_key,
                Body=file_handler.read(),
                ACL='public-read'
            )
            log_info('put_object() s3_resp: {}'.format(s3_resp))

            if s3_resp is not None:
                if s3_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
                    put_success = True
                pass
            pass

        if put_success:
            if use_s3_accelerate is True:
                object_url = "https://{}.s3-accelerate.amazonaws.com/{}".format(
                    bucket_name,
                    remote_key
                )
            else:
                object_url = "https://s3-{}.amazonaws.com/{}/{}".format(
                    bucket_location,
                    bucket_name,
                    remote_key
                )
        else:
            object_url = ''
        pass
    except:
        log_error(traceback.format_exc())
        pass

    return object_url


def delete_object(bucket_name, remote_file_path):
    """
    :param bucket_name: The bucket name.
    :param remote_file_path: The file path at the bucket. ex: pretty-girl-collection/age-18-28/lena.jpg
    :return: None  # TODO: figure out how to know delete object is success or failed.
    """

    try:
        s3_resp = s3_client.delete_object(
            Bucket=bucket_name,
            Key=remote_file_path
        )
        log_info('delete_object() s3_resp: {}'.format(s3_resp))
        pass
    except:
        log_error(traceback.format_exc())
        pass
    pass


def delete_object_via_url(url, bucket_name, bucket_location):
    """
    :param url: The original S3 download-able URL.
    :param bucket_name: The bucket name.
    :param bucket_location: The bucket location at. ex: 'ap-southeast-1'
    :return: None
    """
    delete_key = url.replace('https://s3-{}.amazonaws.com/{}'.format(bucket_location, bucket_name), '')
    delete_key = delete_key.strip('/')

    delete_object(bucket_name, delete_key)
    pass


def delete_object_via_accelerate_url(url, bucket_name):
    """    
    :param url: The original S3 accelerate download-able URL.
    :param bucket_name: The bucket name.
    :return: None 
    """
    delete_key = url.replace('https://{}.s3-accelerate.amazonaws.com/'.format(bucket_name), '')

    delete_object(bucket_name, delete_key)
    pass
