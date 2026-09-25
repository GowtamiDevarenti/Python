# ============================================================
# CONFERENCE PLANNING SYSTEM
# Lesson 2 - Lists, Dictionaries, Tuples and Sets
#
# Restrictions:
# - No loops
# - No functions
# - No classes
# - No file handling
# - No external libraries
# ============================================================


# ============================================================
# PART 1 - DESIGN THE CONFERENCE DATA
# ============================================================

# A set is suitable for topics because each topic should be unique.
topics = {
    "Python",
    "Artificial Intelligence",
    "APIs",
    "Cloud Computing",
    "Cybersecurity"
}


# Speakers are stored in a dictionary.
# Each speaker has information connected to that speaker.
speakers = {
    "Ada": {
        "name": "Ada",
        "role": "Python Developer",
        "skills": {"Python", "APIs"}
    },
    "Grace": {
        "name": "Grace",
        "role": "Cloud Engineer",
        "skills": {"Cloud Computing", "APIs"}
    },
    "Alan": {
        "name": "Alan",
        "role": "AI Researcher",
        "skills": {"Artificial Intelligence", "Python"}
    },
    "Linus": {
        "name": "Linus",
        "role": "Cybersecurity Specialist",
        "skills": {"Cybersecurity", "Cloud Computing"}
    },
    "Margaret": {
        "name": "Margaret",
        "role": "AI Engineer",
        "skills": {"Artificial Intelligence", "Python"}
    }
}


# Rooms are stored in a dictionary.
# The room name is the key and its information is the value.
rooms = {
    "Room A": {
        "floor": 1,
        "location": "North Wing",
        "capacity": 50
    },
    "Room B": {
        "floor": 1,
        "location": "South Wing",
        "capacity": 40
    },
    "Room C": {
        "floor": 2,
        "location": "North Wing",
        "capacity": 60
    },
    "Room D": {
        "floor": 2,
        "location": "South Wing",
        "capacity": 30
    }
}


# Participants are stored in a list because:
# - participants can be added
# - participants can be removed
# - order can be useful
participants = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma",
    "Fatima",
    "George",
    "Hannah",
    "Ivan",
    "Julia"
]


# Sessions are stored as a list because the conference has
# an ordered schedule.
#
# Each session is a dictionary because every session has
# several named pieces of information.
sessions = [
    {
        "title": "Python for AI",
        "speaker": "Ada",
        "room": "Room A",
        "start_time": "09:00",
        "duration": 60,
        "topic": "Python",
        "max_participants": 40
    },
    {
        "title": "Building APIs",
        "speaker": "Grace",
        "room": "Room B",
        "start_time": "10:00",
        "duration": 60,
        "topic": "APIs",
        "max_participants": 35
    },
    {
        "title": "Introduction to LLMs",
        "speaker": "Alan",
        "room": "Room C",
        "start_time": "11:30",
        "duration": 90,
        "topic": "Artificial Intelligence",
        "max_participants": 50
    },
    {
        "title": "Cloud Computing Basics",
        "speaker": "Grace",
        "room": "Room D",
        "start_time": "13:30",
        "duration": 60,
        "topic": "Cloud Computing",
        "max_participants": 25
    },
    {
        "title": "Cybersecurity Fundamentals",
        "speaker": "Linus",
        "room": "Room A",
        "start_time": "14:30",
        "duration": 60,
        "topic": "Cybersecurity",
        "max_participants": 40
    },
    {
        "title": "Machine Learning Workshop",
        "speaker": "Margaret",
        "room": "Room C",
        "start_time": "15:30",
        "duration": 90,
        "topic": "Artificial Intelligence",
        "max_participants": 50
    },
    {
        "title": "Advanced Python",
        "speaker": "Ada",
        "room": "Room B",
        "start_time": "17:00",
        "duration": 60,
        "topic": "Python",
        "max_participants": 35
    },
    {
        "title": "Future of Technology",
        "speaker": "Alan",
        "room": "Room D",
        "start_time": "18:00",
        "duration": 60,
        "topic": "Artificial Intelligence",
        "max_participants": 25
    }
]


