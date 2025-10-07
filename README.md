*“I asked my AI to summarize my codebase. It replied, ‘You could’ve just written cleaner comments.’”*  

# 🧩 SummarizeFlow  

**SummarizeFlow** is a multi-agent, graph-based file summarizer built for complex projects with deep directory hierarchies.  
It automatically reads, organizes, and summarizes files  turning messy folders into structured, high-level summaries.  

Think of it as a **project-wide TL;DR generator** that actually understands dependencies.  

🔗 **Repo:** https://github.com/GhoshSrinjoy/SummarizeFlow  

---

## Executive Summary  

When projects grow, documentation often doesn’t. SummarizeFlow fixes that by using a **graph of intelligent agents** that scan your entire file structure, summarize each file, and connect the dots.  

Each file becomes a **node in a graph**, each dependency an **edge**, and each summary part of a **bigger story**.  

The result: an elegant, JSON-formatted summary map of your entire codebase  perfect for onboarding, audits, or quick understanding of large repositories.  
## Features

- **Graph-Based Processing**: Files are treated as nodes in a graph, allowing for flexible processing order and dependency management.
- **Automatic Summarization**: Summarizes the content of text-based files using an integrated language model.
- **Streamlit Integration**: User-friendly interface powered by Streamlit, providing real-time progress updates and final summary output.
- **JSON Output**: Summaries are saved in a structured JSON format, reflecting the folder hierarchy.

## How It Works

1. **Directory Walk and Graph Construction**:
   - The application starts by walking through the provided directory and reading each file. 
   - Each file is added as a node in a directed graph. Edges can be defined between nodes to represent dependencies or processing order.

2. **Graph-Based Summarization**:
   - The files (nodes) are processed based on the graph's structure. Nodes are traversed in topological order, ensuring that any dependencies are respected.
   - The content of each file is passed to a language model, which generates a summary.

3. **Real-Time Progress Updates**:
   - As files are processed, progress is displayed in the Streamlit interface. Users can see which files are being summarized and the time taken for each.

4. **Output**:
   - The summarized content is saved in a JSON file, maintaining the original folder hierarchy. The JSON output can be easily used for further processing or analysis.

## Project Structure

- **`main.py`**: The entry point of the application. It initializes the Streamlit interface and starts the summarization process.
- **`supervisor.py`**: Contains the `SupervisorAgent` class, which manages the overall process, including graph construction, file processing, and final output generation.
- **`file_reader.py`**: Contains the `FileReaderAgent` class, responsible for walking through the directory structure, reading files, and constructing the graph.
- **`summarizer.py`**: Contains the `SummarizerAgent` class, which interacts with the language model to generate summaries for each file.
- **`json_writer.py`**: Contains the `JSONWriterAgent` class, which formats and writes the summarized data into a structured JSON file.

## Installation

### Requirements

- Python 3.7+
- Streamlit
- NetworkX
- LangChain
- Timeout-Decorator

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/summarizeflow.git
   cd summarizeflow
