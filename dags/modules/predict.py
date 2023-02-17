# <YOUR_IMPORTS>
import dill  # библиотека для распаковки модели
import pandas as pd
import glob
import json
import os
import datetime
from datetime import datetime


def predict():
    path = os.path.expanduser('~/airflow_hw')  # 'это путь до папки проекта
    # ...дальше путь внутри папки до модели
    with open('/opt/airflow/dags/data/models/cars_pipe_202302171710.pkl', 'rb') as file:
        model = dill.load(file)

    predicted_df = pd.DataFrame(columns=['id', 'predict'])  # приготовим пустой датафрейм
    print('predicted_df -', predicted_df)
#############################################################
    def prediction(data_path):
        with open(data_path, 'r') as f: # откроем файл на чтение как f
            data = pd.DataFrame.from_dict([dict(json.load(f))]) # извлечем данные из файла в виде словаря в датафрейм
            print(data)
            y = model.predict(data)[0] # найдем прогноз для этого датафрейма
            predicted_df.loc[len(predicted_df.index)] = [int(data.id), y] # занесем в подготовленный датафрейм результат
#############################################################
    for file_name in os.listdir('/opt/airflow/dags/data/test'):  # для файлов в папке test
        prediction(f'/opt/airflow/dags/data/test/' + file_name)  # выполним функцию prediction для каждого файла
    # по окончании перебора всех данных для тестирования сохраним датафрейм в файл csv
    predicted_df.to_csv(f'/opt/airflow/dags/data/predictions/predictions_{datetime.now().strftime("%Y%m%d%H%M")}.csv')


if __name__ == '__main__':
    predict()
