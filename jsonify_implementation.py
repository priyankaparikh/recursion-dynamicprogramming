# implement jsonify
# key is always a string
# values can be a string , integer or another dictionary

def json(d):
    """ returns a stringified version of the dictionary"""

    s = "{"

    for k in d:

        #base case is if the dictionary is empty return a stignified
        #version of the dictionary
        if type(d[k]) in (int, float, str):
            s += str(k) + ":" + str(d[k]) + ", "
        elif type(d[k]) is dict:
            s += str(k) + ":" + str(json(d[k])) + ", "
        elif type(d[k]) is list:
            s += str(k) + ":" + ",".join[json(item) for item in d[k] + ", "]
    s += "}"
    print s


a = { "1": 4, "hello" : "pic", "io":{"134": "50", 80 : 120, "youtube" : "hello"} }
json(a)
