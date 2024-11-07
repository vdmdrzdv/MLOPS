#!/bin/bash

if command -v python &> /dev/null; then
    PYTHON_COMMAND="python"
elif command -v python3 &> /dev/null; then
    PYTHON_COMMAND="python3"
else
    echo "Python не установлен"
    exit 1
fi

$PYTHON_COMMAND s3_utils/download_file.py --bucket_name data --object_name weight_change_dataset.csv --file_path data/raw/weight_change_dataset.csv
$PYTHON_COMMAND mlops/features.py --input_file data/raw/weight_change_dataset.csv --output_file data/processed/preprocessed_weight_change_dataset.csv
$PYTHON_COMMAND s3_utils/upload_file.py --bucket_name data --file_path data/processed/preprocessed_weight_change_dataset.csv --object_name preprocessed_weight_change_dataset.csv
