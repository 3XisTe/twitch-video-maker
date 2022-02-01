import random 

def orgFile(linkPath):
    fileRead = linkPath + "/Links/requestedLinks.txt"
    writedFile = linkPath + "/Links/formatedLinks.txt"
    with open(fileRead, "r") as f, open(writedFile, "w") as nf:
        
        container = f.readlines()
        f.close()
        container = [x.split("#|#") for x in container]

        random_choice = random.sample(container, 10)

        for everyLine in range(len(random_choice)):
            user, title, vLink, dLink = random_choice[everyLine] 
            nf.write("User: " + user + "\nTitle: " + title + "\nVideo_Link: " + vLink + "\nDownload_Link: " + dLink + '\n')
        nf.close()

#orgFile()