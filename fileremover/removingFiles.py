import os
import shutil
import time
def main():
	# replace your folder's path here
	path = "C:/Users/Owner/Desktop/filestoberemoved"
	seconds = time.time() - (30*24*60*60)
	if os.path.exists(path):
		for folder, folders, files in os.walk(path):
			if (seconds >= age(folder)):
				removefolder(folder)			
				break
			else:
				for folder in folders:
					folderpath = os.path.join(folder, folder)					
					if (seconds >= age(folderpath)):						
						removefolder(folderpath)
				for file in files:
					filepath = os.path.join(folder, file)
					if (seconds >= age(filepath)):
						removefile(filepath)					
		else:
			if(seconds<age(path)):
				print("time left to delete it")
			if (seconds >= age(path)):
				removefile(path)
	else:
		print("-----"+path+' is not found')
def removefolder(path):
	if (not shutil.rmtree(path)):
		print("-----"+path+" is removed successfully")
	else:
		print("Unable to delete the "+path)
def removefile(path):
	if (not os.remove(path)):
		print("-----"+path+' is removed succesfully')
	else:
		print("Unable to delete the "+path)
def age(path):
	time = os.stat(path).st_atime
	return time
if (__name__ == '__main__'):
	main()