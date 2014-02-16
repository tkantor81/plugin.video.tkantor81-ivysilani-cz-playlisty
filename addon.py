#    XBMC Plugin Add-on: iVysilani.cz - Playlisty
#    Copyright (C) 2014  tkantor81 (tkantor81@gmail.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

import sys
import urllib
import urlparse

ADDON_ID = 'plugin.video.tkantor81-ivysilani-cz-playlisty'
NOTIFY_DURATION = 5000


class ShowMode(object):
    LIST_EPISODES = 0
    PLAY_ALL = 1
    SHUFFLE_PLAY = 2


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

my_addon = xbmcaddon.Addon(ADDON_ID)
my_addon_name = my_addon.getAddonInfo('name')
my_addon_icon = my_addon.getAddonInfo('icon')
level = args.get('level', None)
xbmcplugin.setContent(addon_handle, 'movies')

if level is None:

elif level[0] == 'show':

xbmcplugin.endOfDirectory(addon_handle)