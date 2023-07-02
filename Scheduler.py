# after arrive, from -new- to -ready-
def admit():
    pass

# from -ready- to -running-, after selecting
def dispatch():
    pass

# from -running- to -ready-
def preempt():
    pass

# from -running- to -waiting- after CPU burst 1
def IO_request():
    pass

# from -waiting- to -ready- after IO burst
def IO_completion():
    pass

# from -running- to - terminated-, after CPU burst 2
def terminate():
    pass