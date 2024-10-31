from flask import Flask, render_template, redirect, request
import time
import requests
import json
from scipy import stats
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chains.constitutional_ai.base import ConstitutionalChain
from langchain.chains.constitutional_ai.models import ConstitutionalPrinciple
from langchain.prompts import ChatPromptTemplate,FewShotPromptTemplate,PromptTemplate
from langchain.chains import APIChain
import os
from langchain.document_loaders import PyPDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import WikipediaLoader

                                                                                          
app = Flask(__name__,template_folder ="templates")
load_dotenv()

# Set the model name for our LLMs.
GEMINI_MODEL = "gemini-1.5-flash"
GEMINI_API_KEY="AIzaSyAOda96fkiiGt0MhoNi-EJ0LnIaU0V4ZZM"
NASA_API_KEY="cStYLuOKTMgTCVlLx9aIgtsP0rbg2qsm7uDPNSxW"

#rds_connection_string = "postgres:bootcamp@localhost:5432/satellite"
#<insert password>@localhost:5432/customer_db"
#rds_connection_string = "postgres:admin@localhost:5432/satellite"
#engine = create_engine(f'postgresql://{rds_connection_string}')
#engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/satellite')
llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.3)

@app.route("/")
def home():
    
    query = 'give me two dinners to make this week one with chicken and the other vegetarian'
    response = llm.invoke(query)
    llmResponse = response.content
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("index.html", llmdata=llmResponse, query=query, responsedata=responsedata, 
                           init_page="initpage")
    


@app.route("/getPostData", methods=['POST'])
def getPostData():
    query = request.form.get("Search")
    response = llm.invoke(query)
    llmResponse = response.content
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("index.html", llmdata=llmResponse, query=query, responsedata=responsedata, init_page="initpage")
    


@app.route("/getPracForm", methods=['GET'])
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


    
    
    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("pracIndex.html", llmdata=llmResponse, requirement=requirement,   food1=food1, food2=food2,  responsedata=responsedata, init_page="initpage")
    

@app.route("/getPracPostData", methods=['POST'])
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


    
    

    resdata = [{
  
    }
    ]

    responsedata = { 'respdata': resdata
    }
    return render_template("pracIndex.html", llmdata=llmResponse, requirement=requirement,   food1=food1, food2=food2,  responsedata=responsedata, init_page="initpage")
    



@app.route("/getOpenApiForm", methods=['GET'])
def getOpenApiForm():
    responsedata = { }
    return render_template("openApiIndex.html", responsedata=responsedata, init_page="initpage")

@app.route("/getOpenApiPostData", methods=['POST'])
def getOpenApiPostData():
    question = request.form.get("question")

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
    



@app.route("/getResumeForm", methods=['GET'])
def getResumeForm():
    responsedata = { }
    return render_template("resumeReader.html", responsedata=responsedata, init_page="initpage")

@app.route("/getResumePostData", methods=['POST'])
def getResumePostData():
    question = request.form.get("question")
    urlData = request.form.get("urlData")    
    pdf_loader = PyPDFLoader(urlData)
    documents = pdf_loader.load()
    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.0)
    chain = load_qa_chain(llm)
    
    query = 'Could I write to Jane Doe in Spanish and expect her to understand?'
    result = chain.invoke({"input_documents": documents, "question": question})
    answer = result["output_text"]
    
    resdata = [
    ]
    
    querydata = {'question': question,
             'answer': answer}
    resdata.append(querydata)
    
    responsedata = { 'respdata': resdata
    }
   
    return render_template("resumeReader.html", sourceLink=urlData, question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    




@app.route("/getWikipediaForm", methods=['GET'])
def getWikipediaForm():
    responsedata = { }
    return render_template("wikipediaReader.html", responsedata=responsedata, init_page="initpage")

@app.route("/getWikipediaPostData", methods=['POST'])
def getWikipediaPostData():
    resdata = [
    ]
    question = request.form.get("question")
    urlData = request.form.get("urlData") 
    documents = WikipediaLoader(query=urlData, load_max_docs=2, load_all_available_meta=True).load()
    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.0)
    chain = load_qa_chain(llm)
    result = chain.invoke({"input_documents": documents, "question": question})
    answer = result["output_text"]
    querydata = {'question': question,
             'answer': answer}
    resdata.append(querydata)
    
    responsedata = { 'respdata': resdata
    }
   
    return render_template("wikipediaReader.html", topicData=urlData, question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getOpenTextForm", methods=['GET'])
def getOpenTextForm():
    responsedata = { }
    strData="""URL STRUCTURE
        Go to URL https://opentdb.com/api.php to get a plain text response, where
        the category is of type Computers, Mathematics, or Mythology,
        which are mapped to the numbers 18, 19, and 20 respectively.
        The amount parameter has to be specified to determine how many questions to return.
        The difficulty can be set to easy, medium, or hard. 
        Include no other text, only the API call URL. Don't use newlines."""
    return render_template("openTextDesc.html",  strData=strData, responsedata=responsedata, init_page="initpage")

@app.route("/getOpenTextPostData", methods=['POST'])
def getOpenTextPostData():
    question = request.form.get("question")
    spec_str = request.form.get("strData")
    print(spec_str)

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    api_docs=spec_str,
    verbose=True,
    limit_to_domains=["https://opentdb.com/api.php"])
    
    

    resdata = [    
    ]
    query = {"question": question}
    response = chain.invoke(query)
    answer = response["output"]
    querydata = {'question': question,
             'answer': answer}
    resdata.append(querydata)
    
    responsedata = { 'respdata': resdata
    }
   
    return render_template("openTextDesc.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getNASAForm", methods=['GET'])
