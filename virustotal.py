# Copyright (C) 2020-2021 by TeamSpeedo@Github, < https://github.com/TeamSpeedo >.
#
# This file is part of < https://github.com/TeamSpeedo/SpeedoUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamSpeedo/blob/master/LICENSE >
#
# All rights reserved.

import os
import time
import requests
from main_startup.core.decorators import speedo_on_cmd, Config
from main_startup.core.startup_helpers import run_cmd
from main_startup.helper_func.basic_helpers import (
    edit_or_reply,
    progress,
    edit_or_send_as_file,
    get_text,
)
vak = Config.V_T_KEY

@speedo_on_cmd(['vt', 'scan'],
               cmd_help={
                 "help": "Scan A File For Viruses. Needs Api Key From https://virustotal.com",
                 "example": "{ch}vt (Replying to File / Document)"
               })
async def scan_my_file(client, message):
    ms_ = await edit_or_reply(message, "`Please Wait! Scanning This File`")
    if not message.reply_to_message:
      return await ms_.edit("`Please Reply To File To Scan For Viruses`")
    if not message.reply_to_message.document:
      return await ms_.edit("`Please Reply To File To Scan For Viruses`")
    if not vak:
      return await ms_.edit("`You Need To Set VIRUSTOTAL_API_KEY For Functing Of This Plugin.`")
    if int(message.reply_to_message.document.file_size) > 25000000:
      return await ms_.edit("`File Too Large , Limit is 25 Mb`")
    c_time = time.time()
    downloaded_file_name = await message.reply_to_message.download(progress=progress, progress_args=(ms_, c_time, f"`Downloading This File!`"))
    url = "https://www.virustotal.com/vtapi/v2/file/scan"
    params = {"apikey": vak}
    files = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    response = requests.post(url, files=files, params=params)
    try:
       r_json = response.json()
       scanned_url = r_json["permalink"]
    except:
      return await ms_.edit(f"`[{response.status_code}] - Unable To Scan File.`")
    await ms_.edit(f"<b><u>Scanned {message.reply_to_message.document.file_name}</b></u>. <b>You Can Visit :</b> {scanned_url} <b>In 5-10 Min To See File Report</b>")
