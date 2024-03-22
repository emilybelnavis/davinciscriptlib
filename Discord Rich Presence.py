#!/usr/bin/env python3
import DaVinciResolveScript as dvr_script
from discordrp import Presence
import time
import sys, os

client_id = "1206320878992752711"

resolve = dvr_script.scriptapp("Resolve")
fusion = resolve.Fusion()
projectManager = resolve.GetProjectManager()


def main():
    start_time = int(time.time())
    with Presence(client_id) as presence:
        try:
            while True:
                project = projectManager.GetCurrentProject()
                projectName = project.GetName()
                current_time = int(time.time())
                
                isRendering = project.IsRenderingInProgress()
                if isRendering:
                    state = "Rendering"
                else:
                    state = "Editing"

                presence.set(
                    {
                        "state": f"{state}",
                        "details": f"Project: {projectName}",

                        "timestamps": {
                            "start": start_time
                        },
                        "assets": {
                            "large_image": "resolve",
                            "small_image": "resolve"
                        }
                    }
                )
                time.sleep(1)

        except KeyboardInterrupt:
            print("Interrupted by keyboard...")
            print("Exiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()