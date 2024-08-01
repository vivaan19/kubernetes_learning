from bs4 import BeautifulSoup

# Read the HTML content from a file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all span elements with a class containing 'cueText'
cue_text_spans = soup.find_all('span', class_=lambda x: x and 'cueText' in x)

# Open the output file for writing
with open('output.txt', 'w', encoding='utf-8') as output_file:
    # Iterate over each found span element and write its text to the output file
    for span in cue_text_spans:
        output_file.write(span.get_text() + '\n')
