#
#numbers=[]
#numbers=[111]
#numbers=[1,2,3,4,5,6]
numbers=[1,2,3,4,5,6,7]
len_numbers = len(numbers) #довжина списку
len_numbers1=len_numbers%2 #значення для визначення парної або непарної кількості елементів
len_numbers2=len_numbers//2 #значення для визначення парної або непарної кількості елементів
if len_numbers == 0 or len_numbers == 1:
  print(numbers,"=>",numbers)
elif len_numbers >1:
  numbers1=numbers[0:-1:1]
  numbers1.insert(0, numbers[-1])
  print(numbers,"=>",numbers1)
else:
  print("Щось пішло не так :-)")
