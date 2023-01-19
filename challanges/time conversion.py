def convertToSeconds(hours, minutes):
    seconds = ((hours * 60) + minutes) * 60
    return seconds

print(convertToSeconds(3,25))

def convertToHours(minutes):
    hours = (minutes / 60)
    return hours

print(int(convertToHours(120)))