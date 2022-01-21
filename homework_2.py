# 1. Create an int_item variable with a value of 10
int_item = 10

# 2. Create comp_item variable with value 18
comp_item = 18

# 3. Create a variable mult_int in which multiply int_item by 2
mult_int = int_item * 2

# 4. Create variable item_2 with value True
item_2 = True

# 5. Create variable item_3 with value False
item_3 = False

# 6. Create variable item_4 with value 0
item_4 = 0

# 7. Create variable item_5 with value 1
item_5 = 1

# 8. Create variable usd_item with value 'usd'
usd_item = 'usd'

# 9. Create variable usd_usd_rate with value 1
usd_usd_rate = 1

# 10. Create variable eur_item with value 'eur'
eur_item = 'eur'

# 11. Create variable usd_eur_rate with value 0.86
usd_eur_rate = 0.86

# 12. Create variable uah_item with value 'uah'
uah_item = 'uah'

# 13. Create variable usd_uah_rate with value 26.23
usd_uah_rate = 26.23

# 14. Create variable chf_item with value 'chf'
chf_item = 'chf'

# 15. Create variable usd_chf_rate with value 0.91
usd_chf_rate = 0.91

# 16. Create variable rub_item with value 'rub'
rub_item = 'rub'

# 17. Create variable usd_rub_rate with value 71.88
usd_rub_rate = 71.88

# 18. Create variable byn_item with value 'byn'
byn_item = 'byn'

# 19. Create variable usd_byn_rate with value 2.46
usd_byn_rate = 2.46

# 20. Make an if in which there will be a condition: if mult_int is greater than comp_item,
# then output to the console (“mult_int variable is greater than”, comp_item)
if mult_int > comp_item:
    print('mult_int variable is greater than', comp_item)

# 21. Create a div_int variable in which to divide int_item by 2
div_int = int_item / 2

# 22. Make an if in which there will be a condition: if div_int is less than comp_item,
# then output to the console (“div_int variable is less than”, comp_item)
if div_int < comp_item:
    print('div_int variable is less than', comp_item)

# 23. Create a variable item_1 in which to add 10 to the variable int_item
item_1 = int_item + 10

# 24. Make an if in which there will be a condition: if item_1 is less than comp_item,
# then print to the console (“Variable item_1 is less than”, comp_item),
# otherwise, print to the console (“Variable item_1 is greater than or equal to”, comp_item)
if item_1 < comp_item:
    print('Variable item_1 is less than', comp_item)
else:
    print('Variable item_1 is greater than or equal to', comp_item)

# 25. Make an if in which there will be a condition: if item_2, then output to the console (“Variable item_2 = ”, item_2),
# otherwise, output to the console (“Variable item_2 = ”, item_3)
if item_2:
    print('Variable item_2 = ', item_2)
else:
    print('Variable item_2 = ', item_3)

# 26. Make an if in which there will be a condition: if item_3, then output to the console (“Variable item_3 = ”, item_2),
# otherwise, output to the console (“Variable item_3 = ”, item_3)
if item_3:
    print('Variable item_3 = ', item_2)
else:
    print('Variable item_3 = ', item_3)

# 27. Make an if in which there will be a condition: if item_5, then output to the console (“Variable item_5 = ”, item_5),
# otherwise, output to the console (“Variable item_5 = ”, item_4)
if item_5:
    print('Variable item_5 = ', item_5)
else:
    print('Variable item_5 = ', item_4)

# 28. Make an if in which there will be a condition: if item_4, then output to the console (“Variable item_4 = ”, item_5),
# otherwise, output to the console (“Variable item_4 = ”, item_4)
if item_4:
    print('Variable item_4 = ', item_5)
else:
    print('Variable item_4 = ', item_4)

# 29. Create variable currency_convertor with value item_2
currency_convertor = item_2

# 30. Make an if in which there will be a condition: if currency_convertor, then perform the following steps of the task,
# otherwise, output to the console (“Variable currency_convertor = ”, item_3)
# 31. Inside if currency_convertor make the following If conditions:
# 31.1 Create variable currency_usd with value usd_item
# 31.2 Create target_currency variable with value eur_item
# 31.3 Create variable target_currency_amount with value 50
# 31.4 Create variable currency_result with value 0
# 31.4 Make an if in which there will be a condition: if target_currency is equal to 'eur', then in the body of this if,
# in the value of the currency_result variable, calculate how many dollars will be obtained with target_currency_amount
# and usd_eur_rate. Output the result to the console (target_currency_amount, eur_item, “=”, currency_result, usd_item)
# 31.5 Make elif in which there will be a condition: if target_currency is equal to 'uah', then in the body of this if,
# in the value of the currency_result variable, calculate how many dollars will be obtained with target_currency_amount
# and usd_uah_rate. Output the result to the console (target_currency_amount, uah_item, “=”, currency_result, uah_item)
# 31.6 Make elif with other currencies
# 31.7 Leave the else last, which will display (“Unknow currency”) in the console.
if currency_convertor:
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0

    if target_currency == 'eur':
        currency_result = target_currency_amount / usd_eur_rate
        print(target_currency_amount, eur_item, '=', currency_result, usd_item)

    elif target_currency == 'uah':
        currency_result = target_currency_amount / usd_uah_rate
        print(target_currency_amount, uah_item, '=', currency_result, uah_item)

    elif target_currency == 'usd':
        currency_result = target_currency_amount / usd_uah_rate
        print(target_currency_amount, usd_item, '=', currency_result, usd_item)

    elif target_currency == 'chf':
        currency_result = target_currency_amount / usd_chf_rate
        print(target_currency_amount, chf_item, '=', currency_result, chf_item)

    elif target_currency == 'rub':
        currency_result = target_currency_amount / usd_rub_rate
        print(target_currency_amount, rub_item, '=', currency_result, rub_item)

    elif target_currency == 'byn':
        currency_result = target_currency_amount / usd_byn_rate
        print(target_currency_amount, byn_item, '=', currency_result, byn_item)

    else:
        print('Unknown currency')

else:
    print('Variable currency_convertor = ', item_3)