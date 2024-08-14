import os
import time
import networkx as nx
from agents.file_reader import FileReaderAgent
from agents.summarizer import SummarizerAgent
from agents.json_writer import JSONWriterAgent
import streamlit as st

class SupervisorAgent:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.file_reader = FileReaderAgent()
        self.summarizer = SummarizerAgent()
        self.json_writer = JSONWriterAgent()
        self.graph = None

    def build_graph(self):
        folder_structure = self.file_reader.walk_directory(self.folder_path)
        self.graph = self.file_reader.get_graph()

    def process_node(self, node):
        file_path = node
        content = self.graph.nodes[node]['content']
        summary = self.summarizer.summarize_content(content)
        return summary

    def run(self):
        st.info("Starting directory walk...")
        self.build_graph()

        summaries = {}
        progress = st.progress(0)
        file_count = 0
        total_files = len(self.graph.nodes)

        expander = st.expander("Generating summaries...", expanded=False)
        start_time = time.time()

        # Process nodes sequentially
        for node in nx.topological_sort(self.graph):
            summary = self.process_node(node)
            summaries[node] = summary

            # Update progress and UI
            file_count += 1
            progress.progress(file_count / total_files)
            time_taken = time.time() - start_time
            if expander:
                expander.write(f"Summarized: {node} - {summary} (Time taken: {time_taken:.2f} seconds)")
            st.text(f"Processed {file_count}/{total_files} files")

        total_time = time.time() - start_time
        if expander:
            expander.write(f"Total time taken for summarization: {total_time:.2f} seconds")

        st.info("Writing JSON output...")
        output = self.json_writer.write_json(self.graph.nodes, summaries)
        
        st.success("Processing Complete!")
        return output
