import random
import re
mass = ["Яна", "Данило","Іван","Аліна","Єлізар","Людміла","Сергій", "Даша", "Віталій"]


with open("future.txt", "r") as file:
    future = file.readlines()


for i in mass:
    count = random.randint(0, len(future)) - 1
    future_message = re.sub("\n", "", future[count])
    message = i + ", " +  future_message

    with open (f"files/{i}.txt", "tw+") as f:
        f.write("Послання на рік:\n" + message)
        f.close()
        

    future.pop(count)