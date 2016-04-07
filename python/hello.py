# -*- coding: Shift_Jis -*-
import pymel.core as pm
import os

# 新規シーンファイルをつくる
pm.newFile()

# ポリゴンの球をつくる
pm.polySphere()

# シーンファイルを保存するファイルパスを指定する
pm.renameFile(os.getcwd() + '\\hello.ma')

# シーンファイルを保存する
pm.saveFile()