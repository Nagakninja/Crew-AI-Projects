# Research Agent CrewAI Project

This project demonstrates how to build a multi-agent research and writing workflow using [CrewAI](https://github.com/joaomdmoura/crewAI), Google Gemini (via LangChain), and custom tools. The agents collaborate to research and write compelling articles on technology topics, leveraging LLMs and tool augmentation.

---

## Features

- **Multi-Agent Collaboration:**
  - Senior Researcher agent uncovers and analyzes trends in a given topic.
  - Writer agent crafts engaging, accessible articles based on research findings.
- **LLM Integration:**
  - Uses Google Gemini ("gemini-1.5-flash") via `langchain_google_genai` for advanced language understanding and generation.
- **Tool Augmentation:**
  - Agents are equipped with custom tools (see `tools.py`) to enhance their capabilities.
- **Task Orchestration:**
  - Tasks are defined and assigned to agents for sequential execution using CrewAI's `Crew` and `Process` classes.
- **Output Customization:**
  - Final article is saved as a markdown file (`new-blog-post.md`).

---

## Project Structure

```
Research-Agent/
├── agents.py         # Defines the researcher and writer agents
├── crew.py           # Orchestrates the workflow and runs the crew
├── tasks.py          # Defines research and writing tasks
├── tools.py          # Custom tools for agent augmentation
├── requirements.txt  # Python dependencies
├── new-blog-post.md  # Output: generated article
└── ...
```

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Crew-AI-Projects/Research-Agent
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Ensure your `requirements.txt` includes:
   - `crewai`
   - `langchain`
   - `langchain-google-genai`
   - `python-dotenv`
   - Any other dependencies for your custom tools

3. **Set Up Environment Variables**
   - Create a `.env` file in the project directory with your Google API key:
     ```
     GOOGLE_API_KEY=your-google-api-key
     ```

4. **Configure Tools**
   - Edit `tools.py` to customize or add tools as needed for your research and writing tasks.

---

## How It Works

- **Agents:**
  - `news_researcher`: Uses Gemini LLM and tools to research the latest trends in a given topic.
  - `news_writer`: Uses Gemini LLM and tools to write an engaging article based on the research.
- **Tasks:**
  - `research_task`: Instructs the researcher to analyze and report on the topic.
  - `write_task`: Instructs the writer to compose a markdown article.
- **Crew Orchestration:**
  - `crew.py` creates a `Crew` with both agents and tasks, then runs the workflow sequentially.
  - The result is printed and saved to `new-blog-post.md`.

---

## Running the Application

1. **Run the Crew Workflow**
   ```bash
   python crew.py
   ```
   - The agents will collaborate to research and write about the topic (default: "AI in healthcare").
   - The final article will be saved as `new-blog-post.md`.

2. **Customize the Topic**
   - Edit the `inputs={'topic':'AI in healthcare'}` line in `crew.py` to change the research topic.

---

## Requirements

- Python 3.8+
- Google API key for Gemini
- Internet connection for LLM and tool access

---

## License

This project is provided for educational purposes. See the repository for license details.

---

## Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Google Gemini](https://ai.google.dev/)
