import datetime as dt
import os
import sys

from airflow.operators.bash import BashOperator
from airflow.models import DAG
from airflow.operators.python import PythonOperator

path = os.path.expanduser('~/airflow_hw')
# Добавим путь к коду проекта в переменную окружения, чтобы он был доступен python-процессу
os.environ['PROJECT_PATH'] = path
# Добавим путь к коду проекта в $PATH, чтобы импортировать функции
print('qwqweqweqwe', os.environ['PROJECT_PATH'])
sys.path.insert(0, path)
print(sys.path.insert(0, path))
from modules.pipeline import pipeline
from modules.predict import predict
from modules.my import my
# <YOUR_IMPORTS>

args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2022, 6, 10),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(
        dag_id='car_price_prediction_1',
        schedule_interval="00 15 * * *",
        default_args=args,
) as dag:
    # просто тестирую
    first = BashOperator(
        task_id='welcome',
        bash_command='echo "welcome!"'
    )
    # тренируюсь создавать пайтон-оператор
    my = PythonOperator(
        task_id='my',
        python_callable=my,
    )

    pipeline = PythonOperator(
        task_id='pipeline',
        python_callable=pipeline,
    )
    predict = PythonOperator(
        task_id='predict',
        python_callable=predict,
    )
    # <YOUR_CODE>
    first >> my >> pipeline >> predict

