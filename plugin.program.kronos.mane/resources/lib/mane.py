#twentytw93-KronosTeam
import os
import shutil
import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')

THUMBNAILS_PATH = os.path.join(xbmcvfs.translatePath("special://userdata/"), "Thumbnails")
CACHE_PATH = xbmcvfs.translatePath("special://temp/")
PACKAGES_PATH = xbmcvfs.translatePath("special://home/addons/packages/")
TEXTURES_PATH = os.path.join(xbmcvfs.translatePath("special://database/"), "Textures13.db")

def clear_thumbnails():
    if os.path.exists(THUMBNAILS_PATH):
        try:
            shutil.rmtree(THUMBNAILS_PATH)
            os.makedirs(THUMBNAILS_PATH)
            xbmcgui.Dialog().ok(ADDON_NAME, "Thumbnails folder cleared successfully!")
        except Exception as e:
            xbmcgui.Dialog().ok(ADDON_NAME, f"Failed to clear thumbnails: {str(e)}")
    else:
        xbmcgui.Dialog().ok(ADDON_NAME, "Thumbnails folder not found!")

def clear_cache():
    if os.path.exists(CACHE_PATH):
        try:
            for root, dirs, files in os.walk(CACHE_PATH, topdown=False):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception:
                        pass
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir))
                    except Exception:
                        pass
            xbmcgui.Dialog().ok(ADDON_NAME, "Cache folder cleared successfully!")
        except Exception as e:
            xbmcgui.Dialog().ok(ADDON_NAME, f"Failed to clear cache: {str(e)}")
    else:
        xbmcgui.Dialog().ok(ADDON_NAME, "Cache folder not found!")

def clear_packages():
    if os.path.exists(PACKAGES_PATH):
        try:
            for root, dirs, files in os.walk(PACKAGES_PATH, topdown=False):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception:
                        pass
                for dir in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, dir))
                    except Exception:
                        pass
            xbmcgui.Dialog().ok(ADDON_NAME, "Packages folder cleared successfully!")
        except Exception as e:
            xbmcgui.Dialog().ok(ADDON_NAME, f"Failed to clear packages: {str(e)}")
    else:
        xbmcgui.Dialog().ok(ADDON_NAME, "Packages folder not found!")

def clear_textures():
    if os.path.exists(TEXTURES_PATH):
        try:
            if xbmcgui.Dialog().yesno(ADDON_NAME, "Clear the textures database? This removes cached images for skins and add-ons."):
                os.remove(TEXTURES_PATH)
                xbmcgui.Dialog().ok(ADDON_NAME, "Textures database cleared successfully!")
        except Exception as e:
            if "being used by another process" in str(e):
                xbmcgui.Dialog().ok(ADDON_NAME, "Failed: Kodi is using the file. Please close Kodi and try again.")
            else:
                xbmcgui.Dialog().ok(ADDON_NAME, f"Failed to clear textures: {str(e)}")
    else:
        xbmcgui.Dialog().ok(ADDON_NAME, "Textures database not found!")

def clear_all():
    clear_thumbnails()
    clear_cache()
    clear_packages()
    clear_textures()