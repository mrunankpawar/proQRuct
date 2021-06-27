import qrcode

img = qrcode.make("BLACK SALT POWDER"
"INGREDIENTS : BLACK SALT"
"Description:"
"Black Salt Powder (All natural, Sulphur-Rich, Kala Namak)"
"* In accordance with Ayurveda black salt or kala namak a cooling salt"
"and loaded with incredible therapeutic advantages."
"* Ttis used exclusively in making chat items, garnishing salads, making"
"marinades and as an essential part of many ethnic Indian beverages."
"INSTRUCTION FOR STORAGE : DO NOT BRING A WET SPOON IN"
"CONTACT WITH THE POWDER."
"ALWAYS STORE IN AIR TIGHT CONTAINER IN A COOL, DRY PLACE,"
"AWAY FROM DIRECT SUNLIGHT.")
img.save("saltQR.jpg")

import cv2
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("saltQR.jpg"))
print(val)
