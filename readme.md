# DaVinci Resolve Script Library

![GitHub License](https://img.shields.io/github/license/emilybelnavis/davinciscriptlib)
![Static Badge](https://img.shields.io/badge/3.12%2B-blue?style=flat-square&label=python%20version)
[![wakatime](https://wakatime.com/badge/user/25fa80f6-0c6c-4e77-ad2c-9b37c3d81799/project/018e632a-d37a-4b15-a8dd-98032d223fda.svg?style=flat-square&color=green)](https://wakatime.com/badge/user/25fa80f6-0c6c-4e77-ad2c-9b37c3d81799/project/018e632a-d37a-4b15-a8dd-98032d223fda)

A collection of python scripts that streamline the workflow

## Script Collection

- `Discord Rich Presence.py`
    - This just adds rich presence to DaVinci Resolve

- `Create Proxy and Dailies Timelines - Single Cam.py` 
    - This creates and populates timelines for proxy and dailies generation. This assumes that your project structure looks like this:
    ```bash
     Master
     └── Block 1
         └── Shoot-Date_Day#
             └── AXXX
    ```

    You can have `N` number of nested "Block" folders with as many Reel (`AXXX`) folders inside of them.

    Run this script *after* selecting the bin/folder with the shoot day you're generating dailies and proxies for.



## Installation Instructions
Clone this repository
```bash
clone git@github.com:emilybelnavis/davinciscriptlib.git
```

Navigate to `~/Library/Application\ Support/Blackmagic\ Design/DaVinci\ Resolve/Fusion/Scripts/`. You should see a
series of folders like so

```bash
.
├── Color
├── Comp
├── Deliver
├── Edit
├── Tool
├── Utility
└── Views
```

Where you choose to install the scripts is up to the user. Navigate to any one of the folders above and run the
following command: `ln -s /path/to/script-repo/*.py .`. This will add an alias/symbolic link to the script folder. This
should make future updates easier to apply.