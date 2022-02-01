import requests
from PIL import Image, ImageDraw, ImageFont

def downloadAssets(linkPath):

    elementID = 0
    fileRead = linkPath + "/Links/formatedLinks.txt"
    fileWrite = linkPath + "/Links/directoryPaths.txt"
    with open(fileRead, "r") as f, open(fileWrite, "w") as dirPaths:

        for x in f.readlines():

            control = []
            
            if "User:" in x:
                userNick = x.split(' ', 1)[1]
                userNick = userNick.strip()
                control.append(userNick)
                imageDir = linkPath + "/templatePictures/" + userNick + str(elementID) + ".png"
                dirPaths.write(imageDir + '\n')

                with Image.open(linkPath + "/templatePictures/main-template/twitch-banner-username.png") as template:
                    draw = ImageDraw.Draw(template)
                    fontsize = 1
                    textWindow = Image.new('RGB', (250, 36))
                    font = ImageFont.truetype(linkPath + "/templatePictures/main-template/main-font.ttf", fontsize)
                    
                    while (font.getsize(userNick)[0] < textWindow.size[0]) and (font.getsize(userNick)[1] < textWindow.size[1]):
                        fontsize += 1
                        font = ImageFont.truetype(linkPath + "/templatePictures/main-template/main-font.ttf", fontsize)
                    
                    W = template.size[0]
                    w = draw.textsize(userNick, font=font)[0]
                    draw.text((((W-w)/2)-5, 10), userNick, (255,255,255), font = font)
                    template.save(imageDir)

            elif "Download_Link:" in x:

                videoLink = x.split(' ', 1)[1]
                #print (videoLink)
                video_resp = requests.get(videoLink, stream = True)
                print (video_resp)
                vidDirectory = linkPath + "/temporaryVideos/" + userNick + str(elementID) + ".mp4"
                dirPaths.write(vidDirectory + '\n')
                elementID += 1

                with open(vidDirectory, "wb") as vid:
                    vid.write(video_resp.content)

        f.close()
        dirPaths.close()

downloadAssets()