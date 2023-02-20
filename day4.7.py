class shape:
    def __init__(self, *args:):
        if(len(args)==1):
            print("the radius of the circle is:",args[0])
            print("Area:",(pi *(args[0]**2)))
        if(len(args)==2):
            print("the slides of your quadeilateral are:",args[0],args[1])