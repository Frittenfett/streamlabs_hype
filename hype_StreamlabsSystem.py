# ---------------------------------------
#   Import Libraries
# ---------------------------------------
import json
import codecs
import re
import os
import clr

clr.AddReference("IronPython.Modules.dll")
import urllib
import random

# ---------------------------------------
#   [Required]  Script Information
# ---------------------------------------
ScriptName = "Hype"
Website = "https://www.twitch.tv/frittenfettsenpai"
Description = "Hype for everyone."
Creator = "frittenfettsenpai"
Version = "1.0.0"


# ---------------------------------------
#   [Required] Intialize Data (Only called on Load)
# ---------------------------------------
def Init():
    global settings
    settingsfile = os.path.join(os.path.dirname(__file__), "settings.json")

    try:
        with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
            settings = json.load(f, encoding="utf-8")
    except:
        settings = {
            "command": "!hype",
            "emotes": "fritteHype, PikaWan, MarioPls, WowPls, CuteDog, RareParrot",
        }
    return


# ---------------------------------------
#   [Required] Execute Data / Process Messages
# ---------------------------------------
def Execute(data):
    global settings
    if data.IsChatMessage():
        if (data.GetParam(0).lower() == settings["command"]):
            emotes = settings["emotes"].split(",")
            content = "Hype !! "
            for emote in emotes:
                randomCount = random.randint(2, 10)
                i = 0
                while i < randomCount:
                    content = content + emote + " "
                    i = i + 1
            Parent.SendTwitchMessage(content)
    return


# ---------------------------------------
#    [Required] Tick Function
# ---------------------------------------
def Tick():
    return