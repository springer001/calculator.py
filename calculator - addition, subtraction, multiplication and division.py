
    if options in ["1", "2", "3", "4"]:
        int1 = int(input("input your first integer: ")) 
        int2 = int(input("input your second integer: "))
        # these are the generic scripts for when it asks you to input each integer for the calculation
        # you can alway consider the heart of the code, because if this part didn't exist, the whole code would basically break.


    if options == "1":
        result_given = int1 + int2 
        print(result_given)
        # this is the result of addition, of course.

    elif options == "2":
        result_given = int1 - int2
        print(result_given)
        # same for subtraction

    elif options == "3":
        result_given = int1 * int2
        print(result_given)
        # i would believe you understand the process now

    elif options == "4":
        if int1 or int2 == 0:
            print("you can't divide a number by 0.")
            show_choices = False
        continue    
        result_given = int1 / int2
        print(result_given)
        # now this code is a little different; as i've included a script for as you would understand you can't really divide numbers by 0.
