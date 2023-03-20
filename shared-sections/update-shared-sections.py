import os
from bs4 import BeautifulSoup

fullFilePath = r'E:\Users\PC\Documents\web-sites\st-website\shared-sections\test.htm'

# Open the HTML file and read its contents
with open(fullFilePath, 'r', encoding="utf-8") as file:
    html = file.read()

# Use BeautifulSoup to parse the HTML and find the navigation element
soup = BeautifulSoup(html, 'html.parser')
nav = soup.find('nav')

# Update the navigation element (for example, by adding a new link)
new_content = '''
<ul>
  <li><a href="#">Link 1</a></li>
  <li><a href="#">Link 2</a></li>
  <li><a href="#">Link 3</a></li>
</ul>
'''
nav.contents = BeautifulSoup(new_content, 'html.parser').contents

# Save the updated HTML to a new file
new_html_path = r'E:\Users\PC\Documents\web-sites\st-website\shared-sections\test-out.htm'
with open(new_html_path, 'w', encoding="utf-8") as file:
    file.write(str(soup))