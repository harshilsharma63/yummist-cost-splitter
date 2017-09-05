#!/usr/bin/python3


def obtain_user_meal_cost_data():
    user_data = {}

    number_of_users = int(input('Enter number of users: '))
    for i in range(number_of_users):
        username = input('Name: ')
        cost = eval(input('cost equation: '))
        user_data[username] = {'cost': cost}
    return user_data


def calculate_meal_total_cost(user_data):
    total = 0
    for key, value in user_data.items():
        total += value['cost']
    return total


def populate_user_cost_percentage(user_data, total):
    for username in user_data.keys():
        user_data[username]['percentage'] = user_data[username]['cost'] * 100 / total


def get_discount_percentage():
    return float(input('Discount%: ')) / 100.0


def calculate_cost_per_person(user_data, total, discount):
    discounted_price = total * (1 - discount)
    for username in user_data.keys():
        user_discounter_price = discounted_price / 100 * user_data[username]['percentage']
        user_data[username]['discounted_price'] = user_discounter_price


def print_final_cost_per_person(user_data):
    for username, cost_data in user_data.items():
        cost = cost_data['discounted_price']
        print('{username}: {cost}'.format(username=username, cost=cost))


def main():
    user_data = obtain_user_meal_cost_data()
    discount = get_discount_percentage()

    total = calculate_meal_total_cost(user_data)
    populate_user_cost_percentage(user_data, total)
    calculate_cost_per_person(user_data, total, discount)
    print_final_cost_per_person(user_data)


if __name__ == '__main__':
    main()
