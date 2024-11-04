# langchain_llm_finalproject  (Emerging/Advanced AI topics)(Image captioning)

## Emerging AI topics 

In the emerging topics the LLM model created from ChatGoogleGenerativeAI extensively used for all the emerging topics, the attributes for GEMINI API KEY, GEMINI MODEL and temperature plays more critical role to get the required model for to resolve and predict the testing data.function similarly, whether they are generating text, images, or music. In this activity, you’ll have the option of choosing between developing an image or a piece of music.

Recall that image-generation models are trained to recognize noise and predict what the cleared up image should look like. This training process involves first adding noise to an image, then using the model to predict the original image by using the information in the noisy version of the image. In essence, image generation then happens in reverse: a noisy image is generated based on text descriptors (labels). The model then identifies the “level” of noise in this image and clarifies it with a predictive algorithm (Isaacs-Thomas, 2023).

Just like text- and image-generating models, music generators use complex transformers to identify and associate prompts and parts of prompts with particular qualities in sound data.

There are dozens of generative AI tools available, and you likely have already put some of them to use. The goal of this activity is to give you an additional tool to draw from, so we recommend using a tool that is new to you.

To Create a web app that generates articles, blog posts, or social media content based on user input or specified topics. ncorporate LangChain to manage the different steps of content creation, including research, drafting, and editing

Data Analysis with Natural Language Queries

To Create a dashboard that allows users to perform data analysis by asking questions in natural language. Use GPT-4 to interpret the queries and LangChain to connect to data sources, execute queries, and return results in a user-friendly format. Document Summarization Tool

To Build an application that summarizes long documents or articles into concise summaries. Use LangChain to handle the document processing and GPT-4 for generating the summaries.
 

## LangChain Google Chat API Intro
The ChatGoogle API provides more interactive approach for the set of required questions

Some of the common query "give me two dinners to make this week one with chicken and the other vegetarian"

The chatgoogle api provides the recipe for the above and also preparation steps, the food items are chosen from variety of the model trained data.

The interactive approach is also implemened to get food1 and food2  and dietary requirements


## LangChain Open API questions from https://openlibrary.org

These are the questions to openlibrary, to get the list of "core java books", "advanced python book", "favorite movies" and so amny questions, the model built using the open library trained data sets and provides the answers for the questions asked to open library

##  LangChain Resume Reader

The Lang chain generative AI could read the resume and ask questions on the resume to get the required data

The resume is provided as PDF file ( the PDFLoader) from Lang Chain used to read the pdf and ask required question

Ex: Could I write to Jane Doe in Spanish and expect her to understand?

This is the question to the Jane Doe Resume, after parsing the PDF document LLM provides the answers

##  LangChain Wikipedia Questions  https://wikipedia.org

The wikipedia Loader API provides the list of documents Wikipedia has, some of the questions to the Wikipedia through LLM provides the answers correctly
Ex:
Wikipedia Topic  "Leonard Cohen"

Question : How many albums has Leonard Cohen released?

For the above question LLM uses the Wikipedia loader API to retrieve the required answer    Leonard Cohen released 15 albums

##  LangChain OpenText Description Questions https://opentdb.com

  Go to URL https://opentdb.com/ to get a plain text response, where
        the category is of type Computers, Mathematics, or Mythology,

The Source String Structure is also provided as input to choose the topic like (Computes, Mathematics and Mythology to ask the required question from these area)

Question : What is a difficult trivia question about Computers?

The LLM queries the opentdb API and gets the data from the above data set.

##  LangChain NASA Questions https://api.nasa.gov/DONKI/GST. 

Nasa has the list of GeoMagnetic storm for each year and trained the model, the above data is the endpoint URL where langchain gets the data , the spec structure and limit domain URL for the langchain gets the data for required specific question for the spec

Ex:
Spec: URL STRUCTURE
        To retrieve data on Geomagnetic Storms (GSTs) using the NASA API,         
        access the endpoint at https://api.nasa.gov/DONKI/GST. 
        Specify the start date using the "startDate" parameter in the format "yyyy-MM-dd"
        and the end date using the "endDate" parameter in the same format. 
        Ensure to include your API key using the "api_key" parameter, for example, "api_key"= NASA_API_KEY.
         Include no other text, only the API call URL. Don't use newlines.
        
