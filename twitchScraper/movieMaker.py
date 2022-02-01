from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, concatenate_videoclips, vfx
import time

duration = []
titsContainer = []

def __check_duration(current_clip):
    global duration
    duration.append(int(current_clip.duration))

def __convert(timestamp):
    return time.strftime("%M:%S", time.gmtime(timestamp))

def __create_description(basePath):
    global duration
    global titsContainer
    dirDesc = basePath + "/FinalProduct/description.txt"
    desc = open(dirDesc, "w")
    desc.write("Description is needed. \n \n \n")
    desc.write("TIMELINE: \n")
    i = 0
    timestamp = 0
    for x in titsContainer:
        desc.write(x + ' (' + __convert(timestamp) +').\n')
        timestamp = timestamp + duration[i]
        i+=1

    desc.close()

def createVideo(basePath):
    
    dirIntro = basePath + "/temporaryVideos/intro/temp-intro.png"
    dirAd = basePath + "/temporaryVideos/advertisements/temp-ad.png"
    dirOutro = basePath + "/temporaryVideos/outro/temp-outro.png"
    dirClips = basePath + "/Links/directoryPaths.txt"
    dirFinal = basePath + "/FinalProduct/my_video.mp4"
    dirTempAudio = basePath + "/FinalProduct/temp-audio.m4a"
    dirReq = basePath + "/Links/formatedLinks.txt"

    with open(dirClips, "r") as f, open(dirReq, "r") as tits:
        global titsContainer
        clipContainer = [x.strip() for x in f.readlines()]
        for l in tits.readlines():
            if "Title: " in l:
                titsContainer.append(l.removeprefix('Title: ').strip())
        f.close()
        tits.close()

    clips = []

    img = ImageClip(dirIntro).set_duration(2)
    titsContainer.insert(0, "Intro")
    clips.append(img)
    __check_duration(img)
    for row in range(len(clipContainer)):
        if row % 2 == 0:
            clip = VideoFileClip(clipContainer[row+1])
            clip = clip.resize((1920, 1080))
            img = ImageClip(clipContainer[row]).set_duration(clip.duration)
            clip = CompositeVideoClip([clip, img])
            clips.append(clip)
            __check_duration(clip)
        else:
            pass
    
    img = ImageClip(dirOutro).set_duration(5)
    __check_duration(img)
    titsContainer.append("Outro")
    clips.append(img)
    img = ImageClip(dirAd).set_duration(5)
    global duration
    titsContainer.insert(4, "Advertisement")
    duration.insert(4, img.duration)
    clips.insert(4, img)

    __create_description(basePath)
    finalVideo = concatenate_videoclips(clips)
    finalVideo.write_videofile(dirFinal, temp_audiofile=dirTempAudio, remove_temp=True, codec="libx264", audio_codec="aac")

#createVideo()