print("============================================================")
print("PART 1 - CONFERENCE DATA")
print("============================================================")

print("Number of sessions:", len(sessions))
print("Number of speakers:", len(speakers))
print("Number of rooms:", len(rooms))
print("Number of participants:", len(participants))
print("Topics:", topics)


# ============================================================
# PART 2 - WORK WITH THE SCHEDULE
# ============================================================

print("\n============================================================")
print("PART 2 - WORK WITH THE SCHEDULE")
print("============================================================")

# 1. Print the title of the first session.
print("1. First session title:", sessions[0]["title"])

# 2. Print the speaker of the third session.
print("2. Third session speaker:", sessions[2]["speaker"])

# 3. Print the room of the last session.
# Negative indexing gets the last item.
print("3. Last session room:", sessions[-1]["room"])

# 4. Print all information about one selected session.
print("\n4. Complete information about session 4:")
print(sessions[3])

# 5. Print one specific value from a nested structure using
# chained indexing.
print("\n5. Nested indexing:")
print("Third session topic:", sessions[2]["topic"])

# Another example:
print("Third session speaker role:",
      speakers[sessions[2]["speaker"]]["role"])

# 6. Print the first three sessions.
print("\n6. First three sessions:")
print(sessions[:3])

# 7. Print the last two sessions.
print("\n7. Last two sessions:")
print(sessions[-2:])

# 8. Create a reversed version using slicing.
reversed_schedule = sessions[::-1]

print("\n8. Reversed schedule:")
print(reversed_schedule)

# 9. Create a copy containing only part of the schedule.
morning_schedule = sessions[:3]

print("\n9. Morning schedule:")
print(morning_schedule)


# ============================================================
# PART 3 - CONFERENCE CHANGES
# ============================================================

print("\n============================================================")
print("PART 3 - CONFERENCE CHANGES")
print("============================================================")

print("BEFORE CHANGES")
print("Session 1:", sessions[0])
print("Session 2:", sessions[1])
print("Participants:", participants)


# ------------------------------------------------------------
# 1. One session changes room.
# ------------------------------------------------------------

sessions[0]["room"] = "Room C"

print("\nAfter changing Session 1 room:")
print(sessions[0])


# ------------------------------------------------------------
# 2. One speaker is replaced by another speaker.
# ------------------------------------------------------------

sessions[1]["speaker"] = "Margaret"

print("\nAfter replacing the speaker for Session 2:")
print(sessions[1])


# ------------------------------------------------------------
# 3. Add a new session.
# ------------------------------------------------------------

new_session = {
    "title": "Introduction to Quantum Computing",
    "speaker": "Linus",
    "room": "Room D",
    "start_time": "19:00",
    "duration": 60,
    "topic": "Cybersecurity",
    "max_participants": 25
}

sessions.append(new_session)

print("\nAfter adding a new session:")
print("Last session:", sessions[-1])


# ------------------------------------------------------------
# 4. Cancel and remove one session.
# ------------------------------------------------------------

cancelled_session = sessions.pop(4)

print("\nCancelled session:")
print(cancelled_session)

print("\nSchedule after removing cancelled session:")
print(sessions)


# ------------------------------------------------------------
# 5. One participant registers.
# ------------------------------------------------------------

participants.append("Kevin")

print("\nAfter Kevin registers:")
print(participants)


# ------------------------------------------------------------
# 6. One participant cancels.
# ------------------------------------------------------------

participants.remove("Bob")

print("\nAfter Bob cancels:")
print(participants)


# ------------------------------------------------------------
# 7. Add difficulty to one session.
# ------------------------------------------------------------

sessions[0]["difficulty"] = "Beginner"

print("\nSession with new difficulty:")
print(sessions[0])


# ============================================================
# PART 4 - UNIQUE CONFERENCE INFORMATION
# ============================================================

