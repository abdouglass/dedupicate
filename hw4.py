# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

# Goal 2: Who came to *both* your Film Screening and your Happy hour?
def import2files(file1, file2):
    with open(file1,"r") as first_file:
        first_event = first_file.read()
        first_event_list = first_event.split("\n")
        attendees_first = len(first_event_list)
        #print "The number of people at the first event was {0} and their email addresses are {1}.".format(attendees_first,first_event_list)
    with open(file2,"r") as second_file:
        second_event = second_file.read()
        second_event_list = second_event.split("\n")
        attendees_second = len(second_event_list)
        #print "The number of people at the second event was {0} and their email addresses are {1}.".format(attendees_second,second_event_list)
    return first_event_list, second_event_list

first_event_list, second_event_list =import2files("film_screening_attendees.txt","happy_hour_attendees.txt")

def combinelists(list1,list2):
    completelist=list1 + list2
    print completelist
    return completelist

duplicated_members = combinelists(first_event_list,second_event_list)

def dedupattendees(all_members):
    members=list(set(all_members))
    total_members = len(members)
    print "The email list for all members is {0} and we have {1} members.".format(members, total_members)
    return members

currentmembers = dedupattendees(duplicated_members)
total_members = len(currentmembers)

attendedboth=list(set(first_event_list)&set(second_event_list))
print "We had {0} members attend both events and they were: {1}".format(len(attendedboth),attendedboth)
