import _2_year_LR_3

task_func_dict = { # Словник для швидкого доступу до відповідної функції виконання
    "1": _2_year_LR_3.task_Proc26,
    "2": _2_year_LR_3.task2_Matrix5,
}

if __name__ == '__main__':
  choice = input("Please, choose the task 1-3 (0-EXIT): ")
  while choice != "0":
    # Якщо даний ключ є у словнику
    if choice in task_func_dict.keys():
      # Викликаємо відповідну функцію
      task_func_dict.get(choice)()
    else:
      print("Wrong task number!")
    choice = input("Please, choose the task again (0-EXIT): ")
