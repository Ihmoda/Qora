from elasticsearch_dsl.connections import connections 
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk 
from elasticsearch import Elasticsearch 
from .models import *
from ..login_registration.models import *
import models
connections.create_connection()#connects to elastic server
class BlogPostIndex(DocType):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()
    class Meta:
        index = 'blogpost-index'
def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))
def search(author):
    s = Search().filter('term', author=author) 
    response = s.execute()
    return response