# Set the bootloader flag via rebootfromnand and reboot into Android
import os
import subprocess

import xbmc
import xbmcaddon
import xbmcgui

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
NAME = ADDON.getAddonInfo('name')
ICON = ADDON.getAddonInfo('icon')
NANDSCRIPT = '/usr/sbin/rebootfromnand'


def log(msg, level=xbmc.LOGINFO):
    xbmc.log('[{}] {}'.format(ADDON_ID, msg), level)


def notify_error(string_id):
    xbmcgui.Dialog().notification(NAME, ADDON.getLocalizedString(string_id), xbmcgui.NOTIFICATION_ERROR)


def main():
    if not os.access(NANDSCRIPT, os.X_OK):
        log('{} not found or not executable'.format(NANDSCRIPT), xbmc.LOGERROR)
        notify_error(30001)
        return

    if not xbmcgui.Dialog().yesno(NAME, ADDON.getLocalizedString(30000)):
        return

    try:
        result = subprocess.run([NANDSCRIPT], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as e:
        log('Failed to run {}: {}'.format(NANDSCRIPT, e), xbmc.LOGERROR)
        notify_error(30002)
        return

    if result.returncode != 0:
        log('{} exited with {}: {}'.format(NANDSCRIPT, result.returncode, result.stderr.strip()), xbmc.LOGERROR)
        notify_error(30003)
        return

    log('Boot flag set, rebooting to Android')
    xbmcgui.Dialog().notification(NAME, ADDON.getLocalizedString(30004), ICON)
    xbmc.Monitor().waitForAbort(0.5)
    xbmc.executebuiltin('Reboot')


if __name__ == '__main__':
    main()
