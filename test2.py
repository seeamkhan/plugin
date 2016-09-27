import os
import os.path


print "To get the plugin report, you need to enter the logfile name.\nor enter the full file path of the logfile if it's not in the same location.\nFor Example: Test_data/PluginLoadError.log"
raw_input('press ENTER to continue or CTRL-C to exit..')
video_string = 'Hardware: System  Video'
matrox_not_installed_string = "Matrox DSX.utils version is empty."
matrox_failed_string = "Plugin\MatroxFileWriter.vip: Load"
filename = raw_input('Enter the file name here: ')

def count_plugin():
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
    current = ''
    error_message_list = []

    try:
        os.path.isfile(filename) and os.access(filename, os.R_OK)
    except IOError:
        print "Either the file does not exist or is not readable"

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
                            plugin_name = find_plugin_name(line, plugin_name_start, plugin_name_end)
                            plugin_name_string = "Plugin name: %s\n" % plugin_name
                            error_message_list.append(plugin_name_string)
                            plugin_load_error_message = ''.join(all_line_list[current+1:i])
                            plugin_load_error_message_final = "Error Message for %s: \n%s\n" % (plugin_name, plugin_load_error_message)
                            if not plugin_load_error_message:
                                error_message_list.append("No error message found.")
                            else:
                                error_message_list.append(plugin_load_error_message_final)
                else:
                    fail_count += 1
                    # print line
                    # print find_plugin_name(line, plugin_name_start, plugin_name_end)
                    plugin_name = find_plugin_name(line, plugin_name_start, plugin_name_end)
                    plugin_name_string = "Plugin name: %s\n" % plugin_name
                    error_message_list.append(plugin_name_string)
                    plugin_load_error_message = ''.join(all_line_list[current + 1:i])
                    plugin_load_error_message_final = "Error Message for %s: \n%s\n" % (plugin_name, plugin_load_error_message)
                    if not plugin_load_error_message:
                        error_message_list.append("No error message found.")
                    else:
                        error_message_list.append(plugin_load_error_message_final)

    error_message = ''.join(error_message_list)
    write_output(error_message)
    return success_count, fail_count, error_message


def find_plugin_name(line, plugin_name_start, plugin_name_end):
    start = line.find(plugin_name_start) + 8
    end = line.find(plugin_name_end)
    plugin_name = line[start:end]
    return plugin_name


def write_output(something):
    target = open("plugin_report.txt", 'w')
    target.truncate()
    target.write(something)
    target.close()

success_count = count_plugin()[0]
fail_count = count_plugin()[1]
error_message = count_plugin()[2]

success_count_string = "The number of plugins loaded correctly: %d" % success_count
failed_count_string = "The number of plugins failed to load or initiate: %d" % fail_count
final_output = "%s\n%s\n\n%s\n" % (success_count_string, failed_count_string, error_message)

write_output(final_output)
print "The report has been generated successfully...\nPlease check the file: 'plugin_report.txt' for details."