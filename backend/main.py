import json
import yt_dlp
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/playlists")
async def get_playlists(playlist_url: Union[str, None] = None):
  ydl_opts = {}
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)
    data = ydl.sanitize_info(info)
  return {"URL": data}
