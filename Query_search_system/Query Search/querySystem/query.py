import json
from elasticsearch import Elasticsearch
import pandas as pd
import collections
from itertools import islice
from flask import Flask, render_template, request
app = Flask(__name__)

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def to_json(query):
    es = Elasticsearch()
    res = es.search(index="test_v2",  size=10, body={"query": {"match": {'Original_post': {"query": query, }}}})
    
    conversation =[]
    for doc in res['hits']['hits']:
        conversation.append(doc['_source'])
    
    df_result = pd.DataFrame(conversation)
    df_result.columns = ['id', 'post', 'tag', 'title']
    df_result = df_result.sort_values(['title', 'tag'], ascending=[True, False])
    d = collections.defaultdict(list)
    o = collections.OrderedDict()
    #print(df_result.head())
    for index, row in df_result.iterrows():
        ind = row[0]
        post = row[1]
        tag = row[2]
        title = row[3]
        
        temp = {}
        temp["id"] = ind
        temp['post'] = post
        temp['tag'] = tag
        #print(index, title,)
        d[title].append(temp)
        o[title] = True

    n_items = collections.defaultdict(list)
    for i,k in enumerate(o.keys()):
        #print(k, d[k])
        n_items[k].append(d[k])
        if i == 10:
            break
    print(n_items)
    
@app.route('/')
def search():
   return render_template('searchQuery.html')

@app.route('/searchResults', methods = ['POST', 'GET'])
def searchResults():
   if request.method == 'POST':
      result = request.form
      value = result['input']

      print("Input: " + value)
      threads = to_json(value)

   return render_template("searchResults.html", threads = threads)

if __name__ == '__main__':
   app.run(debug = True)