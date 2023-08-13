########google search########################

mygptkey = "Openai API key"

from langchain.llms import OpenAI

myllm = OpenAI(
    model = 'text-davinci-003',
    temperature=1,
    openai_api_key=mygptkey
)

myserpkey = "SERPAPI key"

import os

os.environ["SERPAPI_API_KEY"] = myserpkey

from langchain.agents import load_tools

myserptool = load_tools(tool_names=["serpapi"])

from langchain.agents import AgentType

from langchain.agents import initialize_agent

mygooglechain = initialize_agent(
    llm = myllm,
    tools= myserptool,
    agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


mygooglechain.run("When gadar 2 movie is released?")


##############google search code end#############



#langchain twitter search


import tweepy

from langchain.document_loaders import TwitterTweetLoader

loader = TwitterTweetLoader.from_bearer_token(
    oauth2_bearer_token="Token",
    twitter_users=["@elonmusk"],
    number_tweets=50,  # Default value is 100
)


loader.twitter_users

loader.number_tweets


#documents = loader.load()
#documents[:5]

######################Twitter end######################################


#wikipedia code to search by integrating Chatgpt and google

from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())


wikipedia.run("abdul kalam")

#################################################wikipedia end##################



#################dall-e##################


from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "KEY"


from langchain.utilities.dal import DallEAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["image_desc"],
    template="Generate a detailed prompt to generate an image based on the following description: {image_desc}",
)
chain = LLMChain(llm=llm, prompt=prompt)



######################dall-e end###################




#############You tube seach results#############

from langchain.tools import YouTubeSearchTool


tool = YouTubeSearchTool()


tool.run("jim kwik", 5)

###################You tube end###############

