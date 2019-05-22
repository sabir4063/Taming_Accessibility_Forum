
# coding: utf-8

# In[13]:


from elasticsearch import Elasticsearch
from datetime import datetime
es = Elasticsearch()

class tutorial:
    # create an instance of elasticsearch and assign it to port 9200
    ES_HOST = {"host": "localhost", "port": 9200}
    es = Elasticsearch(hosts=[ES_HOST])


#     def create_index(index_name):
#         """Functionality to create index."""
#         resp = es.indices.create(index=index_name)
#         print(resp)

    def create_index(index_name):
        """Functionality to create index."""
        resp = es.indices.create(
                index=index_name,
                body={
                  'settings': {
                    # just one shard, no replicas for testing
                    'number_of_shards': 1,
                    'number_of_replicas': 0,

                    # custom analyzer for analyzing file paths
                    'analysis': {
                      'analyzer': {
                        'file_path': {
                          'type': 'custom',
                          'tokenizer': 'path_hierarchy',
                          'filter': ['lowercase']
                        }
                      }
                    }
                  }
                },
                # Will ignore 400 errors, remove to ensure you're prompted
                ignore=400
            )


    def document_add(index_name, doc_type, doc, doc_id=None):
        """Funtion to add a document by providing index_name,
        document type, document contents as doc and document id."""
        resp = es.index(index=index_name, doc_type=doc_type, body=doc, id=doc_id)
        #print(resp)


    def document_view(index_name, doc_type, doc_id):
        """Function to view document."""
        resp = es.get(index=index_name, doc_type=doc_type, id=doc_id)
        document = resp["_source"]['Post']
        print(document)


    def document_update(index_name, doc_type, doc_id, doc=None, new=None):
        """Function to edit a document either updating existing fields or adding a new field."""
        if doc:
            resp = es.index(index=index_name, doc_type=doc_type,
                            id=doc_id, body=doc)
            print(resp)
        else:
            resp = es.update(index=index_name, doc_type=doc_type,
                             id=doc_id, body={"doc": new})


    def document_delete(index_name, doc_type, doc_id):
        """Function to delete a specific document."""
        resp = es.delete(index=index_name, doc_type=doc_type, id=doc_id)
        print(resp)


    def delete_index(index_name):
        """Delete an index by specifying the index name"""
        resp = es.indices.delete(index=index_name)
        print(resp)


# In[ ]:


resp = es.indices.delete(index='test_v3')
print(resp)


# In[17]:


tutorial.create_index('test_v3')


# In[18]:


import csv
import json

with open('../FInal Version Code/Data/jaws_to_es.json') as json_file:  
    data = json.load(json_file)
    for p in data:
        tutorial.document_add('test_v3', 'jaws', p)


# In[14]:


resp = es.indices.delete(index='test_v2')
print(resp)


# In[15]:


tutorial.create_index('test_v2')


# In[16]:


import csv
import json

with open('../FInal Version Code/Data/to_es_v2.json') as json_file:  
    data = json.load(json_file)
    for p in data:
        tutorial.document_add('test_v2', 'nvda', p)

