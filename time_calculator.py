def add_time(*times):
    if len(times) == 3:
        start_time = times[0].split(" ")
        meridium = start_time[1]
        time = start_time[0].split(":")

        hour = int(time[0])
        minutes = int(time[1])

        dur = times[1].split(":")
        hour2 = int(dur[0])
        minutes2 = int(dur[1])

        days = 0

        if meridium == "PM":
            cont = 1
        else:
            cont = 0

        for i in range(hour2):
            hour = hour + 1
            if hour == 12:
                if meridium == "PM":
                    meridium = "AM"
                    days = days + 1
                else:
                    meridium = "PM"
                    cont = cont + 1
            if hour == 13:
                hour = 1

        for i in range(minutes2):
            minutes = minutes + 1
            if minutes == 60:
                hour = hour + 1
                minutes = 0
                if hour == 12:
                    if meridium == "PM":
                        meridium = "AM"
                        days = days + 1
                    else:
                        meridium = "PM"
            if hour == 13:
                hour = 1

        h = str(hour)

        if len(str(minutes)) == 1:
            m = str(minutes).zfill(2)
        else:
            m = str(minutes)

        day = times[2]

        if day == "Monday":
          today = 0
        elif day == "tuesday":
          today = 1
        elif day == "Wednesday":
          today = 2
        elif day == "Thursday":
          today = 3
        elif day == "Friday":
          today = 4
        elif day == "saturDay":
          today = 5
        else:
          today = 6
        
        d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        if day == "Monday" or day == "saturDay" or day == "Wednesday" or day == "tuesday":
            for i in range(days):
              today = today + 1
              if today == 7:
                today = 0
            if days > 0:
                if cont == 1:
                    new_time = h + ":" + m + " " + meridium + ", " + d[today] + " (next day)"
                else:
                    new_time = h + ":" + m + " " + meridium + ", " + d[today] + " (" + str(
                        cont) + " days later)"
            else:
                new_time = h + ":" + m + " " + meridium + ", " + d[today]
        else:
            if days > 0:
                if cont == 1:
                    new_time = h + ":" + m + " " + meridium + " (next day)"
                else:
                    new_time = h + ":" + m + " " + meridium + " (" + str(
                        cont) + " days later)"
            else:
                new_time = h + ":" + m + " " + meridium

        return new_time

    else:
        start_time = times[0].split(" ")
        meridium = start_time[1]
        time = start_time[0].split(":")

        hour = int(time[0])
        minutes = int(time[1])

        dur = times[1].split(":")
        hour2 = int(dur[0])
        minutes2 = int(dur[1])

        days = 0

        if meridium == "PM":
            cont = 1
        else:
            cont = 0

        for i in range(hour2):
            hour = hour + 1
            if hour == 12:
                if meridium == "PM":
                    meridium = "AM"
                    days = days + 1
                else:
                    meridium = "PM"
                    cont = cont + 1
            if hour == 13:
                hour = 1

        for i in range(minutes2):
            minutes = minutes + 1
            if minutes == 60:
                hour = hour + 1
                minutes = 0
                if hour == 12:
                    if meridium == "PM":
                        meridium = "AM"
                    else:
                        meridium = "PM"
            if hour == 13:
                hour = 1

        h = str(hour)

        if len(str(minutes)) == 1:
            m = str(minutes).zfill(2)
        else:
            m = str(minutes)

        if days > 0:
            if cont == 1:
                new_time = h + ":" + m + " " + meridium + " (next day)"
            else:
                new_time = h + ":" + m + " " + meridium + " (" + str(
                    cont) + " days later)"
        else:
            new_time = h + ":" + m + " " + meridium

        return new_time
