from sys import argv
import itertools

script, filename = argv

video_string = "Hardware: System  Video"
matrox_not_installed_string = "Matrox DSX.utils version is empty."
matrox_failed_string = "MatroxFileWriter.vip:"


def count_plugin():
    success_count = 0
    fail_count = 0
    f = open(filename)
    vip_string = ".vip: "
    success = "Init ok"
    load_fail = ".vip: Load failed."
    init_fail = "Init failed"

    list = []
    failedPluginList = []
    current = ''
    for i, line in enumerate(f):
        list.append(line)
        if vip_string in line:
            if success in line:
                current = i
                success_count += 1
            if load_fail in line or init_fail in line:
                fail_count += 1
                # print '\n'.join(list[current+1:i])

    # print "Successful plugins load: %d" % success_count
    # print ".......Fail plugins: %d" % fail_count

    f = open(filename)
    data = f.read()
    # print data
    if video_string in data:
        print "video found"
        if (matrox_not_installed_string in data) and (matrox_failed_string in data):
            print "matrox failed found."
            fail_count -= 1
            # print fail_count
    else:
        print "VGA found"
        if matrox_failed_string in data:
            print "matrox failed found."
            fail_count -= 1
            # print fail_count


    print "Successful plugins load: %d" % success_count
    print "Fail plugins: %d" % fail_count



count_plugin()
