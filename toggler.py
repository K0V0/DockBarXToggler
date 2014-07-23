#!/usr/bin/python

import gtk
import pygtk
pygtk.require('2.0')
import os
import gconf
from dockbarx.applets import DockXApplet

GCONF_MY_DIR = '/apps/dockbarx/dock/'
GCONF_VALUE_NAME = 'behavior'
GCONF_HIDDEN_VAL = 'always autohide'
GCONF_PANEL_VAL = 'panel'
GCONF_NORMAL_VAL = 'standard'
GCONF_DODGE_VAL = 'dodge windows'
GCONF_DODGE_ACTIVE_VAL = 'dodge active window'
BUBBLE_HIDE = '\'DockBarX autohide ON\' \'Dock will be shown only on mouse hover\''
BUBBLE_SHOW = '\'DockBarX always visible\' \'Use this applet to toggle it into autohide mode again\''
BUBBLE_ICON = '/usr/share/icons/hicolor/128x128/apps/dockbarx.png'

gclient = gconf.client_get_default()
gvalue = gconf.Value(gconf.VALUE_STRING)

class KovoApplet(DockXApplet):

    def __init__(self, dbx_dict):
        DockXApplet.__init__(self, dbx_dict)
        widget_size = self.get_size()
        state = self.get_state()
        self.connect("clicked", self.on_clicked)
        self.ikon = gtk.Image()
        self.visible_image = self.prepare_pixbuf('toggler-gfx/visible.png', widget_size)
        self.novisible_image = self.prepare_pixbuf('toggler-gfx/novisible.png', widget_size)
        self.render_ikon(state)
        self.show()

    def get_state(self):
        val = gclient.get(GCONF_MY_DIR+GCONF_VALUE_NAME).get_string()
        if val == GCONF_NORMAL_VAL or val == GCONF_PANEL_VAL or val == GCONF_DODGE_VAL or val == GCONF_DODGE_ACTIVE_VAL:
            return val
        elif val == GCONF_HIDDEN_VAL:
            return 0

    def render_ikon(self, stav):
        if stav == 0:
            self.ikon.set_from_pixbuf(self.visible_image)
        else:
            self.ikon.set_from_pixbuf(self.novisible_image)
        self.add(self.ikon)
        self.ikon.show()

    def on_clicked(self, widget, event):
        val = self.get_state()
        if event.button == 1:
            prev_val = ""
            val = self.get_state()
            if val != 0:
                prev_val = val
                next_val = GCONF_HIDDEN_VAL
                alert = BUBBLE_HIDE
            else: 
                next_val = GCONF_NORMAL_VAL if prev_val == "" else prev_val 
                alert = BUBBLE_SHOW
            self.render_ikon(0 if next_val == GCONF_HIDDEN_VAL else 1)
            os.system("notify-send " + alert + " -i " + BUBBLE_ICON)
            gvalue.set_string(next_val)
            gclient.set(GCONF_MY_DIR+GCONF_VALUE_NAME, gvalue)

    def get_resource_path(self, rel_path):
        dir_of_py_file = os.path.dirname(__file__)
        rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
        abs_path_to_resource = os.path.abspath(rel_path_to_resource)
        return abs_path_to_resource

    def prepare_pixbuf(self, img_path, img_size):
         pixbuf = gtk.gdk.pixbuf_new_from_file(self.get_resource_path(img_path))
         pixbuf = pixbuf.scale_simple(img_size, img_size, gtk.gdk.INTERP_BILINEAR)
         return pixbuf

def get_dbx_applet(dbx_dict):
    applet = KovoApplet(dbx_dict)
    return applet
