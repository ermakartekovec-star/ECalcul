[app]
title = Мой калькулятор
package.name = mycalculator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.1.0
orientation = portrait

[android]
# Версия SDK (ИЗМЕНИТЕ НА 33!)
android.sdk = 33
android.minapi = 21
android.target_api = 33
android.arch = armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
