# import os
# import streamlit as st

# class FileReaderAgent:
#     def walk_directory(self, folder_path):
#         folder_structure = {}
#         total_files = sum([len(files) for r, d, files in os.walk(folder_path)])
#         progress = st.progress(0)
#         status_text = st.empty()
#         file_count = 0

#         for root, dirs, files in os.walk(folder_path):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 try:
#                     with open(file_path, 'r', errors='ignore') as f:
#                         folder_structure[file_path] = f.read()
#                 except PermissionError:
#                     st.warning(f"Permission denied: {file_path}")
#                     continue
#                 except Exception as e:
#                     st.error(f"Error reading {file_path}: {e}")
#                     continue
                
#                 file_count += 1
#                 progress.progress(file_count / total_files)
#                 status_text.text(f"Processing file {file_count}/{total_files}: {file_path}")
        
#         return folder_structure


import os
import networkx as nx

class FileReaderAgent:
    def __init__(self):
        self.graph = nx.DiGraph()

    def walk_directory(self, folder_path):
        folder_structure = {}
        for root, dirs, files in os.walk(folder_path):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', errors='ignore') as f:
                        content = f.read()
                        folder_structure[file_path] = content
                        self.graph.add_node(file_path, content=content)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
        return folder_structure

    def get_graph(self):
        return self.graph