print("\n============================================================")
print("PART 4 - UNIQUE CONFERENCE INFORMATION")
print("============================================================")

# Unique conference topics are already represented by a set.
print("Unique conference topics:")
print(topics)


# Technical skills represented by speakers.
ada_skills = speakers["Ada"]["skills"]
grace_skills = speakers["Grace"]["skills"]
alan_skills = speakers["Alan"]["skills"]
linus_skills = speakers["Linus"]["skills"]
margaret_skills = speakers["Margaret"]["skills"]

technical_skills = (
    ada_skills
    | grace_skills
    | alan_skills
    | linus_skills
    | margaret_skills
)

print("\nUnique technical skills represented by speakers:")
print(technical_skills)


# ------------------------------------------------------------
# Workshop registrations
# ------------------------------------------------------------

workshop_a = {
    "Alice",
    "Charlie",
    "Emma",
    "Fatima",
    "George"
}

workshop_b = {
    "Charlie",
    "Emma",
    "Hannah",
    "Ivan",
    "Julia"
}


# Participants in both workshops.
both_workshops = workshop_a & workshop_b

# Participants only in Workshop A.
only_workshop_a = workshop_a - workshop_b

# Participants only in Workshop B.
only_workshop_b = workshop_b - workshop_a

# All unique participants in either workshop.
all_workshop_participants = workshop_a | workshop_b


print("\nWorkshop A:", workshop_a)
print("Workshop B:", workshop_b)
print("Participants in both:", both_workshops)
print("Only Workshop A:", only_workshop_a)
print("Only Workshop B:", only_workshop_b)
print("All workshop participants:", all_workshop_participants)


# ============================================================
# PART 5 - CONFERENCE CONFIGURATION
# ============================================================

print("\n============================================================")
print("PART 5 - CONFERENCE CONFIGURATION")
print("============================================================")


# Tuples are suitable for fixed information that should not
# normally change.

conference_dates = ("2026-10-10", "2026-10-11")

opening_closing_times = ("08:00", "20:00")

conference_contact = (
    "Tech Conference Team",
    "conference@example.com",
    "+46 70 123 45 67"
)

room_a_location = (1, "North Wing", 50)

session_time_slot = ("09:00", "10:00")


# Access individual tuple values.
print("Conference starts:", conference_dates[0])
print("Conference ends:", conference_dates[1])

print("Opening time:", opening_closing_times[0])
print("Closing time:", opening_closing_times[1])

print("Contact name:", conference_contact[0])
print("Contact email:", conference_contact[1])

print("Room A floor:", room_a_location[0])
print("Room A location:", room_a_location[1])

print("Session time slot:", session_time_slot)


# Unpacking a tuple.
contact_name, contact_email, contact_phone = conference_contact

print("\nUnpacked contact information:")
print(contact_name)
print(contact_email)
print(contact_phone)


# ============================================================
# PART 6 - THE SHARED-REFERENCE PROBLEM
# ============================================================

print("\n============================================================")
print("PART 6 - SHARED REFERENCE")
print("============================================================")


# This does NOT create a new list.
# Both variables refer to the same list.
backup_participants = participants

backup_participants.append("SharedReferencePerson")

print("Original participants:")
print(participants)

print("\nBackup participants:")
print(backup_participants)

# What happened?
# backup_participants = participants creates another reference
# to the SAME list. Therefore, changing backup_participants
# also changes participants.


# ------------------------------------------------------------
# Correct way to create a separate list
# ------------------------------------------------------------

backup_participants = participants.copy()

backup_participants.append("CopyOnlyPerson")

print("\nOriginal participants after using .copy():")
print(participants)

print("\nCopied backup after modification:")
print(backup_participants)

# .copy() creates a new list.
# Therefore, adding an item to backup_participants does not
# change the original participants list.


# ------------------------------------------------------------
# Extra challenge - list containing dictionaries
# ------------------------------------------------------------

