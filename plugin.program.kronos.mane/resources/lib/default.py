#twentytw93-KronosTeam
import os
import sys
import urllib.parse
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
import xbmcplugin

from mane import (
    clear_thumbnails,
    clear_cache,
    clear_packages,
    clear_textures,
    clear_all,
)

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_ID = ADDON.getAddonInfo('id')


def router():
    args = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
    action = args.get("action")

    if action == "clear_thumbnails":
        if xbmcgui.Dialog().yesno(ADDON_NAME, "Clear the thumbnails folder?"):
            clear_thumbnails()
    elif action == "clear_cache":
        if xbmcgui.Dialog().yesno(ADDON_NAME, "Clear the cache folder?"):
            clear_cache()
    elif action == "clear_packages":
        if xbmcgui.Dialog().yesno(ADDON_NAME, "Clear the packages folder?"):
            clear_packages()
    elif action == "clear_textures":
        clear_textures()
    elif action == "clear_all":
        if xbmcgui.Dialog().yesno(ADDON_NAME, "Clear all cache, packages, and textures?"):
            clear_all()
    else:
        build_main_menu()


def build_main_menu():
    items = [
        ("[B]Clear Thumbnails[/B]", "clear_thumbnails", "thumbnails.png"),
        ("[B]Clear Cache[/B]", "clear_cache", "cache.png"),
        ("[B]Clear Packages[/B]", "clear_packages", "packages.png"),
        ("[B]Clear Textures[/B]", "clear_textures", "textures.png"),
        ("[B]Clear All[/B]", "clear_all", "all.png"),
    ]

    fanart_path = os.path.join(ADDON.getAddonInfo('path'), "resources", "media", "kronos_mane.jpg")

    for label, action, icon in items:
        url = f"plugin://{ADDON_ID}/?action={action}"
        listitem = xbmcgui.ListItem(label)
        icon_path = os.path.join(ADDON.getAddonInfo('path'), "resources", "media", icon)
        listitem.setArt({
            "thumb": icon_path,   # Square menu icon
            "icon": icon_path,    # Generic icon fallback
            "poster": icon_path,  # Skin compatibility
            "fanart": fanart_path # Full background
        })
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=listitem, isFolder=False)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))

# ----------------------- MAIN -----------------------

if __name__ == "__main__":
    router()