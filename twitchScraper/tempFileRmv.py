from pathlib import Path

def fileRemoval(basePath):
    pathList = [basePath + '/Links', 
                basePath + '/templatePictures', 
                basePath + '/temporaryVideos']

    for x in pathList:
        [f.unlink() for f in Path(x).glob("*") if f.is_file()]

#fileRemoval()