# elasticsearch-indexer/app/indexer.py

from elasticsearch import Elasticsearch

def index_data(elasticsearch_host, elasticsearch_port, index_name, data):
    es = Elasticsearch([{'host': elasticsearch_host, 'port': elasticsearch_port}])
    
    for row in data.collect():
        doc = {
            'URL': row['URL'],
            'Country': row['Country'],
            'NumberOfClicks': row['NumberOfClicks'],
            'UniqueUsers': row['UniqueUsers'],
            'AverageTimeSpent': row['AverageTimeSpent']
        }
        res = es.index(index=index_name, body=doc)
