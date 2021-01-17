
def recursion():
        
    tracker = 0

    def callMe():
        tracker += 1
        if tracker == 3:
            tracker = 0
            return f'loops! '
        return callMe()

callMe = recursion()