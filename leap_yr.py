# Given a year tell whether it is leap year or not.

def leap(yr):
	if yr % 400==0 or ( yr%100!=0 and yr%4==0 ):
		print("Leap year")
	else:
		print("Normal year")
         

leap(2020)