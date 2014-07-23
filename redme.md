DockBarXToggler
===============

DockBarXToggler is applet for use with DockBarX, one of the best and most lightweight launcher/docking apps for linux. 

Functions/features
------------------

Current version of DockBarX can run in 5 modes of behavior:
	- panel: windows (also maximized) cannot overlay space where panel is. Cons: reduced screen size, ugly look, for example black texteditor window and light background in night results in distraction.
	- standart: panel is always visible and overlays windows. Cons: sometimes it can cover controls of app that you are using and you are unable to click it
	- dodge windows: when at least one maximized window is situated on desktop, panel will hide
	- dodge active window: same as dodge window, plus will hide only when maximized window is active. Cons: Some windows does not reports its state, this feature is working mostly randomly.
	- always autohide: self explanatory. Cons: extra time to take some action, mouse out causes to hide panel immediatelly. When drunk and mouse set to 2000 dpi, it's better to forget that icons and use keyboard shortcuts. Due to zero delay of mouse out I find this mode most unsuitable for use, specially on old tablet notebooks (the IBM or HP ones with stylus and pressure sensitivity, not touch) 

This applet gives you more control over your dock. It has only one function: toggling between first four modes (panel, standart, dodge windows, dodge active window) and last one (always autohide). If "autohide" is your default mode, then "standart" mode is used for toggling.

Installation
------------

Just unpack downloaded archive into (create folder(s) if not exists):

```/home/YOURuserNAME/.dockbarx/applets```
or
```/usr/share/dockbarx/applets```

then rerun dockbarx (alt+F2 -> run dialog):

```killall dockx```
then
```dockx```

applet should appear at the 2nd tab "dock applets" in right column. Just add it to left.

If icons are ugly just change them to whatever you want, they are located in toggler-gfx folder

Screenshots
-----------

![Problem explanation here](/../screenshits/screenshots/2.png?raw=true "Overlaying problem")

Notes
-----

This software is protected by spaghetti monster. If want to download, modify or redistribute or fork this original piece you have to pay me 1 000 000 000 000 000 €. If you order it today, you will have discount price only 999 999 999 999 999 €.
