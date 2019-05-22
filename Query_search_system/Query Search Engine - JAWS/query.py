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
    res = es.search(index="test_v3", size=5000, body={"query": {"match": {'Original_post': {"query": query}}}})
    
    conversation =[]
    for doc in res['hits']['hits']:
        conversation.append(doc['_source'])
    
    df_result = pd.DataFrame(conversation)
    #df_result.columns = ['id', 'post', 'tag', 'title']
    #df_result = df_result.sort_values(['title', 'tag'], ascending=[True, False])
    d = collections.defaultdict(list)
    o = o = collections.OrderedDict()
    for index, row in df_result.iterrows():
        ind = row[0]
        post = row[1]
        tag = row[2]
        title = row[3]

        temp = {}
        temp["id"] = ind
        temp['post'] = post
        temp['tag'] = tag
    
        d[title].append(temp)
        o[title] = True
            
    n_items = collections.defaultdict(list)
    for k in o.keys():
        n_items[k] = d[k]
        if len(n_items) == 21:
            break
        
    return n_items
    
@app.route('/')
def search():
   return render_template('searchQuery.html')

@app.route('/searchResults', methods = ['POST', 'GET'])
def searchResults():
   if request.method == 'POST':
      result = request.form
      value = result['input']
      print("Input: " + value)

      # Use input and get results in json file
      # ADD YOUR CODE HERE

      #with open('result.json') as json_file:
      #   threads = json.load(json_file)
         # for t in threads:
            # print("Thread id: " + t)
            # posts = threads[t]
      threads = to_json(value)
      
   return render_template("searchResults.html", threads = threads)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5001, debug=True)