#!/usr/bin/env python3

import os

def writeToFile(path, content):
  file = open(path, "w")
  file.write(content)
  file.close()

# ----------------------------------------- Set according to directory - var ----------------------------
current_path = (r"Z:\programming\generate-next-code")

component_folder = "components"
page_folder = "pages"
styles_folder = "styles"
public_folder = "public"

component_directory = os.path.join(current_path, component_folder)
page_directory = os.path.join(current_path, page_folder)
styles_directory = os.path.join(current_path, styles_folder)
public_directory = os.path.join(current_path, public_folder)


  
def create_components(page_name, component_name):
  component_file_path = f"{component_directory}/{page_name}/{component_name}.js"
  component_content = 'import React from "react"; const ' + component_name + ' = () => { return <div className=" ' + component_name  + '">' + component_name  + '</div>; }; '
  if os.path.exists(component_file_path):
    print("This component already exists")
  else:
    os.mkdir(f"{component_directory}/{page_name}")
    writeToFile(component_file_path, component_content)
    
def create_pages( page_name):
  page_file_path = f"{page_directory}/{page_name}.js"
  page_content = 'import React from "react"; const ' + page_name + ' = () => { return <div className=" ' + page_name  + '">' + page_name  + '</div>; }; '
  if os.path.exists(page_file_path):
    print("This page already exists")
  else:
    if os.path.exists(page_directory):
      print("This page already exists")
    else:
      os.mkdir(page_directory)
    writeToFile(page_file_path, page_content)


# create_components("Home", "HomePreview")
# create_pages("Home")


# components folder, file, and Style
# pages folder file, and style
# if package json isn't there, create it with next - react - react dom - next 
# make a public folder and images folder if not there 
# make globals css if not there
# make app and index if not there
# everytime style is added, import it to app
# use page name, for components folder
