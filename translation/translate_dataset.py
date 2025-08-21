import warnings
# set warnings to ignore
warnings.filterwarnings('ignore')

import pandas as pd
import traceback
import argparse
import joblib

import time
from tqdm.auto import tqdm

from marian_translator import en2esp_marian
pipeline_steps = [
    en2esp_marian
]

num_threads = joblib.cpu_count()


def pipeline_singlecore(df, step, column_name='text'):
    try:
        new_column_name = f'{column_name}_{step.__name__}'
        tqdm.pandas(desc=f'applying {step}:')
        df[new_column_name] = df[column_name].progress_apply(step)

        return df
    except(Exception) as e:
        print(traceback.format_exc())


def pipeline_multicore(df, step, column_name='text'):
    try:
        new_column_name = f'{column_name}_{step.__name__}'

        # Utilizar todos los hilos disponibles en tu CPU
        tqdm.pandas(desc=f'applying {step}:')
        df[new_column_name] = joblib.Parallel(n_jobs=num_threads)(
            joblib.delayed(step)(str(row[column_name])) for _, row in
            tqdm(df.iterrows(), total=len(df), desc=f'Processing rows by {step}:')
        )

        return df
    except Exception as e:
        print(traceback.format_exc())


if __name__ == '__main__':
    try:

        start_time = time.time()

        parser = argparse.ArgumentParser(description='Example of argument handling')

        # Agregar los argumentos
        parser.add_argument('--column', help='Column name', default='text')
        parser.add_argument('--input', help='File name input')
        parser.add_argument('--output', help='File name output')

        # Analizar los argumentos de la línea de comandos
        args = parser.parse_args()

        # Acceder a los valores de los argumentos
        column_name = args.column
        file_input = args.input
        file_output = args.output

        for step in pipeline_steps:
            df = pd.read_csv(file_input, sep=',', header=0)
            df = pipeline_multicore(df, step, column_name)
            df.to_csv(file_output, sep=',', header=True, index=False)

        end_time = time.time()

    except(Exception) as e:
        print(traceback.format_exc())
