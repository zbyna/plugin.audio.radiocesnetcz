# -*- coding: utf-8 -*-

# Copyright (c) 2016 Vladimir Navrat
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. * See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St - Fifth Floor, Boston, MA 02110-1301 USA.

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import urllib2,urllib,re
import xbmcaddon

#import rpdb2 
#rpdb2.start_embedded_debugger('pw')

iconpath = os.path.join(xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'),'resources')

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'songs')
xbmcplugin.addSortMethod(addon_handle, 1) # SORT_METHOD_LABEL

url = 'http://radio.cesnet.cz/'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
httpdata = response.read()
link = response.read()
response.close()

lines = httpdata.split("\n")

station = ''

for line in lines:
    if line.startswith(' <td><strong>'):
        station = re.sub('&nbsp;','',re.sub('<[^<]+?>', '', line)).strip()
        #print station

    if line.startswith(' <td><a href="'):
        # print line
        streams = re.findall('http://[A-Za-z0-9-]*\.cesnet\.cz\:8000/.{1,30}\.m3u', line)
        codecs = re.findall('[1-9][0-9]{1,2}\ kb\/s\ ogg|FLAC', line)

        for i in range(0,streams.__len__()):
            color='000F37'
            #Radio�urn�l ED2E38
            if re.match('.*'+'Radio..urn..l'+'.*', station):
                color='ED2E38'
            #Dvojka 85248F
            if re.match('.*'+'Dvojka'+'.*', station):
                color='85248F'
            #Vltava 00B8E0
            if re.match('.*'+'Vltava'+'.*', station):
                color='00B8E0'
            #Plus DE7008
            if re.match('.*'+'Plus'+'.*', station):
                color='DE7008'
            #Radio Wave CDA200
            if re.match('.*'+'Wave'+'.*', station):
                color='CDA200'
            #Jazz 00809E
            if re.match('.*'+'Jazz'+'.*', station):
                color='00809E'
            #D-dur AB035C
            if re.match('.*'+'D-dur'+'.*', station):
                color='AB035C'
        
            item = xbmcgui.ListItem (station + ' | ' + codecs[i]) 
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=streams[i], listitem=xbmcgui.ListItem (station + ' | [I]' + codecs[i] + '[/I]' , iconImage=os.path.join(iconpath, color+'.png')))

xbmcplugin.endOfDirectory(addon_handle)
