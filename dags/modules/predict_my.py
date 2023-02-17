# <YOUR_IMPORTS>
import dill
import pandas as pd
import glob
import json

def predict():
    # <YOUR_CODE>
    path = '/airflow_hw' # 'это путь до папки проекта
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
            data = pd.DataFrame.from_dict([dict(json.load(fin))])
            #df = pd.DataFrame.from_dict([form])
            print(data)
            #pred = model.predict(df)
            #x = {'car_id': df.id, 'pred': pred}
            #y = model.predict(df)[0]

if __name__ == '__main__':
    predict()