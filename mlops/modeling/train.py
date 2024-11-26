import os
from typing import Union
import boto3
import pandas as pd
import mlflow
import mlflow.sklearn
import json
import argparse
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from botocore.exceptions import ClientError

json_type = dict[str, Union[str, int]]


def load_config(config_path: str) -> json_type:
    with open(config_path, 'r') as file:
        config: json_type = json.load(file)
    return config


def load_dataset(dataset_path: str) -> pd.DataFrame:
    return pd.read_csv(dataset_path)


def train_model(X_train: pd.DataFrame,
                y_train: pd.Series,
                config: json_type) -> RandomForestRegressor:
    model = RandomForestRegressor(**config)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model: RandomForestRegressor,
                   X_test: pd.DataFrame,
                   y_test: pd.Series
                   ) -> tuple[float, float]:
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return mse, r2


def main(config_path: str, dataset_path: str) -> None:
    minio_url = os.getenv('MLFLOW_S3_ENDPOINT_URL')
    access_key = os.getenv('AWS_ACCESS_KEY_ID')
    secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    s3_client = boto3.client('s3',
                             endpoint_url=minio_url,
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key)
    bucket = os.environ.get('BUCKET')
    try:
        s3_client.head_bucket(Bucket=bucket)
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            s3_client.create_bucket(Bucket=bucket)
            print(f'Бакет {bucket} был создан.')
        else:
            print(f'Ошибка при проверке бакета: {e}')

    config = load_config(config_path)
    data = load_dataset(dataset_path)

    X = data.drop('Final Weight (lbs)', axis=1)
    y = data['Final Weight (lbs)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=228)
    mlflow.set_experiment(bucket)
    run_name = config_path.split('/')[-1]
    with mlflow.start_run(run_name=run_name):
        model = train_model(X_train, y_train, config)

        mse, r2 = evaluate_model(model, X_test, y_test)
        print(f"Mean Squared Error: {mse}")
        print(f"R^2 Score: {r2}")

        mlflow.log_params(config)
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)

        input_example = X_test.iloc[0:1]
        mlflow.sklearn.log_model(model, run_name, input_example=input_example)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train a model to predict future weight.')
    parser.add_argument('--config', type=str, required=True, help='Path to the config file.')
    parser.add_argument('--dataset', type=str, required=True, help='Path to the dataset file.')

    args = parser.parse_args()
    main(args.config, args.dataset)
