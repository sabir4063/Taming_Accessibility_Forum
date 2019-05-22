# Taming_Accessibility_Forum

The instructions is given for the Jaws Forum:

CLASSIFICATION

Go to "Final Code for the Classification":

1. First run the Data Pre-processing. It will remove all the quote and author name.
2. Run the Data Processing for the Classifier, it will generate all the features.
3. Run the Classifier for the Help, it will generate several classifier to detect the "Help" related posts.
4. Run the Classifier for the Answer, it will generate several classifier to detect the "Answer" related posts.

ELASTICSEARCH INDEXING

GO to "Elasticsearch Indexing":

First run "Elasticsearch". I used elasticsearch-6.7.0 version.

1. Run CSV to JSON, it will convert .csv file to .json for the indexing
2. Run Index Data to Elsticsearch, it will index the previous .json to Elasticsearch.


WEB INTERFACE:

Go to "Query Search Engine - JAWS":

First run "Flask" web framework.

1. Go to "templates" folder and run.
2. It will run the web interface in the browser. 
3. Now you can perform the query search.
