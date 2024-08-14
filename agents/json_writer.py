import json
import os

class JSONWriterAgent:
    def write_json(self, folder_structure, summaries):
        nested_structure = self._nest_structure(folder_structure, summaries)
        json_output = json.dumps(nested_structure, indent=2)
        return json_output

    def _nest_structure(self, folder_structure, summaries):
        nested_structure = {}
        for path, summary in summaries.items():
            parts = path.split(os.sep)
            current_level = nested_structure
            for part in parts[:-1]:
                current_level = current_level.setdefault(part, {})
            current_level[parts[-1]] = summary
        return nested_structure
