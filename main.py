user_task = []

while True:
    print('-----Aplikacja ToDoList-----')
    print('1. Dodaj zadanie')
    print('2. Wyświetl zadania')
    print('3. Usuń zadanie z listy')
    print('4. Oznacz zadanie jako wykonane')
    print('5. Zapisz zadania do pliku')
    print('6. Wczytaj zadania z pliku')

    user_choice0 = input('Wybierz co chcesz zrobić: ')

    if user_choice0 == '1':
        user_choice1 = input('Dodaj zadanie: ')
        user_task.append(user_choice1)
    elif user_choice0 == '2':
        print(user_task)
    elif user_choice0 == '3':
         user_choice2 = input('Podaj, które zadanie chcesz usunąć: ')
         user_task.remove(user_choice2)
    else:
        print('Nie ma takiej opcji')
        break
