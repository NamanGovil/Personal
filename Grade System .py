grades = []
 
print ( "Enter your choices - ")
while ( True ) :
    print ( "Enter your choice - ")
    print ( "Enter Grades - 1")
    print ( "Delete Grades - 2")
    print ( "Update Grades - 3")
    print ( "Clear Grades - 4")
    print ( "Calculate Average - 5")
    print ("Exit - 6")
     
    choice = input("-->")
    if choice == "6" :
        break
     
    if choice == "1" :
        print ( "Enter grades. type e to exit")
        while True :
            grade = input ( " --> ")
            if grade == "e" :
                break
            else :
                grade   = float(grade)
                grades.append(grade)
        print ( "You have entered - ")
        print ( grades )
 
    elif choice == "2" :
        if len(grades) == 0 :  
            print ( " No grades input yet. Please try to input grades")
        else :
            print ( "Enter index to delete. type e to exit")
            while True or len(grades) != 0 :
                index = 0
                print ( "index - grade")
                for grade in grades :
                    print ( index,"\t",grade)
                    index = index + 1
                 
                grade = input ( "-->")
                if grade == "e" :
                    break
                else :
                    if int(grade) < len(grades) :
                        grades.pop(int(grade))
     
    elif choice == "3":
        if len(grades) == 0 :  
            print ( " No grades input yet. Please try to input grades")
        else :
            print ( "Enter index to update. type e to exit")   
            while True or len(grades) != 0 :
                index = 0
                print ( "index - grade")
                for grade in grades :
                    print ( index,"\t",grade)
                    index = index + 1            
 
                grade = input ( "-->")
                if grade == "e" :
                    break
                else :
                    if int(grade) < len(grades) :
                        print ( "Changing grade")
                        print ( "--------------")
                        print ( "index - grade")
                        print ( int(grade), "\t",grades[int(grade)])
                        print ( "enter new grade")
                        new_grade = input( "-->")
                        grades[int(grade)] = float(new_grade)          
 
    elif choice == "4" :
        if len(grades) == 0 : 
            print ( " No grades input yet. Please try to input grades")   
        else :
            grades.clear()
            print ( "cleared all grades") 
            print ( "=================")        
 
    elif choice == "5" :
        average = sum(grades) / len(grades)
        print ("Average --> ",average)    
        print ("=================")       
     
    else :
        print ( "Enter valid choice - Try again")
