from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
from sqlalchemy import create_engine, text
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import csv
import datetime, time
import requests
from scipy import stats
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chains.constitutional_ai.base import ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple
from langchain.prompts import ChatPromptTemplate
from langchain.chains import APIChain
import os

# Create an instance of Flask
#app = Flask(__name__)
#app = Flask(__name__)                                                                                                  
app = Flask(__name__,template_folder ="templates")
load_dotenv()

# Set the model name for our LLMs.
GEMINI_MODEL = "gemini-1.5-flash"
GEMINI_API_KEY="AIzaSyAOda96fkiiGt0MhoNi-EJ0LnIaU0V4ZZM"

#rds_connection_string = "postgres:bootcamp@localhost:5432/satellite"
#<insert password>@localhost:5432/customer_db"

rds_connection_string = "postgres:admin@localhost:5432/satellite"
engine = create_engine(f'postgresql://{rds_connection_string}')
#engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/satellite')
llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.3)

@app.route("/")
def home():

    # @TODO: YOUR CODE HERE!
    #country = engine.connect().execute(text("select * from country"))
    #data_cat = engine.connect().execute(text("select * from satellite_category"))
    #sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    #sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
     
    country = []
    data_cat = []
    sat_ids = []
    sat_names = []
    # Return template and data
    query = 'give me two dinners to make this week one with chicken and the other vegetarian'
    response = llm.invoke(query)
    llmResponse = response.content
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("index.html", llmdata=llmResponse, query=query, category=data_cat, responsedata=responsedata, 
                           init_page="initpage", sat_ids=sat_ids, sat_names=sat_names)
    #return render_template("index.html", llmdata=llmResponse, query=query,  init_page="initpage")


@app.route("/getPostData", methods=['POST'])
def getPostData():
    query = request.form.get("Search")

    # @TODO: YOUR CODE HERE!
    #country = engine.connect().execute(text("select * from country"))
    #data_cat = engine.connect().execute(text("select * from satellite_category"))
    #sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    #sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
    country = []
    data_cat = []
    sat_ids = []
    sat_names = []
    # Return template and data
    #query = 'give me two dinners to make this week one with chicken and the other vegetarian'
    response = llm.invoke(query)
    llmResponse = response.content
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("index.html", llmdata=llmResponse, query=query, category=data_cat, responsedata=responsedata, init_page="initpage",
                            sat_ids=sat_ids, sat_names=sat_names)
    #return render_template("index.html", llmdata=llmResponse, query=query,  init_page="initpage")


@app.route("/getPrac1Form", methods=['GET'])
def getPrac1Form():
    food1 = "Chicken"
    food2 = "Vegetable"
    requirement = "kosher"
    query = {"query": f"Give me two dinners to make this week, one has to have {food1} and the other {food2}."}
    
    recipe_chain = LLMChain(llm=llm, prompt=ChatPromptTemplate.from_template("{query}"))
    
    principle = ConstitutionalPrinciple(
    name="Dietary Requirements",
    critique_request=f"The model should only offer recipes that fit a {requirement} diet.",
    revision_request=f"Modify the recipes to fit a {requirement} diet",)

    constitutional_chain = constitutional_chain = ConstitutionalChain.from_llm(
    chain=recipe_chain,
    constitutional_principles=[principle],
    llm=llm,
    verbose=True)
    result = constitutional_chain.invoke(query)
    llmResponse = result["output"]
    #print(result["output"])

    # @TODO: YOUR CODE HERE!
    #country = engine.connect().execute(text("select * from country"))
    #data_cat = engine.connect().execute(text("select * from satellite_category"))
    #sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    #sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
    country = []
    data_cat = []
    sat_ids = []
    sat_names = []
    # Return template and data
    #query = 'give me two dinners to make this week one with chicken and the other vegetarian'
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("prac1Index.html", llmdata=llmResponse, requirement=requirement,   food1=food1, food2=food2, category=data_cat, responsedata=responsedata, init_page="initpage",
                            sat_ids=sat_ids, sat_names=sat_names)
    #return render_template("index.html", llmdata=llmResponse, query=query,  init_page="initpage")

