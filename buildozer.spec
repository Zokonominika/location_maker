[app]

# (str) Title of your application
title = Kıble Gösterici

# (str) Package name
package.name = kiblegosterici

# (str) Package domain (needed for android/ios packaging)
package.domain = org.caner

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,plyer

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#
# (str) python macos ext
osx.python_version = 3
# (str) Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#
# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET
# (For magnetometer compassion access on Android, usually no extra specific permission is strictly required by plyer compass besides basic ones, but we keep it minimal)

# (int) Target Android API, should be as high as possible.
android.api = 33

# (bool) Automatically accept SDK license agreements.
android.accept_sdk_license = True

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK architecture (armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backups feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk or aar).
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
