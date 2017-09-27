import httplib, urllib, base64

subscription_key = '4c9d869cdd3a4adba127a880088daac4'
# uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key':  subscription_key,
}

params = urllib.urlencode({
})

body = urllib.urlencode({
    "name": "sample_list",
    "userData": "User-provided data attached to the face list"
})

def createList():

    params = urllib.urlencode({
        'faceListId': 'abc1234abc1234'
    })

    try:
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("PUT", "/face/v1.0/facelists/{faceListId}?%s" % params, '{body}', headers)
        print "CACA"
        response = conn.getresponse()
        print response
        data = response.read()

        print "DATA:: "
        print data

        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.message, e.args))