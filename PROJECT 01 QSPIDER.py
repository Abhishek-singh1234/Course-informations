# #offline counseling \
        
place = input("enter your location : ").lower()
if place == 'gurugram':
   print('''course information or trainer information or offer or discount or payment method :- 
         1.python fullstack
         2.java fullstack
         3.web development
         4.testing
         5.sql
         6.extra courses
         7.trainer information
         8.offer or discount 
         9.payment method
         10. demo schedule

         press the number some 1,2,3,4,5  so,get the particular infrormation of the courses ''')
   print("\n")

   course = int(input("enter the code  : "))
   if course == 1:
       print('''1.python fullstack :-
             
             1.1 html , css, javascript , python, django, sql
             1.2 fees:- 30000
             1.3 duration:- 1year
             1.4 timing :- 2:00 to 4:00
             ''')

   elif course == 2:
        print('''2.java fullstack :-
              
             2.1 html , css, javascript , java , sql
             2.2 fees:- 30000
             2.3 duration:- 1year
             2.4 timing :- 9:00 to 11:00
             ''')
   elif course == 3:
        print('''3.web development :-
              
             3.1 html , css, javascript , react,bootstrap
             3.2 fees:- 17000
             3.3 duration:- 1year
             3.4 timing :- 8:00 to 11:00
             ''')
        
   elif course == 4:
        print('''4.testing :-
              
             4.1 python , java , menual testing , testing
             4.2 fees:- 30000
             4.3 duration:- 1year
             4.4 timing :- 11:00 to 1:00
             ''')
   elif course == 5:
        print('''2.sql:-
              
             5.1 sql
             5.2 fees:- 5000
             5.3 duration:- 1year
             5.4 timing :- 12:00 to 2:00
             ''')
   elif course == 6:
        print('''6.extra skills :-
              
             6.1 resume bulilding, intership etc.
             6.2 fees:- 10000
             6.3 duration:- 1year
             6.4 timing :- 11:00 to 1:00
             ''')
        
   elif course == 7:
        print('''7.trainer information :-
              
             7.1 python :- nadeem sir 
             7.2 java :- debasis sir
             7.3 wed developmen :- aman sir
             7.4 testing :- chandrakanta sir
             7.5 sql :- harshal sir
             ''')
   elif course == 8:
        print('''8.offer or discount :-
              
            8.1 month begining :- 2000
            8.2 month ending :- 2500
            8.3 present time join :- 3000
            8.4 one time payment :- 500
             ''')
   elif course == 9:
        print('''9.payment method :-
              9.1 online
              9.2 offline
              9.3 one time payment
              9.4 installment :- 
                  9.4.1:- 1st installment - 60%
                  9.4.2:- 2nd installment - 40%
             
             ''')
   elif course == 10:
        print('''10. demo schedule :-
              
             10.1 :-  3 day demo
            
              
             ''')
        
       
   else:
       print("----Enter the valid code----")

else:
   print("----Not a gurugram branch-----")















