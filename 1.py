def add_course(all_courses): 
    #print("Evaluation:")
    print("")
    course_name = name_of_course()

    while course_name == "" or course_name in all_courses:
            if course_name == "":
                course_name = input("Course name cannot be empty ")
            elif course_name == all_courses:
                course_name = input("Error: course name already exists")
            #course_name = input("Course_name: ")
    all_courses[course_name] = {}
    print("Evaluation:")



    activity = name_of_activity(all_courses,course_name)
    weight = get_weight()


    while activity !="" :
        all_courses[course_name][activity]= {}
        break

    while True:
        if weight == "":
            weight = input("Error: the weight number cannot be empty")
        else:
            weight = float(weight)
            all_courses[course_name][activity]['weight'] = weight
            break
        print("Evaluation:")

    while True:
        activity = name_of_activity(all_courses,course_name)
        weight = get_weight()

        if activity =="":
            break

        print(" === Gradebook ===")
    return print("evaluation: ") , all_courses
#SUB FUNCTIONS USED AND IMPLETED IN TO ADD COURSE FUNCTION
def get_weight():
    weight_of_activity = input("  Weight: ")

    while not weight_of_activity.isdigit():
        weight_of_activity = input("  Weight: ")

        if weight_of_activity == "":
            break


    return weight_of_activity
#-----------------------------------------------------------------
def name_of_activity(all_courses,course_names):
    activity = input("  Activitiy: ")
    if activity == "":
        return print("\n\n === Gradebook ===")

    elif activity in all_courses[course_names]:
        print("Error: the activity name already exists")
        activity = input("  Activity: ")
    else: 
        return (activity)

all_courses = {}    
add_course(all_courses)
