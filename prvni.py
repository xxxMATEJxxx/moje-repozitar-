"ZAVORKOVY ZKOUSEC"
# vyzkouší, zda jsou všechny závorky správně uzavřené

def zavorkyzkus(text):
	openbrackets=0
	closebrackets=0
	if (text[0])==")":
		return print("neplatné") 
	if (text[-1])=="(":
		return print("neplatné")
	for znaminko in text:
		if znaminko == "(":
			openbrackets+=1
		if znaminko == ")":
			closebrackets+=1
	if openbrackets==closebrackets: 
		return print("dobře")
	else:
		return print("neplatné")

zavorkyzkus(input())
