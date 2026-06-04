def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: attendees must be a list of dictionaries")
            return

    placeholders = [
        "name",
        "event_title",
        "event_date",
        "event_location"
    ]

    for index, attendee in enumerate(attendees, start=1):
        content = template

        for key in placeholders:
            value = attendee.get(key, "N/A")

            if value is None:
                value = "N/A"

            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        with open(filename, "w") as file:
            file.write(content)
