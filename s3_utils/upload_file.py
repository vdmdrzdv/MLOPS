import argparse
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from mlops.config import minio_url, access_key, secret_key

s3_client = boto3.client('s3',
                         endpoint_url=minio_url,
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key)

parser = argparse.ArgumentParser()
parser.add_argument('--bucket_name', type=str)
parser.add_argument('--file_path', type=str)
parser.add_argument('--object_name', type=str)

bucket_name = parser.parse_args().bucket_name
file_path = parser.parse_args().file_path
object_name = parser.parse_args().object_name

try:
    s3_client.head_bucket(Bucket=bucket_name)
except ClientError as e:
    if e.response['Error']['Code'] == '404':
        s3_client.create_bucket(Bucket=bucket_name)
        print(f'Бакет {bucket_name} был создан.')
    else:
        print(f'Ошибка при проверке бакета: {e}')

try:
    s3_client.upload_file(file_path, bucket_name, object_name)
    print(f'Файл {file_path} успешно загружен в {bucket_name}/{object_name}')
except FileNotFoundError:
    print(f'Файл {file_path} не найден.')
except NoCredentialsError:
    print('Ошибка: неверные учетные данные.')
except Exception as e:
    print(f'Произошла ошибка: {e}')
