from sys import argv
import itertools
import mmap

script, filename = argv
data = open(filename).read()

success_plugin_string = '.vip: Load ok. Init ok.'
load_init_fail_plugin_string = '.vip: Load failed. Init failed.'
init_fail_plugin_string = '.vip: Load ok. Init failed.'
failed_plugin = 'Init failed.'
found_video = 'Hardware: System  Video'

# Print the number if lines in the file.
def number_of_lines():
    not_a_plugin_string = "Go to hell."
    num_lines = sum(1 for line in open(filename))
    print num_lines

def count_keywords(keywords):
    error_list = []
    f = open(filename)
    count = 0
    for i, line in enumerate(f):
    # for line in f:
        if keywords in line:
            count =  count+1
            error_list.append(line)
            # print line
            print i, line
    print "Found %d '%s' in the file." % (count, keywords)
    print "Here's the error list: "
    print '\n'.join(error_list)

def count_success():
    count_success = data.count(success_plugin_string)
    print "Number of plugins successfully loaded: %d" % count_success


# count_keywords(success_plugin_string)
# count_keywords(load_init_fail_plugin_string)
# count_keywords(load_fail_plugin_string)
# count_keywords(init_fail_plugin_string)
count_success()
count_keywords(failed_plugin)