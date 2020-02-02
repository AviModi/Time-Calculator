user_input = int(input("Enter A Number Of Seconds: "))
seconds = user_input
hours = seconds//3600
seconds = seconds % 3600
minutes = seconds//60
seconds = seconds % 60
print(hours,"hours", minutes,"minutes", seconds, "seconds")
