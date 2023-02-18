# Бренный путь первого DAGa

###По мотивам практического задания из модуля 33.Airflow из курса Machine Learning Engineer платформы Skillbox

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

Многочисленные поиски по нашему уважаемому телеграмм-каналу, [мучения Dim-Dim](https://github.com/UzunDemir/airflow_hw/blob/main/33.pdf), и конечно же ознакомление с [официальной документацией airflow](https://airflow.apache.org/docs/apache-airflow/stable/start.html) я тут же пробовал для нахождения верного пути для того чтобы DAG увидел эти файлы. Необходимо также отметить поддержку вот этих ребят (@Stas_the_company и @eugix), которые подкидывали мне идеи для решения этой проблемы.
Так например, @eugix предположил, что DAG не находит пути потому что в моем - есть папки с пробелами 

(C:\Users\HP Z2\airflow_hw\dags). 

Я проверил это, НАЛИЧИЕ ПРОБЕЛА В ИМЕНИ НЕ ВЛИЯЕТ НА ПРОБЛЕМУ ПУТИ. Но все же, вы лучше придерживаетесь правил и если вы только начинаете проект, то создавайте папки и файлы без пробелов. (Мне такой user HP Z2 достался в месте с компьютером). Я по разному прописывал пути. И относительные и абсолютные - ничего не помогало. Потом просто перекинул папку data в папку dags и все заработало!

![image](https://user-images.githubusercontent.com/94790150/219742311-c568c3df-cb65-463c-8cf1-8a16b479727b.png)

![image](https://user-images.githubusercontent.com/94790150/219742493-8237fcf0-f331-4a79-996b-49e478ecfedc.png)

На всякий случай, возьмите себе на заметку, что рабочий путь в airflow всегда примерно такой 

/opt/airflow/<папкИ внутри вашего проекта!>, 

к примеру у меня был такой (это когда я их в dags поместил): /opt/airflow/dags/data/models/

Но я задался вопросом, как же все таки сделать так чтобы папка data была видна в контейнере. Как войти в контейнер (наряду с установкой airflow) вы найдете в самом задании или [здесь](https://github.com/UzunDemir/ds-intro-my-lerning/blob/main/33_Airflow/33.1%20%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20Airflow/33.1%20%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D1%8F%20%D0%BF%D0%BE%20%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5%20Airflow.pdf)

Я вошел в контейнер и попробовал там создать нужные папки:

![image](https://user-images.githubusercontent.com/94790150/219869618-b0f9d594-8a04-445e-8d56-82248c3a5d2c.png)

И вот вывод, папки можно создавать, но контейнер airflow по прежнему их не будет видеть! Еще немного размышлений и изысканий привели меня к тому, что папки можно задать в файле airflow.cfg, и это действительно так, но как открывать этот файл из контейнера я пока не нашел (если вами это известно, пожалуйста, научите и меня). И вот, после многих часов проб и ошибок меня осенило, что указание доступных папок может быть и в самом начале создания проекта airflow, то есть в файле docker-compose.yml. Действительно! Это так и есть! Открываем docker-compose.yml в блокноте 

![image](https://user-images.githubusercontent.com/94790150/219870104-2b651342-613e-4ad8-9e61-47e45e0e481b.png)

Добавляем недостающие для нашего проекта папки:

volumes:
    - ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
    
    - ${AIRFLOW_PROJ_DIR:-.}/logs:/opt/airflow/logs
    
    - ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/plugins
    
    .....
    - ${AIRFLOW_PROJ_DIR:-.}/modules:/
    
    - ${AIRFLOW_PROJ_DIR:-.}/data:/models
    
    - ${AIRFLOW_PROJ_DIR:-.}/data:/predictions
    
    .....
    
    и так далее, если есть вложенные папки, тоже их укажите
    
 Вот и все, после этого мой DAG заработал согласно тех условиям, которые были в задании, то есть структура папок проекта была сохранена! 
 
 Вот результат работы DAG:
 
 ![airflow](https://user-images.githubusercontent.com/94790150/219755070-ae14b4ed-3b57-41c7-838a-50a15c421c87.png)
