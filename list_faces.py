import httplib, urllib, base64

subscription_key = '4c9d869cdd3a4adba127a880088daac4'
uri_base = 'westcentralus.api.cognitive.microsoft.com'
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key':  subscription_key,
}

params = urllib.urlencode({
})

def ListFaces(body):
    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("PUT", "/face/v1.0/facelists/{faceListId}?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return data