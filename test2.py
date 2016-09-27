import time

# Print an introductory text.
print "To get the plugin report, you need to enter the logfile name.\nor enter the full file path of the logfile if it's not in the same location.\nFor Example: Test_data/PluginLoadError.log"
raw_input('press ENTER to continue or CTRL-C to exit..')
video_string = 'Hardware: System  Video'
matrox_not_installed_string = "Matrox DSX.utils version is empty."
matrox_failed_string = "Plugin\MatroxFileWriter.vip: Load"
# Get the file name.
filename = raw_input('Enter the file name here: ')

# Function for write File open error message.
def write_error_log(Error):
    target = open("Error_log.txt", 'a')
    target.write(Error)
    target.close()
# Validate file, write error message for invalid file, in the 'Error_log.txt' file.
try:
    f = open(filename)
except IOError, e:
    io_error = str(e)
    error_msg = "%s. \nPlease check the file name and try again.\n" % io_error
    write_error_log(error_msg)

# Function for counting the successfully loaded/initialized plugins, failed plugins, get the failed plugin names and get the error messages.
def count_plugin():
    success_count = 0
    fail_count = 0
    # Open the file
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

    for i, line in enumerate(f):
        # Append all the lines of the file in the 'all_line_list'.
        all_line_list.append(line)
        # Check if the plugin load/initializing string found.
        if vip_string in line:
            # Check if the plugin load/initializing successful string found, then count the successful plugins.
            if success in line:
                current = i
                success_count += 1
            # Check if the plugin load/initializing failed string found, then count the failed plugins.
            if load_fail in line or init_fail in line:
                # Check for the exceptions, if the engine runs as VGA version or Matrox DSX Utils are not installed, the plugin MatroxFilewriter.vip must be ignored.
                if matrox_failed_string in line:
                    if matrox_not_installed_string in all_line_list:
                        pass
                    else:
                        if video_string in all_line_list:
                            fail_count += 1
                            # Found the failed plugin names from the plugin status string.
                            plugin_name = find_plugin_name(line, plugin_name_start, plugin_name_end)
                            plugin_name_string = "Plugin name: %s\n" % plugin_name
                            error_message_list.append(plugin_name_string)
                            # Found the error message for the failed plugins from the 'all_line_list'.
                            plugin_load_error_message = ''.join(all_line_list[current+1:i])
                            # Create a readable error message string.
                            plugin_load_error_message_final = "Error Message for %s: \n%s\n" % (plugin_name, plugin_load_error_message)
                            # Check if there any failed plugin with no error message.
                            if not plugin_load_error_message:
                                error_message_list.append("No error message found.")
                            else:
                                error_message_list.append(plugin_load_error_message_final)
                # Count the other failed plugins.
                else:
                    fail_count += 1
                    # Found the failed plugin names from the plugin status string.
                    plugin_name = find_plugin_name(line, plugin_name_start, plugin_name_end)
                    plugin_name_string = "Plugin name: %s\n" % plugin_name
                    error_message_list.append(plugin_name_string)
                    # Found the error message for the failed plugins from the 'all_line_list'.
                    plugin_load_error_message = ''.join(all_line_list[current + 1:i])
                    # Create a readable error message string.
                    plugin_load_error_message_final = "Error Message for %s: \n%s\n" % (plugin_name, plugin_load_error_message)
                    # Check if there any failed plugin with no error message.
                    if not plugin_load_error_message:
                        error_message_list.append("No error message found.")
                    else:
                        error_message_list.append(plugin_load_error_message_final)

    # All error message string.
    error_message = ''.join(error_message_list)
    # Return 3 values, number of successful plugins, number of failed plugins and all the error messages.
    return success_count, fail_count, error_message


# Function for finding plugin name from the plugin status string.
def find_plugin_name(line, plugin_name_start, plugin_name_end):
    start = line.find(plugin_name_start) + 8
    end = line.find(plugin_name_end)
    plugin_name = line[start:end]
    return plugin_name


# Function for writing the final output in a file named 'plugin_report.txt'. New file will be created if the file is not already exist.
def write_output(something):
    target = open("plugin_report.txt", 'w')
    target.truncate()
    target.write(something)
    target.close()

# Assign returned values from the 'count_plugin()' function.
success_count = count_plugin()[0]
fail_count = count_plugin()[1]
error_message = count_plugin()[2]

# Create final output strings.
success_count_string = "The number of plugins loaded correctly: %d" % success_count
failed_count_string = "The number of plugins failed to load or initiate: %d" % fail_count
final_output = "%s\n%s\n\n%s\n" % (success_count_string, failed_count_string, error_message)

# Write the output in the 'plugin_report.txt' file using 'write_output()' function.
write_output(final_output)
# Print the success message and wait 3 seconds for watching the message.
print "The report has been generated successfully...\nPlease check the file: 'plugin_report.txt' for details."
time.sleep(3)