Question: Get a list of the 3 strongest Geomagnetic Storms in 2024 and show the details such as when they occurred and the corresponding KP Index for each one of them?

Answer: 
The 3 strongest Geomagnetic Storms in 2024 were:

1. **2024-05-10T15:00:00-GST-001**: Occurred on May 10, 2024, with a maximum KP Index of 9.0.
2. **2024-10-10T15:00:00-GST-001**: Occurred on October 10, 2024, with a maximum KP Index of 9.0.
3. **2024-03-24T12:00:00-GST-001**: Occurred on March 24, 2024, with a maximum KP Index of 8.0. 
 
 
 According to the question the required data could be obtained through this model
 

##  LangChain Prompt Template

The templates are set of specs for the query string and other required input format and response format of the string so according to the specific formats of input and output the LLM uses the prompt template and LLM model to get the data
Ex:
content="You are an athletic trainer."
content="Provide me with a summary of what to do this week for my workouts."

The output from LLM
Please tell me more about your goals and current fitness level! To give you a personalized workout plan, I need to know:

* **What are your fitness goals?** (e.g., lose weight, gain muscle, improve endurance, etc.)
* **What is your current fitness level?** (e.g., beginner, intermediate, advanced)
* **What kind of workouts do you enjoy?** (e.g., running, weightlifting, yoga, swimming, etc.)
* **How many days a week can you work out?**
* **Do you have any injuries or limitations?**

Once I have this information, I can create a safe and effective workout plan for you. 


Template 2:
    Human: {query}
    AI: {answer}
    
    
    query  "grime"
    
    The output is text:
    {'query': 'grime', 'text': 'Human: grime\nAI: The mime climbed a lime tree in the prime. \n'} 
    
    

##  LangChain Image Captioning


In the image captioning the images are stored locally on img folder and the GUI interface requests the image that requires the caption when user enters the file name and submit it provides the caption for the image

ex:  group of workers , dog running on grass, soccer and many more, if the model trained with more data set more generic png files could be used to get the required caption


---

## References


     Image Generators

    * [DALL-E 2](https://openai.com/product/dall-e-2) is a popular image generator from OpenAI that, like Stable Diffusion, generates images based on text prompts using “contrastive learning” that trains transformers to associate text descriptions with related images (Bullas, 2023).

    * [Artbreeder](https://www.artbreeder.com/) is unique among image generators in that it doesn’t require text prompts. Instead, users can manipulate images through a range of sliders to create their own original artwork.

    * [DeepArt.io](https://creativitywith.ai/deepartio/) takes user images and recreates them in the styles of significant art movements, such as Pop Art or Impressionism.

     Music Generators

    * [Aimi](https://www.aimi.fm/) can craft and output a new sound file that can be modified to the producer’s liking without them having to compose, record, and assemble a final mix from scratch.

    * [Soudraw](https://soundraw.io/) allows users to generate their own royalty-free music based on the mood, genre, and length of song requested.
    
Black, D. 2023. *AI music generator apps &ndash DJ’s worst nightmare or the ultimate tool?* Available: [https://cybernews.com/editorial/ai-music-generator-apps/](https://cybernews.com/editorial/ai-music-generator-apps/) [2023, April 25].

Bullas, J. 2023. *The ultimate list of AI image generator tools &ndash; create powerful visuals for your next digital marketing campaign* [Blog, 25 May]. Available: [https://www.jeffbullas.com/ai-image-generator/](https://www.jeffbullas.com/ai-image-generator/) [2023, April 25].

Isaacs-Thomas, B. 2023. *How AI turns text into images*. Available: [https://www.pbs.org/newshour/science/how-ai-makes-images-based-on-a-few-words](https://www.pbs.org/newshour/science/how-ai-makes-images-based-on-a-few-words) [2023, April 25].

---



