#!/usr/bin/env python3

import DaVinciResolveScript as dvr_script
import sys, os
from time import sleep


RESOLVE = dvr_script.scriptapp("Resolve")
FUSION = RESOLVE.Fusion()
PROJECT_MANAGER = RESOLVE.GetProjectManager()

# Get the Current Project and Project Name
PROJECT = PROJECT_MANAGER.GetCurrentProject()
PROJECT_NAME = PROJECT.GetName()

# Get the current media pool
MEDIA_POOL = PROJECT.GetMediaPool()

WORKING_MP_FOLDER = MEDIA_POOL.GetCurrentFolder()
WORKING_MP_FOLDER_NAME = WORKING_MP_FOLDER.GetName()

timelines = []


def get_timelines():
    # get the total number of timelines in the project
    timeline_count = PROJECT.GetTimelineCount()

    for i in range(1, timeline_count + 1):
        # Returns a given timeline in the range of 1 <= index <= PROJECT.GetTimelineCount() by design in the Resolve Scripting API
        timeline = PROJECT.GetTimelineByIndex(i)
        timeline_name = timeline.GetName()
        timelines.append(timeline_name)


def main():
    reels = WORKING_MP_FOLDER.GetSubFolders()
    all_clips = []
    circle_clips = []

    for key,value in reels.items():
        # temporarily change to the subfolder in the object array
        reel = MEDIA_POOL.SetCurrentFolder(value)

        # get the current folder and name
        reel = MEDIA_POOL.GetCurrentFolder()
        reel_id = reel.GetName()

        # get all the clips in the reel folder
        reel_clips = reel.GetClips()

        # check for circled clips
        for clip_key, clip_value in reel_clips.items():
            all_clips.append(clip_value)
            metadata = clip_value.GetClipProperty("Good Take")
            if (metadata == "1"):
                circle_clips.append(clip_value)

        # set the current working directory back to the working folder we had earlier
        MEDIA_POOL.SetCurrentFolder(WORKING_MP_FOLDER)

        reel_timeline_name = f"{WORKING_MP_FOLDER_NAME}_{reel_id}"

        # create a new timeline with the reel name

        # check if a timeline with `timeline_name` already exists
        
        if not reel_timeline_name in timelines:
            MEDIA_POOL.CreateTimelineFromClips(reel_timeline_name, reel_clips)
    
    # create timelines for dailies generation
    timeline_all = f"{WORKING_MP_FOLDER_NAME}_Daily_AllClips"
    timeline_circleonly = f"{WORKING_MP_FOLDER_NAME}_Daily_CircleOnly"

    if not timeline_all in timelines:
        MEDIA_POOL.CreateTimelineFromClips(timeline_all, all_clips)
    
    if not timeline_circleonly in timelines:
        MEDIA_POOL.CreateTimelineFromClips(timeline_circleonly, circle_clips)

if __name__ == "__main__":
    get_timelines()
    main()