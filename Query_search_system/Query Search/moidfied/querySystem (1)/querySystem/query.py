import json
from flask import Flask, render_template, request
app = Flask(__name__)

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

      with open('result.json') as json_file:
         threads = json.load(json_file)
         # for t in threads:
            # print("Thread id: " + t)
            # posts = threads[t]

   return render_template("searchResults.html", threads = threads)

if __name__ == '__main__':
   app.run(debug = True)