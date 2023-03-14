import os


'''This is a quick and dirty script to delete the contents of my downloads folder
and my screenshots folder this could be extended in the future to include other 
directories that will need to be occasionaly cleaned out of the junk'''


screenshots = "/mnt/c/users/sross/My Documents/screenshots"
downloads = "/mnt/c/users/sross/Downloads"
desktop = "/mnt/c/users/sross/Desktop"
def cleanMe(path):

    for root, dirs, files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root,file))
        for dir in dirs:
            cleanMe(os.path.join(root, dir))
            os.rmdir(os.path.join(root,dir))


if __name__ == "__main__":
    cleanMe(screenshots)
    cleanMe(downloads)
    cleanMe(desktop)
