# to calculate total and average of the given numbers where if 0 comes use continue and in case of negative use break
# where munbers are:10,0,25,0,50,-1,40

numbers = [10, 0, 25, 0, 50, -1, 40]
total = 0
count = 0

for num in numbers:
        if num == 0:continue
        if num < 0 : break
        print (f"Numbers Are:{num}")

        total += num
        count = count+1
        
        average = total/count if count!= 0 else 0
print(f"Sum is: {total}")
print(f"Average is: {average}")


