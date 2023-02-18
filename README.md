# airflow_hw
Airflow home work from Skillbox ds-intro volum 33

Изучая видеоурок по модулю "33.Airflow" от Skillbox, термин DAG вызвал у меня улыбку. "Да уж, даги нынче не те" - подумал я про себя, вспоминая уроженцев Дагестана, которым я, пользуясь случаем передаю пламенный "СЕЛЯМ!". 

Однако, на деле все оказалось не так уж и весело. Решение этой задачи по развертыванию проекта airflow отняло у меня очень много времени и нервов.

Вначале все было очень даже неплохо. Несмотря на многочисленные предупреждения коллег в телеграмм-канале курса, что учебные модули 31-33 очень тяжелые, мне удалось прямо таки с ходу сделать 31 и 32 практические задания. Подумалось, что точно также я преодолею и 33 модуль. Обучающий материал я просмотрел и с успехом установил Docker и запустил первый учебный контейнер. Дальше я приступил к выполнению практической работы.

Итак, я скачал и распаковал архив airflow_hw. Папку __MACOSX можно смело удалить, она вам не понадобится, так как является визиткой, что этот архив был создан на MAC.
Дополнить файлы pipeline.py и predict.py в Pycharm я смог достаточно быстро, получив небольшую корректировку от своего куратора. И вот уже у меня обучается модель, записывается и определяются предикты по всем тестовым данным, которые также записываются в папку. Оставалось, то же самое повторить в airflow. 

Я как обычно запустил контейнер в Docker:

![image](https://user-images.githubusercontent.com/94790150/219742019-e9ea88b4-0519-4d85-b501-8187d9156532.png)

С первого раза конечно же DAG не появился:

![image](https://user-images.githubusercontent.com/94790150/219866554-e1267cdf-9990-44ff-a586-7a699cae9bbc.png)

Но воспользовавшись советом, который разместил коллега Dim-Dim 

![image](https://user-images.githubusercontent.com/94790150/219868312-06546064-1bb0-40d0-97fe-c4361974b06a.png)

я просто перенес папку modules с рабочими файлами в папку проекта \airflow_hw\dags и тогда мой DAG без проблем обнаружил себя в Airflow! Как вы видите, в процессе изучения я еще добавил парочку своих шагов: my, welcome. Не обращайте на них внимания.

![image](https://user-images.githubusercontent.com/94790150/219741460-6ce73252-e556-42fd-937f-a63d2385e39a.png)

Это конечно же нарушало условия задачи, стпуктура проекта должна была быть такой:

![image](https://user-images.githubusercontent.com/94790150/219867488-70cfe528-e74a-4493-97f3-4520fc8b583e.png)

но поверьте, это не такая срашная проблема, позже я вам покажу как добавить в контейнер папки, которые он будет видеть. Большую проблему для меня  доставил вопрос указания верного пути, для того, чтобы заработали файлы pipeline.py и predict.py. А пока, мой DAG упорно не запускался и выдавал такую ошибку:

FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/HP Z2/airflow_hw/data/train/homework.csv'

Вот борьба с этой ошибкой заняла больше всего времени!

Многочисленные поиски по нашему уважаемому телеграмм-каналу, мучения Dim-Dim, и конечно же ознакомление с [официальной документацией airflow](https://airflow.apache.org/docs/apache-airflow/stable/start.html) я тут же пробовал для нахождения верного пути для того чтобы DAG увидел эти файлы.


Но при его запуске выскочила ошибка:

![image](https://user-images.githubusercontent.com/94790150/219867310-99fde76d-4944-4ac0-839f-9e70c79cae74.png)


![image](https://user-images.githubusercontent.com/94790150/219742311-c568c3df-cb65-463c-8cf1-8a16b479727b.png)

![image](https://user-images.githubusercontent.com/94790150/219742493-8237fcf0-f331-4a79-996b-49e478ecfedc.png)


![airflow](https://user-images.githubusercontent.com/94790150/219755070-ae14b4ed-3b57-41c7-838a-50a15c421c87.png)
