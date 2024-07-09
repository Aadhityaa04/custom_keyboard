import subprocess
import json

def search_arduino_library(library_name):
    try:
        # Run the arduino-cli command
        result = subprocess.run(['./arduino-cli', 'lib', 'search', library_name], 
                                capture_output=True, text=True, check=True)
        
        # Parse the output
        libraries = []
        current_library = {}
        for line in result.stdout.splitlines():
            if line.startswith("Name:"):
                if current_library:
                    libraries.append(current_library)
                current_library = {"Name": line.split(":")[1].strip()}
            elif line.startswith("  Author:"):
                current_library["Author"] = line.split(":")[1].strip()
            elif line.startswith("  Maintainer:"):
                current_library["Maintainer"] = line.split(":")[1].strip()
            elif line.startswith("  Sentence:"):
                current_library["Sentence"] = line.split(":")[1].strip()
            elif line.startswith("  Paragraph:"):
                current_library["Paragraph"] = line.split(":")[1].strip()
            elif line.startswith("  Website:"):
                current_library["Website"] = line.split(":")[1].strip()
            elif line.startswith("  Category:"):
                current_library["Category"] = line.split(":")[1].strip()
            elif line.startswith("  Architecture:"):
                current_library["Architecture"] = line.split(":")[1].strip()
            elif line.startswith("  Types:"):
                current_library["Types"] = line.split(":")[1].strip()
            elif line.startswith("  Versions:"):
                current_library["Versions"] = line.split(":")[1].strip().strip('[]').split(', ')
        if current_library:
            libraries.append(current_library)
        
        # Convert to JSON-like structure
        return libraries
        
    except subprocess.CalledProcessError as e:
        # Handle errors in subprocess execution
        print(f"Command failed with error: {e}")
        print(e.stderr)
        return None

# Example usage
library_name = "HID-Project"
result = search_arduino_library(library_name)
if result:
    print(json.dumps(result, indent=2))
else:
    print("No libraries found.")
