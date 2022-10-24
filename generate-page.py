import os

def writeToFile(path, content):
  file = open(path, "w")
  file.write(content)
  file.close()

start_num = 0
file_num = 0

# ----------------------------------------- Set according to directory - var ----------------------------
# ****** REPLACE THIS WITH PROJECT DIRECTORY *********
current_path = (r"Z:\programming\next-template")

component_directory = "components"
page_directory = "pages"
styles_directory = "styles"

component_path = os.path.join(current_path, component_directory)
page_path = os.path.join(current_path, page_directory)
styles = os.path.join(current_path, styles_directory)

def react_content_func(name):
  intro = "import React from 'react'; const "
  mid = "= () => { return ( <div className='"
  end="'>name</div>);}; export default "
  react_content= intro + name + mid + name + end + name
  return react_content

def component_content_func(name):
  intro = "import React from 'react'; const "
  mid = "= (props) => { return ( <div className='"
  end="'>name</div>);}; export default "
  react_content= intro + name + mid + name + end + name
  return react_content

def style_content_func(name):
  style = "." + name + "{}"
  return style 

styles_content = ".Example{}"
component_content="import React from 'react'; const Example = () => { return ( <div className='Example'>Example</div>);};"

js_component_path = './components/'
js_page_path = './pages/'
styles_path = "./styles/"

user_page_input = "y"

# ----------------------------------------- Create component directory ----------------------------
print("Components path being made...")
if os.path.exists(component_path):
  print("Component path already exists.")
else:
  os.mkdir(component_path)

# ----------------------------------------- Create pages directory ----------------------------
print("Page path being made...")
if os.path.exists(page_path):
  print("Page path already exists.")
else:
  os.mkdir(page_path)

# ----------------------------------------- Create styles directory ----------------------------
print("Style path being made...")
if os.path.exists(styles_path):
  print("Style path already exists.")
else:
  os.mkdir(styles_path)

# ----------------------------------------- Create pages and styles ----------------------------
while user_page_input.lower() == "y" or user_page_input.lower() == "yes":
  user_page_input = input("Would you like to add a page?")
  if user_page_input.lower() == "y" or user_page_input.lower() == "yes":
    page_name = input("What is the page name?")
    print(f"Adding page and css for {page_name}...")
    page_file_dir = js_page_path + page_name + ".js"
    page_style_dir = styles_path + page_name + ".scss"
    styles_content = f".{page_name}" + "{}"
    writeToFile(page_file_dir, react_content_func(page_name))
    writeToFile(page_style_dir, style_content_func(page_name))
    styles = "import '../styles/" + page_name + ".scss'"
    with open('./pages/_app.js', 'r+') as file: 
        file_data = file.read() 
        file.seek(0, 0) 
        file.write(styles + '\n' + file_data) 

# ----------------------------------------- Create components and styles ----------------------------
user_component_input = "y"

while user_component_input.lower() == "y" or user_component_input.lower() == "yes":
  user_component_input = input("Would you like to add a component?")
  if user_component_input.lower() == "y" or user_component_input.lower() == "yes":
    component_name = input("What is the components name?")
    print(f"Adding page and css for {component_name}...")
    component_file_dir = js_component_path + component_name + ".js"
    component_style_dir = styles_path + page_name + ".scss"
    styles_content = f".{page_name}" + "{}"
    writeToFile(component_file_dir, component_content_func(page_name))
    writeToFile(component_style_dir, style_content_func(page_name))
    styles = "import '../styles/" + page_name + ".scss'"
    with open('./pages/_app.js', 'r+') as file: 
        file_data = file.read() 
        file.seek(0, 0) 
        file.write(styles + '\n' + file_data) 


