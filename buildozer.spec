[app]
title = Мой калькулятор
package.name = mycalculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.1.0,cython==0.29.33
orientation = portrait

[android]
android.accept_sdk_license = True
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.minapi = 21
android.target_api = 33
android.arch = armeabi-v7a
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0
