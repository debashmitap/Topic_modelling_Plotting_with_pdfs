import os
import PyPDF2
import matplotlib.pyplot as plt

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        print("Parsing PDF at path: " + pdf_path)
        reader = PyPDF2.PdfReader(file, strict=False)
        num_pages = len(reader.pages)
        text = []
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text.append(page.extract_text())
    
    return "\n".join(text)

# Path to the folder containing the PDF files
folder_path = r'C:\Users\poddar\Desktop\Papers'

# List to hold the extracted text from all PDF files
all_text = []

# Extract text from all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        all_text.append(extract_text_from_pdf(pdf_path))

# Combine all extracted text
combined_text = " ".join(all_text)

# List of human-induced pressures
pressures = [
    "agriculture", "urbanization", "industrialization", "deforestation", 
    "overfishing", "pollution", "climate change", "habitat fragmentation", 
    "mining", "tourism"
]

# Count the occurrences of each pressure in the combined text
pressure_counts = {pressure: combined_text.lower().count(pressure) for pressure in pressures}

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


