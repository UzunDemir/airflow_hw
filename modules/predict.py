# <YOUR_IMPORTS>
import pandas as pd
import dill
import json
import glob
import os
from pathlib import Path

def predict():
    # <YOUR_CODE>
    path = os.path.expanduser('~/airflow_hw') # 'это путь до папки проекта
    # ...дальше путь внутри папки до модели
    with open(f'{path}/data/models/cars_pipe_202302151818.pkl', 'rb') as file:
        model = dill.load(file)
    df_pred = pd.DataFrame(columns=['car_id', 'pred'])
    print('ok')
    # готовим путь до файлов для теста
    path_files = path + '/data/test/*json'
    # перебираем тестовые файлы из путей файлов
    for json_files_path in glob.iglob(path_files):
        with open(json_files_path) as fin:
            form = json.load(fin)
            print(form)
            df = pd.DataFrame.from_dict([form])
            print(df)
            pred = model.predict(df)
            #x = {'car_id': df.id, 'pred': pred}
            #y = model.predict(df)

if __name__ == '__main__':
    predict()
