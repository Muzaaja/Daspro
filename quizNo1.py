"""Nama : Muhammad Zaidan Rahman
Kelas : 1B
NIM : 2404903"""

Pdinding = 1000
Ldinding = 2000
Tdinding = 800

Meter = 100
Harga = 450000

PdindingMeter = int(Pdinding/Meter)
LdindingMeter = int(Ldinding/Meter)
TdindingMeter = int(Tdinding/Meter)
Luasdinding = int(2 * PdindingMeter * TdindingMeter + 2 * LdindingMeter * TdindingMeter)
Operasi = int(Luasdinding * Harga)
print(Operasi)