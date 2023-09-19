def add_time(start, duration, day=False):
  
    # CONSTANTS
    DAY_MINUTES = 1440
    HOUR_MINUTES = 60
    WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Separate elements and transforming into int to operate
    hour = start.lower().split()
    time = hour[0].split(':')
    time = [int(x) for x in time]
    
    # Transforming to 24h format and turning into minutes
    if hour[1] == 'pm':
        time[0] += 12
    time[0] *= HOUR_MINUTES
    minutes = time[0] + time[1]

    # The same for duration
    time = duration.split(':')
    time = [int(x) for x in time]
    time[0] *= HOUR_MINUTES
    minutes += time[0] + time[1]
    
    # Check how many days
    message = ', ' + day.capitalize() if day else False
      
    if minutes > DAY_MINUTES:
        days = int(minutes/DAY_MINUTES)
        message = ''
        if day:
            index = WEEK.index(day.capitalize())
            index += days
            while index > 6:
                index -= 7
            message = ', ' + WEEK[index]
        if days > 1:
            message += ' (' + str(days) + ' days later)'
        else:
            message += ' (next day)'
        
        # Set new time
        days *= DAY_MINUTES
        minutes -= days
    
    # Return to HH:MM format
    new_hour = int(minutes / HOUR_MINUTES)
    new_minutes = minutes - (new_hour * HOUR_MINUTES)
    
    # Check if AM or PM
    if new_hour >= 0 and new_hour < 12:
        meridian = ' AM'
    else:
        new_hour -= 12
        meridian = ' PM'
    if new_hour == 0:
        new_hour = 12
    
    new_time = str(new_hour) + ':' + "{0:0=2d}".format(new_minutes) + meridian
    
    if message:
        new_time += message
    
    return new_time