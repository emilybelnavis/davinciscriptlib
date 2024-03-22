# DaVinci Resolve Script Library

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