#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:17:03 2020

@author: yuchangnan
"""

import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s','format':'137'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=wbGPmMDHUag',
        download=True # We just want to extract the info
    )