participant_records = [
    {"name": "Alice", "ticket": "Standard"},
    {"name": "Charlie", "ticket": "VIP"}
]

participant_records_copy = participant_records.copy()

participant_records_copy[0]["ticket"] = "VIP"

print("\nOriginal participant records:")
print(participant_records)

print("\nCopied participant records:")
print(participant_records_copy)

# The change to the dictionary also appears in the original.
#
# Why?
# .copy() creates a new outer list, but the dictionaries inside
# the list are still shared between the two lists.
#
# This is an example of a shallow copy.


# ============================================================
# PART 7 - RESTRUCTURE THE DATA
# ============================================================

print("\n============================================================")
print("PART 7 - RESTRUCTURED DATA")
print("============================================================")


# The original information was stored in separate lists.
# That makes it difficult to see which speaker and room belong
# to which session.
#
# Instead, each session is represented by one dictionary.
# The dictionaries are stored together inside a list.

restructured_sessions = [
    {
        "title": "Python for AI",
        "speaker": "Ada",
        "room": "Room A",
        "start_time": "09:00",
        "duration": 60,
        "topic": "Python"
    },
    {
        "title": "Building APIs",
        "speaker": "Grace",
        "room": "Room B",
        "start_time": "10:00",
        "duration": 60,
        "topic": "APIs"
    },
    {
        "title": "Introduction to LLMs",
        "speaker": "Alan",
        "room": "Room C",
        "start_time": "11:30",
        "duration": 90,
        "topic": "Artificial Intelligence"
    }
]


# Access the second session.
print("Second session title:",
      restructured_sessions[1]["title"])

print("Second session speaker:",
      restructured_sessions[1]["speaker"])

print("Second session room:",
      restructured_sessions[1]["room"])

print("Second session start time:",
      restructured_sessions[1]["start_time"])

print("Second session duration:",
      restructured_sessions[1]["duration"])

print("Second session topic:",
      restructured_sessions[1]["topic"])


# The new structure is easier to understand because all
# information belonging to one session is stored together.
# We do not have to remember that index 1 in three separate
# lists represents the same session.


# ============================================================
# FINAL CHALLENGE - COMPLETE CONFERENCE STATE
# ============================================================

print("\n============================================================")
print("FINAL CHALLENGE - COMPLETE CONFERENCE STATE")
print("============================================================")


conference = {
    "conference": {
        "name": "Stockholm Technology Conference",
        "year": 2026,
        "dates": conference_dates,
        "opening_closing": opening_closing_times,
        "contact": conference_contact
    },

    "sessions": sessions,

    "speakers": speakers,

    "rooms": rooms,

    "participants": participants,

    "topics": topics,

    "workshops": {
        "Workshop A": workshop_a,
        "Workshop B": workshop_b
    }
}


# ------------------------------------------------------------
# Retrieve at least 10 pieces of information
# ------------------------------------------------------------

print("\n1. Conference name:")
print(conference["conference"]["name"])

print("\n2. Conference year:")
print(conference["conference"]["year"])

print("\n3. Conference start date:")
print(conference["conference"]["dates"][0])

print("\n4. Conference opening time:")
print(conference["conference"]["opening_closing"][0])

print("\n5. Contact email:")
print(conference["conference"]["contact"][1])

print("\n6. First session title:")
print(conference["sessions"][0]["title"])

print("\n7. First session speaker:")
print(conference["sessions"][0]["speaker"])

print("\n8. First session room:")
print(conference["sessions"][0]["room"])

print("\n9. Speaker role:")
print(
    conference["speakers"]
    [conference["sessions"][0]["speaker"]]
    ["role"]
)

print("\n10. Room capacity:")
print(
    conference["rooms"]
    [conference["sessions"][0]["room"]]
    ["capacity"]
)

print("\n11. Number of registered participants:")
print(len(conference["participants"]))

print("\n12. Workshop A participants:")
print(conference["workshops"]["Workshop A"])

print("\n13. Workshop B participants:")
print(conference["workshops"]["Workshop B"])

