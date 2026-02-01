[app]
title = E-Calcul
package.name = ecalcul
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 4.0
requirements = python3,kivy==2.1.0
orientation = portrait

[android]
# ВАЖНО: должно совпадать с workflow!
android.sdk = 33
android.minapi = 21
android.target_api = 33
android.ndk = 25b
android.ndk_api = 21
android.arch = armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
