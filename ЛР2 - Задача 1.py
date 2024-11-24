money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Счетчик месяцев

# Цикл, пока есть возможность покрывать расходы
while True:
    # Рассчитываем текущий бюджет
    current_budget = money_capital + salary

    if current_budget < spend:  # Проверяем, хватает ли бюджета на текущие расходы
        break  # Если нет, то выходим из цикла

    months += 1  # Увеличиваем счётчик месяцев
    money_capital -= spend  # Уменьшаем капитал на текущие расходы
    money_capital += salary # Увеличиваем бюджет за счёт ЗП
    spend *= (1 + increase)  # Увеличиваем траты на рост цен


print("Количество месяцев, которое можно протянуть без долгов:", months)