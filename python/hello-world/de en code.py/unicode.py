#unicode是內建<不用import
import base64
unicode = b'\u0042\u0072\u0065\u0061\u006b\u0041\u004c\u004c\u0043\u0054\u0046\u007b\u006d\u0079\u005f\u0066\u0069\u0072\u0073\u0074\u005f\u0055\u006e\u0069\u0043\u0030\u0064\u0065\u005f\u0033\u004f\u005f\u0045\u0061\u0073\u0079\u007d'
x = unicode.decode("unicode_escape")
print(x)

print("==============================")

input = input("輸入 UINCODE:")
s = unicode.decode('UTF-8')
y = unicode.decode("unicode_escape")
print(y)
