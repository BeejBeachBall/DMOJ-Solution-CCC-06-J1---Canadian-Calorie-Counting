b = int(input())
s = int(input())
dr = int(input())
de = int(input())


if b == 1:
	b = 461

elif b == 2:
	b = 431

elif b == 3:
	b = 420

elif b == 4:
	b = 0



if s == 1:
	s = 100

elif s == 2: 
	s = 57

elif s == 3:
	s = 70

elif s == 4:
	s = 0



if dr == 1:
	dr = 130

elif dr == 2:
	dr = 160

elif dr == 3:
	dr = 118

elif dr == 4:
	dr = 0



if de == 1:
	de = 167

elif de == 2:
	de = 266

elif de == 3:
	de = 75

elif de == 4:
	de = 0
	

total = (b + s + dr + de)

print('Your total Calorie count is ' + str(total) + '.')
