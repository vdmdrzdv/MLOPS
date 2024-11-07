import argparse
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from mlops.config import RAW_DATA_DIR, minio_url, access_key, secret_key


s3_client = boto3.client('s3',
                         endpoint_url=minio_url,
                         aws_access_key_id=access_key,
                         aws_secret_access_key=secret_key)

parser = argparse.ArgumentParser()
parser.add_argument('--bucket_name', type=str)
parser.add_argument('--object_name', type=str)
parser.add_argument('--file_path', type=str)

bucket_name = parser.parse_args().bucket_name
object_name = parser.parse_args().object_name
file_path = parser.parse_args().file_path

try:
    s3_client.download_file(bucket_name, object_name, file_path)
    print(f'Файл {object_name} успешно скачан из {bucket_name} и сохранен по пути {file_path}.')
except FileNotFoundError:
    print(f'Ошибка: путь для сохранения {RAW_DATA_DIR} не найден.')
except NoCredentialsError:
    print('Ошибка: неверные учетные данные.')
except ClientError as e:
    print(f'Ошибка при скачивании файла: {e}')
