from elasticsearch_dsl.connections import connections 
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk 
from elasticsearch import Elasticsearch 
from .models import *
from ..login_registration.models import *
import models
connections.create_connection()#connects to elastic server

class QuestionIndex(DocType):
    content = Text()
    class Meta:
        index = 'question-index'

# class BlogPostIndex(DocType):
#     author = Text()
#     posted_date = Date()
#     title = Text()
#     text = Text()
#     class Meta:
#         index = 'blogpost-index'

def bulk_indexing():
    # BlogPostIndex.init()
    QuestionIndex.init()
    es = Elasticsearch()
    #bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))
    bulk(client=es, actions=(b.indexing() for b in models.Question.objects.all().iterator()))

#def search(author):
def search(content):
    s = Search().filter('term', content=content) 
    response = s.execute()
    return response