@app.route("/getPrac1PostData", methods=['POST'])
def getPrac1PostData():
    food1 = request.form.get("food1")
    food2 = request.form.get("food1")
    requirement = request.form.get("Search")
    query = {"query": f"Give me two dinners to make this week, one has to have {food1} and the other {food2}."}
    
    recipe_chain = LLMChain(llm=llm, prompt=ChatPromptTemplate.from_template("{query}"))
    
    principle = ConstitutionalPrinciple(
    name="Dietary Requirements",
    critique_request=f"The model should only offer recipes that fit a {requirement} diet.",
    revision_request=f"Modify the recipes to fit a {requirement} diet",)

    constitutional_chain = constitutional_chain = ConstitutionalChain.from_llm(
    chain=recipe_chain,
    constitutional_principles=[principle],
    llm=llm,
    verbose=True)
    result = constitutional_chain.invoke(query)
    llmResponse = result["output"]
    #print(result["output"])

    # @TODO: YOUR CODE HERE!
    #country = engine.connect().execute(text("select * from country"))
    #data_cat = engine.connect().execute(text("select * from satellite_category"))
    #sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    #sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
    country = []
    data_cat = []
    sat_ids = []
    sat_names = []
    # Return template and data
    #query = 'give me two dinners to make this week one with chicken and the other vegetarian'

    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("prac1Index.html", llmdata=llmResponse, requirement=requirement,   food1=food1, food2=food2, category=data_cat, responsedata=responsedata, init_page="initpage",
                            sat_ids=sat_ids, sat_names=sat_names)
    #return render_template("index.html", llmdata=llmResponse, query=query,  init_page="initpage")



@app.route("/getOpenApiForm", methods=['GET'])
def getOpenApiForm():


    #print(result["output"])

    # @TODO: YOUR CODE HERE!
    #country = engine.connect().execute(text("select * from country"))
    #data_cat = engine.connect().execute(text("select * from satellite_category"))
    #sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    #sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
    country = []
    data_cat = []
    sat_ids = []
    sat_names = []
    # Return template and data
    #query = 'give me two dinners to make this week one with chicken and the other vegetarian'
    resdata = [{}]
    querydata = [{}]
    responsedata = { }
    return render_template("openApiIndex.html", responsedata=responsedata, init_page="initpage")

