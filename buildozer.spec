[app]

# (1) অ্যাপের নাম ও টাইটেল
title = Dhaka13 App
package.name = dhaka13
package.domain = org.tata

# (2) সোর্স ফাইল এবং এক্সটেনশন (সবচেয়ে জরুরি লাইন)
source.dir = .
source.include_exts = py,png,jpg,ui,db,ttf,zip

# (3) ভার্সন
version = 0.1

# (4) রিকোয়ারমেন্টস (PyQt6 এবং SQLite)
requirements = python3,pyqt6,sqlite3

# (5) অ্যাপ ওরিয়েন্টেশন (পোট্রেট মোড)
orientation = portrait
fullscreen = 0

# (6) আইকন
icon.filename = %(source.dir)s/icon.png

# (7) অ্যান্ড্রয়েড পারমিশন
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (8) অ্যান্ড্রয়েড টেকনিক্যাল কনফিগারেশন (API 33 - Android 13)
android.api = 33
android.minapi = 24
android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a

# (9) লোডিং স্ক্রিন কালার
android.presplash_color = #f0f8ff

[buildozer]

# (10) লগ লেভেল
log_level = 2
warn_on_root = 1
