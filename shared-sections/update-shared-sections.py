import os
from bs4 import BeautifulSoup

#settings
isDebug = True
sourceFileName = 'index'
tagsToUpdate = ['nav','footer']        #contains a list of tags to be updated; contents is handled via object

#global vars
tagsToUpdateList = []
sourceFilePath = ""
workingDirectory = ""

class Tag:
    def __init__(self, tag, tagBody):
      self.tag = tag
      self.tagBody = tagBody

def getWorkingDir():
    global workingDirectory
    
    if workingDirectory != "":
       return workingDirectory
  
  #debug purposes
    if isDebug: 
       workingDirectory = r'E:\Users\PC\Documents\web-sites\st-website'
       return workingDirectory

    dir_path = input("Enter directory path: ")

    if not os.path.isdir(dir_path):
      print("Invalid directory path.")
    else:
      workingDirectory = dir_path
      return dir_path
    
def initTags():
   for tagToUpdate in tagsToUpdate:
      newTag = Tag(tagToUpdate,"")
      tagsToUpdateList.append(newTag)
      

def getFilesInDir(dirPath):
   return os.listdir(dirPath)

def isValidHTMLFile(filePath: str) -> bool:
  return filePath.lower().endswith(('.html', '.htm'))

def getFileNameForDebugOutput(filePath: str) -> str:
   fileName = getFileNameFromFilePath(filePath)
   debugFolderPath =  os.path.join(getWorkingDir(),"debug-tagUpdate-output")

   if not os.path.exists(debugFolderPath):
    os.makedirs(debugFolderPath)

   return os.path.join(debugFolderPath, fileName)


def getFileNameFromFilePath(filePath: str) -> str:
   return os.path.basename(filePath)

def getFileNameWithoutExtension(filePath: str) -> str:
   return os.path.splitext(os.path.basename(filePath))[0]

def getSourceFile(workingDir: str) -> str:
  global sourceFileName
  
  for fileName in getFilesInDir(workingDir):
     if getFileNameWithoutExtension(fileName) == sourceFileName:
        return os.path.join(getWorkingDir(),fileName)
     
def updateTagListWithContentFromSourceFile(sourceFilePath: str):
  global tagsToUpdateList

  if len(tagsToUpdate) == 0:
    print('no tags listed for update')
    return

  file = open(sourceFilePath, 'r', encoding="utf-8")
  fileContents = file.read()

  for tag in tagsToUpdateList:
    htmlSoup = BeautifulSoup(fileContents, 'html.parser')
    tag.contents = htmlSoup.find(tag.tag)

  file.close()

def isValidFileToUpdate(filePath: str) -> bool:
   global sourceFilePath
   return isValidHTMLFile(filePath) and filePath != sourceFilePath

def updateTagsInFile(filePath: str):
  global tagsToUpdateList
  global isDebug

  # CHECK CONDITIONS #
  if len(tagsToUpdateList) == 0:
      print('tag list is empty. something wrong')
      return
   
  if filePath == "":
      print('file to be updated was not provided.')
      return
   
   # Open the HTML file and read its contents
  file = open(filePath, 'r', encoding="utf-8")
  fileContents = file.read()
  file.close()

  # Use BeautifulSoup to parse the HTML and find the navigation element
  soup = BeautifulSoup(fileContents, 'html.parser')

  # Update each tag that is listed for an update
  for tag in tagsToUpdateList:
    tagRef = soup.find(tag.tag)
    if tagRef != None:
      tagRef.replace_with(tag.contents)
    #tagRef.contents = BeautifulSoup(tag.contents, 'html.parser').contents

  # Save the updated HTML to a file
  if isDebug:
     filePath = getFileNameForDebugOutput(filePath)

  file = open(filePath, 'w', encoding="utf-8")
  file.write(str(soup))
  file.close
   


def updateFilesWithNewTags(workingDir: str):
   filesInDir = getFilesInDir(workingDir)

   for file in filesInDir:
      if isValidFileToUpdate(file):
         updateTagsInFile(file)

def main():
  global sourceFilePath
  workingDir = getWorkingDir()
  sourceFilePath = getSourceFile(workingDir)
  initTags()
  updateTagListWithContentFromSourceFile(sourceFilePath)
  updateFilesWithNewTags(workingDir)

main()