@app.route("/getOpenApiPostData", methods=['POST'])
def getOpenApiPostData():
    question = request.form.get("question")
    querydatas = [{}]
    #print(result["output"])

    # @TODO: YOUR CODE HERE!
    #country = engine.connect().execute(text("select * from country"))
    #data_cat = engine.connect().execute(text("select * from satellite_category"))
    #sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    #sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
    country = []
    data_cat = []
    sat_ids = []
    sat_names = []
    spec_str = """Open Library provides an experimental API to search. 
    WARNING: This API is under active development and may change in future.
    Overview & Features
    The Open Library Search API is one of the most convenient and complete ways to retrieve book data on Open Library. The API:
    Is able to return data for multiple books in a single request/response
    Returns both Work level information about the book, as well as Edition level information (such as)
    Author IDs are returned which you can use to fetch the author's image, if available
    Options are available to return Book Availability along with the response.
    Powerful sorting options are available, such as star ratings, publication date, and number of editions.
    Endpoint
    The endpoint for this API is:
    https://openlibrary.org/search.json
    Examples
    The URL format for API is simple. Take the search URL and add .json to the end. Eg:
    https://openlibrary.org/search.json?q=the+lord+of+the+rings
    https://openlibrary.org/search.json?title=the+lord+of+the+rings
    https://openlibrary.org/search.json?author=tolkien&sort=new
    https://openlibrary.org/search.json?q=the+lord+of+the+rings&page=2
    https://openlibrary.org/search/authors.json?q=twain
    Using Thing IDs to get Images
    You can use the olid (Open Library ID) for authors and books to fetch covers by olid, e.g.:
    https://covers.openlibrary.org/a/olid/OL23919A-M.jpg
    URL Parameters
    Parameter	Description
    q	The solr query. See Search HowTo for sample queries
    fields	The fields to get back from solr. Use the special value * to get all fields (although be prepared for a very large response!).
    To fetch availability data from archive.org, add the special value, availability. Example: /search.json?q=harry%20potter&fields=*,availability&limit=1. This will fetch the availability data of the first item in the `ia` field.
    sort	You can sort the results by various facets such as new, old, random, or key (which sorts as a string, not as the number stored in the string). For a complete list of sorts facets look here (this link goes to a specific commit, be sure to look at the latest one for changes). The default is to sort by relevance.
    lang	The users language as a two letter (ISO 639-1) language code. This influences but doesn't exclude search results. For example setting this to fr will prefer/display the French edition of a given work, but will still match works that don't have French editions. Adding language:fre on the other hand to the search query will exclude results that don't have a French edition.
    offset / limit	Use for pagination.
    page / limit	Use for pagination, with limit corresponding to the page size. Note page starts at 1.
    Include no other text, only the API call URL. Don't use newlines."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    # Return template and data
    #query = 'give me two dinners to make this week one with chicken and the other vegetarian'

    resdata = [{
    }
    ]
    query = {"question": question}
    response = chain.invoke(query)
    answer = response["output"]
    querydata = {'question': question,
             'answer': answer}
    resdata.append(querydata)
    
    responsedata = { 'respdata': resdata
    }
   
    return render_template("openApiIndex.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    #return render_template("index.html", llmdata=llmResponse, query=query,  init_page="initpage")



@app.route("/getSatellite/<cntry>/<numSat>")
def satellite_country(cntry,numSat):

    # @TODO: YOUR CODE HERE!
    #sat_cnt_cnt = engine.connect().execute(text("select * from country_satellite where country_code='"+cntry+"'"))
    #country = engine.connect().execute(text("select * from country "))
    #data_cat = engine.connect().execute(text("select * from satellite_category"))
    #sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    #sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
    sat_cnt_cnt = []
    country = []
    data_cat = []
    sat_ids = []
    sat_names = []
    # Return template and data

    incrd =0
    coordinatesjson = {}
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }

    incdata = 0
    
    for record in sat_cnt_cnt:
        coordinatesjson = {}
        if (incrd >int(numSat)):
            break
        try: 
            url = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(record['satellite_id'])+"/41.702/-76.014/0/2/&apiKey=J3H9EJ-Z2GE6Y-BC2E6G-4LOF"
            response = requests.get(url).json()            
            tt = time.strftime("%D %H:%M", time.localtime(int(response['positions'][0]['timestamp'])))
            tt2 = time.strftime("%D %H:%M", time.localtime(int(response['positions'][1]['timestamp'])))
       
            coordinatesjson['latitude'] = response['positions'][1]['satlatitude']            
            coordinatesjson['longitude'] = response['positions'][1]['satlongitude']                      
            coordinatesjson['azimuth'] = response['positions'][1]['azimuth']            
            coordinatesjson['elevation'] = response['positions'][1]['elevation']            
            coordinatesjson['altitude'] = response['positions'][1]['sataltitude']            
            coordinatesjson['satname'] = response['info']['satname']            
            coordinatesjson['satid'] = response['info']['satid'] 
            coordinatesjson['datetime'] = tt2  
            resdata.append(coordinatesjson)
            incrd = incrd+1
            incdata = incdata+1
        except:
            pass

        responsedata['respdata'] = resdata
    

    # Build partial query URL
   
    return render_template("index.html", country=country, category=data_cat, sat_country=sat_cnt_cnt,responsedata=responsedata,
     init_page="notinitpage" , sat_ids=sat_ids, sat_names=sat_names, sel_cnt=cntry)

@app.route("/getSatelliteById/<satid>/<numSat>")
def satellite_byid(satid,numSat):

    # @TODO: YOUR CODE HERE!
    sat_cnt_cnt = engine.connect().execute(text("select * from country_satellite where satellite_id='"+satid+"'"))
    country = engine.connect().execute(text("select * from country "))
    data_cat = engine.connect().execute(text("select * from satellite_category"))
    sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
    # Return template and data

    incrd =0
    coordinatesjson = {}
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }

    incdata = 0
    
    for record in sat_cnt_cnt:
        coordinatesjson = {}
        if (incrd >int(numSat)):
            break
        try: 
            url = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(record['satellite_id'])+"/41.702/-76.014/0/2/&apiKey=J3H9EJ-Z2GE6Y-BC2E6G-4LOF"
            response = requests.get(url).json()            
            
            tt = time.strftime("%D %H:%M", time.localtime(int(response['positions'][0]['timestamp'])))
            tt2 = time.strftime("%D %H:%M", time.localtime(int(response['positions'][1]['timestamp'])))
        
            coordinatesjson['latitude'] = response['positions'][1]['satlatitude']            
            coordinatesjson['longitude'] = response['positions'][1]['satlongitude']                      
            coordinatesjson['azimuth'] = response['positions'][1]['azimuth']            
            coordinatesjson['elevation'] = response['positions'][1]['elevation']            
            coordinatesjson['altitude'] = response['positions'][1]['sataltitude']            
            coordinatesjson['satname'] = response['info']['satname']            
            coordinatesjson['satid'] = response['info']['satid'] 
            coordinatesjson['datetime'] = tt2  
            resdata.append(coordinatesjson)
            incrd = incrd+1
            incdata = incdata+1

        except:
            pass

        responsedata['respdata'] = resdata
    

    # Build partial query URL
   
    return render_template("index.html", country=country, category=data_cat, sat_country=sat_cnt_cnt,responsedata=responsedata,  
    init_page="notinitpage" , sat_ids=sat_ids, sat_names=sat_names, sat_sel_id=satid)

@app.route("/getSatelliteByName/<satName>/<numSat>")
def satellite_byname(satName,numSat):

    # @TODO: YOUR CODE HERE!
    sat_cnt_cnt = engine.connect().execute(text("select * from country_satellite where satellite_name='"+satName+"'"))
    country = engine.connect().execute(text("select * from country "))
    data_cat = engine.connect().execute(text("select * from satellite_category"))
    sat_ids = engine.connect().execute(text("select satellite_id from country_satellite order by 1"))
    sat_names = engine.connect().execute(text("select satellite_name from country_satellite order by 1"))
    # Return template and data

    incrd =0
    coordinatesjson = {}
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }

    incdata = 0
    
    for record in sat_cnt_cnt:
        coordinatesjson = {}
        if (incrd >int(numSat)):
            break
        try: 
            url = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(record['satellite_id'])+"/41.702/-76.014/0/2/&apiKey=J3H9EJ-Z2GE6Y-BC2E6G-4LOF"
            response = requests.get(url).json()            
         
            tt = time.strftime("%D %H:%M", time.localtime(int(response['positions'][0]['timestamp'])))
            tt2 = time.strftime("%D %H:%M", time.localtime(int(response['positions'][1]['timestamp'])))
          
            coordinatesjson['latitude'] = response['positions'][1]['satlatitude']            
            coordinatesjson['longitude'] = response['positions'][1]['satlongitude']                      
            coordinatesjson['azimuth'] = response['positions'][1]['azimuth']            
            coordinatesjson['elevation'] = response['positions'][1]['elevation']            
            coordinatesjson['altitude'] = response['positions'][1]['sataltitude']            
            coordinatesjson['satname'] = response['info']['satname']            
            coordinatesjson['satid'] = response['info']['satid'] 
            coordinatesjson['datetime'] = tt2  
            resdata.append(coordinatesjson)
            incrd = incrd+1
            incdata = incdata+1
        except:
            pass

        responsedata['respdata'] = resdata
    

    # Build partial query URL
   
    return render_template("index.html", country=country, category=data_cat, sat_country=sat_cnt_cnt,responsedata=responsedata,
      init_page="notinitpage", sat_ids=sat_ids, sat_names=sat_names,sel_name=satName)


# Route to render index.html template using data from Mongo
@app.route("/indexplots")
def indexplots():

    # Build partial query URL
   
    return render_template("index_plots.html")


@app.route("/minimapindex")
def minimapindex():

    # Build partial query URL
   
    return render_template("minimap_index.html")


@app.route("/satglobe")
def satglobe():

    # Build partial query URL
   
    return render_template("satGlobe.html")


@app.route("/cluster")
def cluster():

    # Build partial query URL
   
    return render_template("cluster.html")

if __name__ == "__main__":
    app.run(debug=True)
    
