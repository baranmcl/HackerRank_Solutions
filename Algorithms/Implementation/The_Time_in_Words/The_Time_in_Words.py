def timewords(h, m):
    words = ['twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine']
    hour = words[h]
    if m > 30:
        hour = words[h+1]
        minutes = words[60-m]
        if m == 45: return 'quarter to %s' %(hour)
        else: return '%s minutes to %s' %(minutes, hour)
    elif m == 0:
        return "%s o' clock" %(hour)
    elif m < 30:
        minutes = words[m]
        if m == 1: return '%s minute past %s' %(minutes, hour)
        if m == 15: return 'quarter past %s' %(hour)
        else: return '%s minutes past %s' %(minutes, hour)
    elif m == 30:
        return 'half past %s' %(hour)
    else:
        return 'You done messed up'

if __name__ == '__main__':
    hour = int(input())
    minutes = int(input())
    print(timewords(hour, minutes))
