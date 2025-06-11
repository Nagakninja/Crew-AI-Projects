from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv

load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="Gemini 2.5 Pro Experimental 03-25",
                           verbose=True,
                           temperature=0.7,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))


## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding videos on Spring AI, Its features, and its use cases,"
       "you delve into the depths of content, extracting insights" 
    ),
    tools=[yt_tool],
    allow_delegation=True
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False


)