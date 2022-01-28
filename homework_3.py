# 1. Create a variable count with value 0
count = 0

# 2. Create variable range_count with value 10
range_count = 10

# 3. Create variable for_count with value 0
for_count = 0

# 4. Create run variable with value True
run = True

# 5. Make a while loop that will run while run
# Loop body:
# 5.1 Output “Hello Cycle” to the console
while run:
    print('Hello Cycle')

# 6. Make a while loop that will run while run
# Loop body:
# 6.1 Output to console (“Step =”, count)
# 6.2 Add 1 to the variable count with an assignment
while run:
    print('Step = ', count)
    count += 1

# 7. Make a while loop that will run while count < range_count
# Loop body:
# 7.1 Output to console (“Step =”, count)
# 7.2 Add 1 to the variable count with assignment
while count < range_count:
    print('Step = ', count)
    count += 1

# 8. Make a while loop that will run while count < range_count
# Loop body:
# 8.1 Output to console (“Step =”, count)
# 8.2 Add 1 to the variable count with an assignment.
# 8.3 Make an if with a condition, if count is 3 then output to the console (“Step =”, count, ‘If body’)
while count < range_count:
    print('Step = ', count)
    count += 1
    if count == 3:
        print('Step = ', count, 'If body')

# 9. Make a while loop that will run while run
# Loop body:
# 9.1 Output to console (“Step =”, count)
# 9.2 Add 1 to the variable count with an assignment
# 9.2 Make an if with a condition, if count is equal to range_count then the loop will stop
# 9.3 In the if body print to the console (“STOP”, count)
while run:
    print('Step = ', count)
    count += 1
    if count == range_count:
        print('STOP', count)
        break

# 10. Make a for loop with the item variable that will run until the range counter counts from for_count to range_count
# Loop body:
# 10.1 Print to console ('Step =', item)
for item in range(for_count, range_count):
    print('Stop = ', item)

# 11. Make a for loop with the item variable that will run until the range counter counts from 0 to 30
# Loop body:
# 11.1 Print to console ('Step =', item)
# 11.2 Make an if with a condition, if item is equal to 5, then print to the console (‘Item =’, item).
# 11.3 Make an if with a condition, if item is equal to 10, then print to the console (‘Item =’, item).
# 11.4 Make an if with a condition, if item is less than 4, then print to the console (‘Item <’, item).
# 11.5 Make an if with a condition, if item is greater than or equal to 27, then print to the console (‘Item >=’, item).
for item in range(0, 30):
    print('Step = ', item)
    if item == 5:
        print('Item =', item)
    if item == 10:
        print('Item =', item)
    if item < 4:
        print('Item < ', item)
    if item >= 27:
        print('Item >= ', item)

# 12.  Make a for loop with the item variable that will run until the range counter counts from 0 to range_count +1
# Loop body:
# 12.1 Print to console ('Step =', item)
# 12.2 Do an if with a condition if item is 7.
# - In the if body, create a variable inner_count equal to 0
# - In the body of the if output to the console ('-- inner_count =', inner_count)
# - In the if body, make another for loop with the inner_item variable that will work until the range counter counts from 0 to item.
# The body of the inner For loop:
# -- Print to consol('-------- Inner_Step =', inner_item)e
# -- Do an if if inner_item is 5, then assign inner_count to inner_item
# - Outside the body of the previous loop, output to the console ('-- inner_count =', inner_count)
for item in range(0, range_count + 1):
    print('Step =', item)
    if item == 7:
        inner_count = 0
        print('-- inner_count = ', inner_count)
        for inner_item in range(0, item):
            print('-------- Inner_Step =', inner_item)
            if inner_item == 5:
                inner_count = inner_item
        print('-- inner_count = ', inner_count)

# 13. Make a for loop with the item variable that will run until the range counter counts from 0 to 20
# Loop body:
# 13.1 Print to console ('Step =', item)
# 13.2 Do an if with a condition if item is greater than 7 and item is less than 12.
# - In the body of if output ('If_item =', item)
# - In the if body, put continue
# 13.3 Exit with if. Print to console ('End_iteration =', item)
for item in range(0, 20):
    print('Step = ', item)
    if (item > 7) and (item < 12):
        print('If_item =', item)
        continue
print('End_iteration = ', item)