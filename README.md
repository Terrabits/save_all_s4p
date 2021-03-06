# Save All S4P

Saves all available S4P files from data already on the VNA.

To be safe, it also saves all trace data to csv and saves screenshots.

## Install

Copy `save_all_s4p.zip` onto the desktop of the VNA. Right-click the file and select `Extract all...`

![Right Click menu](doc/images/right-click-extract-all.png)

Set the extract location to the desktop.

![Extract path dialog](doc/images/extract-to-desktop-path.png)

The result should be a folder named `save_all_s4p` with the following contents:

![folder contents](doc/images/save-all-s4p-folder-contents.png)

## Run

Double-click `run.bat` to save all data on the VNA. Data is saved in the `data/` folder, organized by timestamp.

![Data folder example](doc/images/example-data.png)

## Set Continuous Sweep (Optional)

A side-effect of `save_all_s4p` is that continuous measurements are stopped so that consistent data is present before it is saved.

When using the VNA manually, you may want to restore `Continuous Sweep` mode by performing the following:

1.  Click the `Sweep` hard key
2.  Select the `Sweep Control` soft key (tab)
3.  Click the `All Channels Continuous` button to resume measurements
