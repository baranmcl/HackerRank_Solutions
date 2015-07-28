def timeConverter(time):
    hour = int(time[0])*10 + int(time[1])
    if time[8] == 'P' and hour != 12:
        newhour = hour + 12
        time = str(newhour) + time[2:8]
    elif time[8] == 'A' and hour == 12:
        newhour = '00'
        time = newhour + time[2:8]
    return time[:8]

if __name__ == '__main__':
    time = str(input())
    print(timeConverter(time))
