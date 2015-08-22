import sys, json

with open(sys.argv[1]) as f:
    json_data = json.load(f)
    for articles in json_data["index"]["original"]["inv"].items():
        print ("%s" % articles[0].encode("utf-8"))
        for features in articles[1].items():
            print ("\t %s: %f" % (features[0].encode("utf-8"), float(features[1])))
            
