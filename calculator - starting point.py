import math # this initiates the equations for cosine, sine and tangent later on

show_choices = True # if this is enabled, it shows the script at the given moment.
                    # if disabled, it completely hides the whole option tray.

while True:
    if show_choices:
        print("choose an operator(1-8): ")
        print("(1): addition")
        print("(2): subtraction")
        print("(3): multiplication")
        print("(4): division")
        print("(5): exponentiate")
        print("(6): sine")
        print("(7): cosine")
        print("(8): tangent")
        # choices for the different calculator options
    
    options = input("list choice here: ")
    # the script in which the user lists their choices.
