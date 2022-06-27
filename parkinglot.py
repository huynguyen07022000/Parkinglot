from tabulate import tabulate
import pyttsx3
import time
current = 0
maximum = 700
row1_max = 100
row1 = 0
t1 = 0
row2_max = 100
row2 = 0
t2 = 0
row3_max = 100
row3 = 0
t3 = 0
row4_max = 100
row4 = 0
t4 = 0
row5_max = 100
row5 = 0
t5 = 0
row6_max = 100
row6 = 0
t6 = 0
row7_max = 100
row7 = 0
t7 = 0

while True:
	mydata = [["Hàng 1", row1_max],["Hàng 2", row2_max],["Hàng 3", row3_max],["Hàng 4", row4_max],["Hàng 5", row5_max],["Hàng 6", row6_max],["Hàng 7", row7_max],]
	head = ["Hàng", "Chỗ trống còn lại"]
	print(tabulate(mydata, headers=head, tablefmt="grid"))

	input("Nhấn Enter để đưa xe vào")
	t = time.time()
	current += 1

	if int(current)<int(maximum):
		if t-t1>10 and row1 <= 100 :
			row1 += 1
			row1_max -= 1
			
			print("Mời bạn di chuyển tới hàng 1")
			t1=time.time()
			#Nói
			robot_brain = "Row 1"
			robot_mouth = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

		elif t-t2>10 and row2 <= 100 :
			row2 += 1
			row2_max -= 1
			print("Mời bạn di chuyển tới hàng 2")
			t2=time.time()
			#Nói
			robot_brain = "Row 2"
			robot_mouth = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

		elif t-t3>10 and row3 <= 100 :
			row3 += 1
			row3_max -= 1
			print("Mời bạn di chuyển tới hàng 3")
			t3=time.time()
			#Nói
			robot_brain = "Row 3"
			robot_mouth = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

		elif t-t4>10 and row4 <= 100 :
			row4 += 1
			row4_max -= 1
			print("Mời bạn di chuyển tới hàng 4")
			t4=time.time()
			#Nói
			robot_brain = "Row 4"
			robot_mouth = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

		elif t-t5>10 and row5 <= 100 :
			row5 += 1
			row5_max -= 1
			print("Mời bạn di chuyển tới hàng 5")
			t5=time.time()
			#Nói
			robot_brain = "Row 5"
			robot_mouth = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()
		
		elif t-t6>10 and row6 <= 100 :
			row6 += 1
			row6_max -= 1
			print("Mời bạn di chuyển tới hàng 6")
			t6=time.time()
			#Nói
			robot_brain = "Row 6"
			robot_mouth = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

		elif t-t7>10 and row7 <= 100 :
			row7 += 1
			row7_max -= 1
			print("Mời bạn di chuyển tới hàng 7")
			t7=time.time()
			#Nói
			robot_brain = "Row 7"
			robot_mouth = pyttsx3.init()
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

	else:
		print("Hết chỗ để xe!")
		robot_brain = "Parking full of lot"
		robot_mouth = pyttsx3.init()
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
		