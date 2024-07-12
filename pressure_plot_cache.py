import os
import PyPDF2
import matplotlib.pyplot as plt
import argparse
import json

# List of human-induced pressures
pressures = [
    "agriculture", "urbanization", "industrialization", "deforestation", 
    "overfishing", "pollution", "climate change", "habitat fragmentation", 
    "mining", "tourism"
]

# Set up argument parser
parser = argparse.ArgumentParser(
    prog="Pressure_plot",
    description="Reading and plotting topic counts from a folder"
)

# Accept a filename as either '-f' or '--file'
parser.add_argument('-f', '--file', required=True)
args = parser.parse_args()

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    json_path = os.path.splitext(pdf_path)[0] + ".json"  # returns ('/home/user/somefile', '.txt')
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            pressure_counts = json.load(f)
            return pressure_counts
        
    pressure_counts = {pressure: 0 for pressure in pressures}
    with open(pdf_path, 'rb') as file:
        print("Parsing PDF at path: " + pdf_path)
        reader = PyPDF2.PdfReader(file, strict=False)
        num_pages = len(reader.pages)
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            for pressure in pressures:
                pressure_counts[pressure] += page_text.lower().count(pressure)   
            
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(pressure_counts, f, ensure_ascii=False, indent=4)   
    return pressure_counts
    
# Path to the folder containing the PDF files
folder_path = args.file

# List to hold the extracted text from all PDF files
pressure_counts = {pressure: 0 for pressure in pressures}
# Extract text from all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        pdf_pressures = extract_text_from_pdf(pdf_path) 
        for pressure in pressures:
            pressure_counts[pressure] += pdf_pressures[pressure]



# Calculate the total number of pressures mentioned
total_mentions = sum(pressure_counts.values())

# Calculate the percentage of each pressure
pressure_percentages = {pressure: (count / total_mentions) * 100 for pressure, count in pressure_counts.items()}

# Plot the percentages
plt.figure(figsize=(10, 6))
plt.bar(pressure_percentages.keys(), pressure_percentages.values(), color='red')
plt.xlabel('Human-Induced Pressures')
plt.ylabel('Percentage (%)')
plt.title('Percentage of Human-Induced Pressures on Ecosystems and Habitats')
plt.xticks(rotation=45)
plt.show()


