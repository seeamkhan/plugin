from sys import argv

script, filename = argv

video_string = "Hardware: System  Video"
matrox_not_installed_string = "Matrox DSX.utils version is empty."
matrox_failed_string = "Plugin\MatroxFileWriter.vip: Load"


def count_plugin():
    print "Counting plugins:"
    success_count = 0
    fail_count = 0
    f = open(filename)
    vip_string = ".vip: "
    success = "Init ok"
    load_fail = ".vip: Load failed."
    init_fail = "Init failed"
    plugin_name_start = "\\Plugin\\"
    plugin_name_end = ": Load "
    all_line_list = []
    failed_plugin_list = []
    current = ''

    for i, line in enumerate(f):
        all_line_list.append(line)
        if vip_string in line:
            if success in line:
                current = i
                success_count += 1
            if load_fail in line or init_fail in line:
                if matrox_failed_string in line:
                    if matrox_not_installed_string in all_line_list:
                        pass
                    else:
                        if video_string in all_line_list:
                            fail_count += 1
                            print line
                            print find_plugin_name(line, plugin_name_start, plugin_name_end)
                            # collect the error message
                            plugin_load_error_message = ''.join(all_line_list[current+1:i])
                            print plugin_load_error_message
                            # failed_plugin_list.append(plugin_load_error_message)
                else:
                    fail_count += 1
                    print line
                    print find_plugin_name(line, plugin_name_start, plugin_name_end)
                    # collect the error message
                    plugin_load_error_message = ''.join(all_line_list[current + 1:i])
                    print plugin_load_error_message

                    # # collect all the error message
                    # plugin_load_error_message = ''.join(all_line_list[current+1:i])
                    # failed_plugin_list.append(plugin_load_error_message)
    error_message_list = '\n'.join(failed_plugin_list)

    # error_message_list = '\n'.join(failed_plugin_list)
    # write_output(error_message_list)
    # print '\n'.join(failed_plugin_list)

    print "Successful plugins load: %d" % success_count
    print "Fail plugins: %d" % fail_count


def find_plugin_name(line, plugin_name_start, plugin_name_end):
    start = line.find(plugin_name_start) + 8
    end = line.find(plugin_name_end)
    plugin_name = line[start:end]
    return plugin_name
    # print plugin_name


# def write_output(something):
#     target = open("write.txt", 'w')
#     target.truncate()
#     # output.write(error_message_list)
#     target.write(something)
#     target.close()



count_plugin()
