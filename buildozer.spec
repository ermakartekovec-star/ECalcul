[app]
title = E-Calcul
package.name = ecalcul
package.domain = org.ecalcul
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.0
requirements = python3,kivy==2.1.0
orientation = portrait
fullscreen = 0

[android]
# SDK
android.sdk = 33
android.minapi = 21
android.target_api = 33
android.ndk = 25b
android.ndk_api = 21

# Архитектура
android.arch = armeabi-v7a

# Подпись (debug)
android.accept_sdk_license = True

# Разрешения
android.permissions = INTERNET

# Иконка (можно добавить позже)
# icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 0
