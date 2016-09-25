from sys import argv
import itertools


script, filename = argv

def count_plugin():
    success_count = 0
    fail_count = 0
    f = open(filename)
    vip_string = ".vip: "
    success = "Init ok"
    fail = "Init failed"
    list = []
    failedPluginList=[]
    current=''
    for i, line in enumerate(f):
        list.append(line)
        if vip_string in line:
            if success in line:
                current = i
                success_count = success_count+1
            if fail in line:
                fail_count = fail_count+1
                print '\n'.join(list[current+1:i])

    print "Successful plugin load: %d" % success_count
    print "Fail plguin: %d" % fail_count
            # print line



count_plugin()