def getNASAForm():
    responsedata = { }
    spec = """URL STRUCTURE
        To retrieve data on Geomagnetic Storms (GSTs) using the NASA API,         
        access the endpoint at https://api.nasa.gov/DONKI/GST. 
        Specify the start date using the "startDate" parameter in the format "yyyy-MM-dd"
        and the end date using the "endDate" parameter in the same format. 
        Ensure to include your API key using the "api_key" parameter, for example, "api_key"= NASA_API_KEY.
         Include no other text, only the API call URL. Don't use newlines.
        """
    return render_template("nasaQuestions.html", strData=spec,responsedata=responsedata, init_page="initpage")

@app.route("/getNASAPostData", methods=['POST'])
def getNASAPostData():
    question = request.form.get("question")
    spec_str = request.form.get("strData")
    print(spec_str)
    spec_str = """URL STRUCTURE
        To retrieve data on Geomagnetic Storms (GSTs) using the NASA API,         
        access the endpoint at https://api.nasa.gov/DONKI/GST. 
        Specify the start date using the "startDate" parameter in the format "yyyy-MM-dd"
        and the end date using the "endDate" parameter in the same format. 
        Ensure to include your API key using the "api_key" parameter, for example, "api_key"=NASA_API_KEY.
         Include no other text, only the API call URL. Don't use newlines.
        """
    
    spec_str = spec_str.replace("NASA_API_KEY",NASA_API_KEY)

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.0)


    chain = APIChain.from_llm_and_api_docs(
    llm,
    api_docs=json.dumps(spec_str),
    verbose=False,  # Changing to True will expose user's NASA_API_KEY API key.
    limit_to_domains=["https://api.nasa.gov/DONKI/GST"],)

    
    

    resdata = [    
    ]
    query = {"question": question}
    response = chain.invoke(query)
    answer = response["output"]
    querydata = {'question': question,
             'answer': answer}
    resdata.append(querydata)
    
    responsedata = { 'respdata': resdata
    }
   
    return render_template("nasaQuestions.html", strData=spec_str, question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getConversationalMemoryForm", methods=['GET'])
def getConversationalMemoryForm():
    responsedata = { }
    return render_template("conversationalMem.html", responsedata=responsedata, init_page="initpage")

@app.route("/getConversationalMemoryPostData", methods=['POST'])
def getConversationalMemoryPostData():
    question = request.form.get("question")
    spec_str = """Open Library provides ."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    
    

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
   
    return render_template("conversationalMem.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getSummaryMemoryForm", methods=['GET'])
def getSummaryMemoryForm():
    responsedata = { }
    return render_template("summaryMem.html", responsedata=responsedata, init_page="initpage")

@app.route("/getSummaryMemoryPostData", methods=['POST'])
def getSummaryMemoryPostData():
    question = request.form.get("question")
    spec_str = """Open Library provides ."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    
    

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
   
    return render_template("summaryMem.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getEventPlannerForm", methods=['GET'])
def getEventPlannerForm():
    responsedata = { }
    return render_template("eventPlanner.html", responsedata=responsedata, init_page="initpage")

@app.route("/getEventPlannerPostData", methods=['POST'])
def getEventPlannerPostData():
    question = request.form.get("question")
    spec_str = """Open Library provides ."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    
    

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
   
    return render_template("eventPlanner.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getPromptTemplateForm", methods=['GET'])
def getPromptTemplateForm():
    examples =  [
    {
        "query": "rat",
        "answer": "The cat sat next to the bat."
    }, {
        "query": "frog",
        "answer": "A dog hops a log in the bog."
    }, {
        "query": "ten",
        "answer": "Ben sent ten hens to the glen."
    }
    ]
  
    example_format = """
    Human: {query}
    AI: {answer}
    """
    suffix = """
    Human: {query}
    AI: 
    """
    prefix = """
    Here are examples between a human and AI. The human provides a word, and
    the AI provides a single sentence with easy to read words that mostly rhyme
    with the word the human provided. The sentence does not have to include the 
    original word. For example:
    """
    responsedata = { }
    return render_template("promptTemplates.html", examples=examples, example_format=example_format, suffix=suffix,prefix=prefix,
                           responsedata=responsedata, init_page="initpage")

@app.route("/getQuoteGenPostData", methods=['POST'])
def getQuoteGenPostData():
    question = request.form.get("question")
    suffix = request.form.get("suffix")
    example_format = request.form.get("example_format")
    examples = request.form.get("examples")
    examples =  [
    {
        "query": "rat",
        "answer": "The cat sat next to the bat."
    }, {
        "query": "frog",
        "answer": "A dog hops a log in the bog."
    }, {
        "query": "ten",
        "answer": "Ben sent ten hens to the glen."
    }
    ]
    prefix = request.form.get("prefix")
    spec_str = """Open Library provides ."""
    print(examples)
    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.3)
    
    example_template = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_format)
    
    prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_template,
    input_variables=["query"],
    prefix=prefix,
    suffix=suffix,
    example_separator="\n\n")
    chain = LLMChain(llm=llm, prompt=prompt_template)

    resdata = [    
    ]
    query = {"question": question}
    response = chain.run(question)
    answer = response
    querydata = {'question': question,
             'answer': answer}
    resdata.append(querydata)
    
    responsedata = { 'respdata': resdata
    }
   
    return render_template("promptTemplates.html",  examples=examples, example_format=example_format, suffix=suffix,prefix=prefix,
                            question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getDataParserForm", methods=['GET'])
def getDataParserForm():
    responsedata = { }
    return render_template("dataParsers.html", responsedata=responsedata, init_page="initpage")

@app.route("/getDataParserPostData", methods=['POST'])
def getDataParserPostData():
    question = request.form.get("question")
    spec_str = """Open Library provides ."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    
    

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
   
    return render_template("dataParsers.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getReceipeForm", methods=['GET'])
def getReceipeForm():
    responsedata = { }
    return render_template("recipeInfo.html", responsedata=responsedata, init_page="initpage")

@app.route("/getReceipePostData", methods=['POST'])
def getReceipePostData():
    question = request.form.get("question")
    spec_str = """Open Library provides ."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    
    

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
   
    return render_template("recipeInfo.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getLnsAgentForm", methods=['GET'])
def getLnsAgentForm():
    responsedata = { }
    return render_template("lnsAgent.html", responsedata=responsedata, init_page="initpage")

@app.route("/getLnsAgentPostData", methods=['POST'])
def getLnsAgentPostData():
    question = request.form.get("question")
    spec_str = """Open Library provides ."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    
    

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
   
    return render_template("lnsAgent.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getStuGenForm", methods=['GET'])
def getStuGenForm():
    responsedata = { }
    return render_template("stuGenAI.html", responsedata=responsedata, init_page="initpage")

@app.route("/getStuGenPostData", methods=['POST'])
def getStuGenPostData():
    question = request.form.get("question")
    spec_str = """Open Library provides ."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    
    

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
   
    return render_template("stuGenAI.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    


@app.route("/getPictureCaptionForm", methods=['GET'])
def getPictureCaptionForm():
    responsedata = { }
    return render_template("pictureCaptioning.html", responsedata=responsedata, init_page="initpage")

@app.route("/getPictureCaptionPostData", methods=['POST'])
def getPictureCaptionPostData():
    question = request.form.get("question")
    spec_str = """Open Library provides ."""

    llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY, model=GEMINI_MODEL, temperature=0.9)
    chain = APIChain.from_llm_and_api_docs(
    llm,
    spec_str,
    #verbose = True,
    limit_to_domains=["https://openlibrary.org/"])
    
    

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
   
    return render_template("pictureCaptioning.html",  question=question, answer=answer, responsedata=responsedata, init_page="initpage")
    



@app.route("/getSatellite/<cntry>/<numSat>")
def satellite_country(cntry,numSat):

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
   
    return render_template("index.html", responsedata=responsedata,
     init_page="notinitpage" )

@app.route("/getSatelliteById/<satid>/<numSat>")
def satellite_byid(satid,numSat):


    
    
    
    

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
   
    return render_template("index.html", responsedata=responsedata,  
    init_page="notinitpage" )

@app.route("/getSatelliteByName/<satName>/<numSat>")
def satellite_byname(satName,numSat):


    
    
    
    

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
   
    return render_template("index.html", responsedata=responsedata,
      init_page="notinitpage")



if __name__ == "__main__":
    app.run(debug=True)
    
