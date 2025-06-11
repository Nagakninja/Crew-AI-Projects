# YouTube Blog Writer CrewAI Project

This project demonstrates how to use CrewAI agents, Google Gemini LLM, and YouTube content search tools to automate the process of researching and writing tech blogs based on YouTube videos from a specific channel. The workflow is orchestrated by CrewAI, with agents collaborating to extract insights from YouTube and generate engaging blog articles.

---

## Features

- **Multi-Agent Collaboration:**
  - **Blog Researcher:** Searches a specified YouTube channel for relevant videos and extracts transcriptions for a given topic.
  - **Blog Writer:** Crafts compelling, easy-to-understand blog articles based on the research findings.
- **YouTube Channel Search:**
  - Uses `crewai_tools.YoutubeChannelSearchTool` to target a specific channel (e.g., `@DanVega`).
- **LLM Integration:**
  - Utilizes Google Gemini ("Gemini 2.5 Pro Experimental 03-25") via `langchain_google_genai` for advanced language understanding and content generation.
- **Configurable Workflow:**
  - Task execution is sequential, with memory, caching, and verbose logging enabled for transparency and efficiency.
- **Customizable Output:**
  - The topic for research and writing can be easily changed in the code.

---

## Project Structure

```
YT-Blog-Writer/
├── agents.py         # Defines the researcher and writer agents
├── crew.py           # Orchestrates the workflow and runs the crew
├── tasks.py          # Defines research and writing tasks
├── tools.py          # YouTube channel search tool
├── requirements.txt  # Python dependencies
└── ...
```

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Crew-AI-Projects/YT-Blog-Writer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Ensure your `requirements.txt` includes:
   - `crewai`
   - `crewai_tools`
   - `langchain-google-genai`
   - `python-dotenv`
   - `youtube-transcript-api`
   - `yt_dlp`

3. **Set Up Environment Variables**
   - Create a `.env` file in the project directory with your Google API key:
     ```
     GOOGLE_API_KEY=your-google-api-key
     ```

---

## How It Works

- **Agents:**
  - `blog_researcher`: Uses the YouTube tool to find and extract video transcriptions for the specified topic from the target channel.
  - `blog_writer`: Uses the same tool and LLM to write a blog article based on the research findings.
- **Workflow:**
  - `crew.py` creates a `Crew` with both agents and their tasks, then runs the workflow sequentially.
  - The result is printed to the console.
- **Customization:**
  - Change the `inputs={'topic':'Spring AI Going GA'}` line in `crew.py` to research and write about a different topic.

---

## Running the Application

1. **Run the Crew Workflow**
   ```bash
   python crew.py
   ```
   - The agents will collaborate to research and write about the specified topic using YouTube content.
   - The result will be printed in the terminal.

---

## Requirements

- Python 3.8+
- Google API key for Gemini
- Internet connection for LLM and YouTube access

---

## License

This project is provided for educational purposes. See the repository for license details.

---

## Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Google Gemini](https://ai.google.dev/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
