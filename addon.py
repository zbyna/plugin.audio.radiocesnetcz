import sys
import xbmc
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'songs')

radio = {}
radio['cro1radizurnal128'] = {
  'url':  'http://radio.cesnet.cz:8000/z-cro1.ogg',
  'li':   xbmcgui.ListItem('CRo Radiozurnal', iconImage='DefaultAudio.png')
}
radio['cro2dvojka128'] = {
  'url':  'http://radio.cesnet.cz:8000/z-cro2.ogg',
  'li':   xbmcgui.ListItem('CRo Dvojka', iconImage='DefaultAudio.png')
}
radio['cro3vltava128'] = {
  'url':  'http://radio.cesnet.cz:8000/z-cro3.ogg',
  'li':   xbmcgui.ListItem('CRo Vltava', iconImage='DefaultAudio.png')
}
radio['croplus128'] = {
  'url':  'http://radio.cesnet.cz:8000/cro-plus.ogg',
  'li':   xbmcgui.ListItem('CRo Plus/Jazz', iconImage='DefaultAudio.png')
}
radio['croradiojunior128'] = {
  'url':  'http://radio.cesnet.cz:8000/cro-radio-junior.ogg',
  'li':   xbmcgui.ListItem('CRo Radio Junior', iconImage='DefaultAudio.png')
}
radio['croradiowave128'] = {
  'url':  'http://radio.cesnet.cz:8000/cro-radio-wave.ogg',
  'li':   xbmcgui.ListItem('CRo Radio Wave', iconImage='DefaultAudio.png')
}
radio['croddur128'] = {
  'url':  'http://radio.cesnet.cz:8000/z-cro-d-dur.ogg',
  'li':   xbmcgui.ListItem('CRo D-dur', iconImage='DefaultAudio.png')
}
for key, value in radio.items():
  xbmcplugin.addDirectoryItem(handle=addon_handle, url=value['url'], listitem=value['li'])

xbmcplugin.endOfDirectory(addon_handle)
