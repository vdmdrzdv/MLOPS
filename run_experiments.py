import argparse
import os
import subprocess


def run_experiment(config_folder: str,
                   config_file: str,
                   dataset_path: str,
                   dataset_file: str) -> None:
    command = [
        'docker', 'run',
        '--rm',
        '-v', f"{os.getcwd()}/{config_folder}:/configs",
        '-v', f"{os.getcwd()}/{dataset_path}:/data",
        '--env-file', '.container_env',
        'weights-prediction',
        'python', 'train.py',
        '--config', f'/configs/{config_file}',
        '--dataset', f'/data/processed/{dataset_file}'
    ]

    subprocess.run(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_folder', type=str, required=True,
                        help='Path to the config file.')
    args = parser.parse_args()

    config_folder = args.config_folder
    dataset_path = 'data'
    dataset_file = 'preprocessed_weight_change_dataset.csv'

    config_files = [f for f in os.listdir(config_folder) if f.endswith('.json')]

    for config_file in config_files:
        run_experiment(config_folder, config_file, dataset_path, dataset_file)
