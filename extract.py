from bs4 import BeautifulSoup
import re
import json

# Assuming `html_content` contains the HTML from the question
html_content = open("index.html").read()

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all projects
projects_divs = soup.find_all("div", class_="cell project")

# Initialize a list to hold project data
projects_data = []

# Extract data for each project
for project_div in projects_divs:
    # Extract project name, year, and optionally, collaboration and its link
    project_name = project_div.find("h3").get_text(strip=True)
    em = project_div.find("em")
    if not em:
        continue
    
    em_text = em.get_text(strip=True)
    
    results = []
    if 'with' in em_text:
        collaborators = em.find_all("a")
        for collaborator in collaborators:
            results.append({
                "name": collaborator.get_text(strip=True),
                "url": collaborator["href"]
            })
    
    
    # for the year, take the first 4-digit number, using re
    year = re.search(r"\d{4}", em_text).group()
    
    # Extract description
    description_tag = project_div.find("div", class_="description")
        
    # get raw HTML from description div
    description = str(description_tag)
    description = description.split('</em>')[-1].strip() if '</em>' in description else description
    # remove the ending </div>
    description = description.split('</div>')[0].strip()
    # print(description)
        
    # Extract image source
    image = project_div.find("img")["src"] if project_div.find("img") else None
    
    # remove thumbs/ from image
    image = image.replace("thumbs/", "") 
    
    # Extract links
    links = []
    for link in project_div.find('ul').find_all("a"):
        links.append({
            "text": link.get_text(strip=True),
            "url": link["href"]
        })
            
    # Construct project detail object
    project_data = {
        "name": project_name,
        "year": year,
        "description": description,
        "links": links,
        "image": image,
        "collaborators": results
    }
    
    projects_data.append(project_data)

# Construct the final dictionary
final_dict = {"works": projects_data}

# Convert dict to JSON
json_data = json.dumps(final_dict, indent=2)

# Print or save to a file
# print(json_data)
# If you want to save the JSON to a file do the following:
with open("projects.json", "w") as json_file:
    json_file.write(json_data)