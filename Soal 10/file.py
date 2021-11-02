# Nama : Alwizain Almas Trigreisian
# NPM : 1194004
# Kelas : D4 TI / 3A
# 1194004 mod 8 = 4, maka saya membuat jajargenjang dan karena angka terakhir npm saya 4 maka saya membuat 4 buah jajargenjang

import shapefile

w = shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType


w.field("kolom1", "C")
w.field("kolom2", "C")

w.record("sat", "satu")
w.record("set", "dua")
w.record("wat", "tiga")
w.record("wet", "empat")


w.poly([[[1, 2], [2, 5], [7, 5], [6, 2], [1, 2]]])
w.poly([[[2, 6], [3, 9], [8, 9], [7, 6], [2, 6]]])
w.poly([[[9, 2], [10, 5], [15, 5], [14, 2], [9, 2]]])
w.poly([[[10, 6], [11, 9], [16, 9], [15, 6], [10, 6]]])

w.close()