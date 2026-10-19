# Reboot to Android (script.reboottoandroid)

Kodi add-on that reboots a CoreELEC box on Amlogic hardware into the Android
system installed in its internal storage (eMMC/NAND).

## Requirements

- Amlogic device running CoreELEC, with Android still installed in internal storage
- Kodi 19 (Matrix) or newer
- `/usr/sbin/rebootfromnand`, which ships with CoreELEC

## Installation

1. Download `script.reboottoandroid-<version>.zip` from the
   [Releases](https://github.com/CE-Repo/script.reboottoandroid/releases) page.
   Don't use GitHub's "Download ZIP" button: the folder inside that archive is
   named `script.reboottoandroid-main`, which doesn't match the add-on ID.
2. In Kodi, enable *Settings → System → Add-ons → Unknown sources*.
3. Go to *Settings → Add-ons → Install from zip file* and pick the downloaded zip.

## Usage

Start *Add-ons → Program add-ons → Reboot to Android* and confirm the dialog.
The add-on runs `rebootfromnand` to set the bootloader flag and only reboots
if that succeeded.

### Favourites

Open the context menu on the add-on and choose *Add to favourites*.

### Keymap

To start it with a key, create `/storage/.kodi/userdata/keymaps/reboottoandroid.xml`:

```xml
<keymap>
  <global>
    <keyboard>
      <f12>RunScript(script.reboottoandroid)</f12>
    </keyboard>
  </global>
</keymap>
```

Replace `<keyboard>`/`<f12>` with the button of your remote as needed.

## Troubleshooting

Errors are written to the Kodi log (`/storage/.kodi/temp/kodi.log`) with the
prefix `[script.reboottoandroid]`.

## Releasing

1. Bump `version` and update `<news>` in `addon.xml`.
2. Tag the commit as `v<version>` (e.g. `v1.1.0`) and push the tag.

The release workflow builds an installable zip with the correct folder name
and attaches it to a GitHub release.

## License

[MIT](LICENSE)
