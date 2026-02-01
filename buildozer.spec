[app]
title = E-Calcul
package.name = ecalcul
package.domain = com.ecalcul
source.dir = .
version = 1.0
requirements = python3,kivy==2.0.0  # Более стабильная версия!
orientation = portrait

[android]
# ТОЛЬКО ОСНОВНЫЕ НАСТРОЙКИ
android.minapi = 21
android.ndk = 19c  # Старая стабильная версия!
android.sdk = 28   # Стабильный API
android.arch = armeabi-v7a

[buildozer]
log_level = 2
