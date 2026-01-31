[app]
title = Мой калькулятор
package.name = mycalculator
package.domain = org.test  
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait


[android]
android.accept_sdk_license = True
android.minapi = 21
android.target_api = 34
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
