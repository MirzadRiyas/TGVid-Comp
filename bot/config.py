#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", "17124006")
    API_HASH = config("API_HASH", "97e184dc9c07513de148002859aef2b2")
    BOT_TOKEN = config("BOT_TOKEN", "5301928162:AAEmDl0Au1z8IQkncjDsmojAO7akB8Mj9Qg")
    DEV = 1165699179
    OWNER = config("OWNER", "1165699179")
    ffmpegcode = ["-preset slow -c:v libx264 -s 1280x720 -x264-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By @PokeTide (https://t.me/PokeTide)' -pix_fmt yuv420p -crf 26 -c:a libopus -b:a 64k -c:s copy -map 0 -ac 2 -ab 64k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/96a8e440ca77fbf5b4c67.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
