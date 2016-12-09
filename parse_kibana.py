with open('test_results.json', 'r') as myfile:
    data=myfile.read().replace('\n', '')

res=data.split(",")
grade = [k for k in res if 'grade' in k]

if any("FAIL" in s for s in grade):
    raise Exception("At least a test has failed")
    print "Failed"
else:
    print "Everything is Ok"