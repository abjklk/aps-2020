# Program to find the day given date using the Tomohiko Sakamoto Algorithm (Idea of Doomsday Algorithm)

def day_of_the_week(y, m, d) : 

	t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ] 
		
	if (m < 3) : 
		y = y - 1
	
	return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7
	
	
day = 13
month = 9
year = 2020
week = ["sun","mon","tue","wed","thu","fri","sat"]
print(week[day_of_the_week(year, month, day)]) 