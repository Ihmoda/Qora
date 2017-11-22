# Qora 
## An attempt at relicating Quora 
### Coding Dojo Hackathon



## Setup Process

1. Install Elasticsearch 5.1.1
    https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.1.1.tar.gz
2. Edit /elasticsearch-5.1.1/config/elasticsearch.yml
    Add the below lines to the yml file.
    ```
    http.cors.enabled: true
    http.cors.allow-origin: "*"
    ```
3. Activate your virtual envirnment.
4. Run 
    ```
    pip install -r requirements.txt
    ```
5. Make sure you have elasticsearch-dsl and django, if not run the below command in your virtual envirnment.
    ```
    pip install django
    pip install elasticsearch-dsl
    ```
6. Run your elasticsearch
    From your elasticsearch-5.1.1 folder
    ```
    ./bin/elasticsearch
    ```
7. If you already have data in your database you will have to add it to the elasticsearch index.
You can do this by logging into the shell and running the bulk index.
    ```
    python manage.py shell
    from apps.login_registration.search import *
    bulk_indexing()
    ```
8. Now run you application.
    ```
    python manage.py runserver
    ```

