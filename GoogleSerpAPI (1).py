#!/usr/bin/env python
# coding: utf-8

# In[ ]:


########google search########################


# In[37]:


mygptkey = "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"


# In[ ]:





# In[38]:


from langchain.llms import OpenAI


# In[39]:


myllm = OpenAI(
    model = 'text-davinci-003',
    temperature=1,
    openai_api_key=mygptkey
)


# In[ ]:





# In[40]:


myserpkey = "d0ab357c3b66fe2dee2bbe013b19d4f6db97893105b51c6e70d489fb3f6b40d2"


# In[41]:


import os


# In[42]:


os.environ["SERPAPI_API_KEY"] = myserpkey


# In[43]:


from langchain.agents import load_tools


# In[44]:


myserptool = load_tools(tool_names=["serpapi"])


# In[45]:


from langchain.agents import AgentType


# In[46]:


from langchain.agents import initialize_agent


# In[47]:


mygooglechain = initialize_agent(
    llm = myllm,
    tools= myserptool,
    agent= AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


# In[48]:


mygooglechain.run("When gadar 2 movie is released?")


# In[50]:


##############google search code end#############


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#langchain twitter search


# In[32]:


import tweepy


# In[33]:


from langchain.document_loaders import TwitterTweetLoader


# In[36]:


loader = TwitterTweetLoader.from_bearer_token(
    oauth2_bearer_token="AAAAAAAAAAAAAAAAAAAAAOjcpAEAAAAAgG5t9I2DJ09m87eOFudaD4EOkuk%3D5iOHtnDf4Pp87u2ZwzEjdDuGZSX4MRdJ2mpZUYGp09VZAzbZtV",
    twitter_users=["@elonmusk"],
    number_tweets=50,  # Default value is 100
)


# In[38]:


loader.twitter_users


# In[39]:


loader.number_tweets


# In[46]:


#documents = loader.load()
#documents[:5]


# In[ ]:


######################Twitter end######################################


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#wikipedia code to search by integrating Chatgpt and google


# In[ ]:





# In[41]:


from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper


# In[42]:


wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())


# In[45]:


wikipedia.run("abdul kalam")


# In[ ]:





# In[49]:


#################################################wikipedia end##################


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[51]:


#################dall-e (But not working)##################


# In[59]:


from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"


# In[60]:


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


# In[ ]:





# In[52]:


######################dall-e end###################


# In[ ]:





# In[53]:


##############YouTube search##################


# In[ ]:





# In[ ]:





# In[58]:


#############You tube seach results#############


# In[54]:


from langchain.tools import YouTubeSearchTool


# In[55]:


tool = YouTubeSearchTool()


# In[56]:


tool.run("jim kwik", 5)


# In[57]:


tool


# 

# In[ ]:


###################You tube end###############