print("\n14. Conference topics:")
print(conference["topics"])


# ============================================================
# FIVE FINAL CHANGES TO THE CONFERENCE STATE
# ============================================================

print("\n============================================================")
print("FIVE FINAL CHANGES")
print("============================================================")


# Change 1 - Update a session room.
conference["sessions"][0]["room"] = "Room D"

print("Change 1 - New room for first session:")
print(conference["sessions"][0]["room"])


# Change 2 - Update a speaker.
conference["sessions"][2]["speaker"] = "Margaret"

print("\nChange 2 - New speaker for third session:")
print(conference["sessions"][2]["speaker"])


# Change 3 - Add a participant.
conference["participants"].append("Laura")

print("\nChange 3 - Added participant:")
print(conference["participants"])


# Change 4 - Remove a participant.
conference["participants"].remove("Alice")

print("\nChange 4 - Removed participant:")
print(conference["participants"])


# Change 5 - Add difficulty to another session.
conference["sessions"][1]["difficulty"] = "Intermediate"

print("\nChange 5 - Added difficulty:")
print(conference["sessions"][1])


# ============================================================
# FINAL STATE
# ============================================================

print("\n============================================================")
print("FINAL CONFERENCE STATE")
print("============================================================")

print("Conference:", conference["conference"])
print("Sessions:", conference["sessions"])
print("Speakers:", conference["speakers"])
print("Rooms:", conference["rooms"])
print("Participants:", conference["participants"])
print("Topics:", conference["topics"])
print("Workshops:", conference["workshops"])


# ============================================================
# DESIGN EXPLANATION
# ============================================================

# 10. Where did you use a list, and why was a list suitable?
#
# I used lists for sessions and participants.
# A list is suitable because the conference sessions have an
# order, and participants can be added or removed.
#
#
# 11. Where did you use a dictionary, and why was a dictionary
# suitable?
#
# I used dictionaries for speakers, rooms and individual
# sessions.
# A dictionary is suitable because information can be connected
# to descriptive keys such as "name", "room", "speaker" and
# "duration".
#
#
# 12. Where did you use a tuple, and why was a tuple suitable?
#
# I used tuples for conference dates, opening/closing times,
# contact information and room location.
# Tuples are suitable for information that belongs together and
# should normally remain unchanged.
#
#
# 13. Where did you use a set, and why was a set suitable?
#
# I used sets for conference topics, speaker skills and workshop
# registrations.
# Sets are suitable when uniqueness is important and when we
# want to perform operations such as union, intersection and
# difference.
#
#
# 14. Which parts of your data are mutable?
#
# Lists and dictionaries are mutable.
# For example, I can add or remove participants and update
# information about a session.
# Sets are also mutable because items can be added or removed.
#
#
# 15. Which parts should ideally remain unchanged?
#
# Conference dates, opening/closing times and contact
# information can be represented using tuples because these
# values should normally remain fixed.
#
#
# 16. What is one advantage of using nested collections?
#
# Nested collections allow related information to stay together.
# For example:
#
# conference -> sessions -> session -> speaker
#
# This makes the relationships between the data easier to
# understand.
#
#
# 17. What is one disadvantage of deeply nested collections?
#
# Deeply nested collections can become difficult to read and
# access. Long chains of indexing can also make the code harder
# to understand.
#
#
# 18. What is the difference between assigning one list to
# another variable and copying the list?
#
# Example:
#
# backup = participants
#
# Both variables refer to the same list. Changing one changes
# the other.
#
# Example:
#
# backup = participants.copy()
#
# This creates a separate outer list, so changing the list itself
# does not change the original list.
#
#
# 19. If you were allowed to use concepts from later lessons,
# what part would you most want to improve?
#
# I would most like to use functions and classes.
# Functions could reduce repeated code, while classes could
# represent sessions, speakers, rooms and participants in a more
# organized way.
#
# ============================================================
# END OF CONFERENCE PLANNING SYSTEM
# ============================================================
