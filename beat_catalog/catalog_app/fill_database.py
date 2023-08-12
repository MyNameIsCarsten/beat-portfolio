import os
import re

def mp3_path(dir_path:str):
    # Store beats in list
    beat_list = []

    # For loop to iterate through current path
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            beat_list.append(file)
    return beat_list

def get_bpm_key (beat:str, folder_path:str):
    txt = beat

    # Get beat number
    w = re.search(r"\[.*\]", txt)
    number = w.group().strip()
    number = int(number[1:len(number)-1])
    txt = txt.replace(w.group(), "")

    # Get beat key
    x = re.search(r"\s.*(Minor|Major)", txt)
    key = x.group().strip()
    ## Name fix
    try:
        key = key.split("/")[1].strip()
    except:
        pass
    txt = txt.replace(x.group(), "")

    # Get beat bpm
    y = re.search(r".*BPM", txt.strip())
    bpm = y.group().strip().replace("BPM", "")
    txt = beat.split("\\")[-1]

    # Get beat name
    z = re.search(fr"(?<=BPM )(.*?)(?= \(Prod)", txt)
    name = z.group().strip()

    # Full beat path
    full_path = folder_path + '\\' + str(beat)

    return number, bpm, key, name, full_path

'''
folder_path = "D:\Dropbox\Beats\ProfessionalStuff\Beatstars\Female"
beat_list = mp3_path(folder_path)

for beat in beat_list:
    try:
        print(get_bpm_key(beat, folder_path))
    except:
        pass
'''