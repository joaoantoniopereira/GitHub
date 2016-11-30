import xml.etree.ElementTree as ET
file = ET.parse('robot_results.xml')
name = file.findall('suites/entry/suite/caseResults/entry')
case = file.findall('suites/entry/suite/caseResults/entry/case')

passed_failed, start, end, test_name = ([] for i in range(4))

for c, n in zip(case, name):
    passed_failed.append(c.find('passed').text)
    start.append(c.find('starttime').text)
    end.append(c.find('endtime').text)
    #errorM = c.find('errorMsg').text
    test_name.append(n.find('string').text)

with open('parsed_robot_report.csv', 'wb') as fp:
    fp.write("{},{},{},{}\n".format("title", "passed/failed", "start_time", "end_time"))
    for ax, bx, cx, dx in zip(test_name[:], passed_failed[:], start[:], end[:]):
        fp.write("{},{},{},{}\n".format(ax, bx, cx, dx))