from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process with enhanced feedback

result=crew.kickoff(inputs={'topic':'Artificial General intelligence in tech industry'})
print(result)