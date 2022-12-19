import os
import json
import networkx as nx

# Set the path to the folder containing the JSON-LD files
folder_path = "kg_json"

# Iterate through the files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    
    # Attempt to load the JSON-LD file
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        # If an error occurs while loading the file, print the error and skip the file
        print(f"Error while loading {file_name}: {e}")
        continue
    
    # Attempt to convert the JSON-LD data to a GEXF file
    try:
        graph = nx.node_link_graph(data)
        nx.write_gexf(graph, f"{file_name}.gexf", encoding='utf-8')
        print(f"{file_name} converted to GEXF format")
    except Exception as e:
        # If an error occurs while converting the file, print the error
        print(f"Error while converting {file_name}: {e}")
