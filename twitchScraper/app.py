import twitchLinker
import linkOrganiser
import assetDownload
import movieMaker
import tempFileRmv
import pathlib

currentPath = str(pathlib.Path().resolve())
twitchLinker.setValues(1, '7d')
print("Loading contents it may take a while. Please wait.")
twitchLinker.enterWeb()
print("Finding links finished, saving progres.")
twitchLinker.saveLinks(currentPath)
print("Links saved.\n")
print ("Organising links:")
linkOrganiser.orgFile(currentPath)
print ("Downloading assets it may take a while. Please wait.")
assetDownload.downloadAssets()
print ("Starting to prepare movie: ")
movieMaker.createVideo(currentPath)
print ("Finished creating video.\nWould you like to delete temprorary files? Y/n \n(you won't be able to download next video compilation until you delete them manually...)")
if input() == "Y":
    tempFileRmv.fileRemoval(currentPath)
elif input() == "n":
    print ("Remember to remove files manually, thanks for using our software.")