#coding: UTF-8
import httplib, urllib, base64, json, cognitive_face

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '4c9d869cdd3a4adba127a880088daac4'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    #'returnFaceAttributes': 'age,gender,smile,facialHair,hair',
    #'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
})


# The URL of a JPEG image to analyze.
#body = "{'url':'https://scontent.fntr4-1.fna.fbcdn.net/v/t1.0-9/18010854_1893085790717078_2637128141764059535_n.jpg?oh=b709287b84055329b57da85c67121459&oe=5A84D1A9'}"

#try:
    # Execute the REST API call and get the response.
    #conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    #conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    #response = conn.getresponse()
    #data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    #parsed = json.loads(data)
    #print ("Response:")
    #print (json.dumps(parsed, sort_keys=True, indent=2))
    #conn.close()

#except Exception as e:
    #print("[Errno {0}] {1}".format(e.errno, e.strerror))


# Method for reading faces
def readFace(path, isURL):
    result = ''

    if isURL:
        headers['Content-Type'] = 'application/json'
        body = path
    else:
        headers['Content-Type'] = 'application/octet-stream'
        filename = path
        f = open(filename, "rb")
        body = f.read()

        f.close()

    try:
        # Execute the REST API call and get the response.
        conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        # print ("Response:")
        # print (json.dumps(parsed, sort_keys=True, indent=2))

        result = (json.dumps(parsed, sort_keys=True, indent=2))

        conn.close()

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return result

