# İkinci Dereceden Denklem Çözücü

## Açıklama

Bu proje, verilen katsayılara göre ikinci dereceden bir denklemin gerçek köklerini bulan bir Python modülüdür.

## Kurulum ve Kullanım

Bu proje yalnızca Python standart kütüphanesini kullanır; ek bir kurulum adımı gerekmez.

```python
from mystery_module import find_roots

kokler = find_roots(1, -3, 2)
print(kokler)  # (2.0, 1.0)
```

`ax^2 + bx + c = 0` biçimindeki bir denklem için `a`, `b` ve `c` katsayılarını `find_roots` fonksiyonuna verin. Denklemin gerçek kökü yoksa fonksiyon `None` döndürür.
