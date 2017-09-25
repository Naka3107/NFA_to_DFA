import cognitive_face as CF

KEY = '4c9d869cdd3a4adba127a880088daac4' # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print result