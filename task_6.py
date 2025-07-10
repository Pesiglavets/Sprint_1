types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

tickets_by_type = {

}

def clear_duplicates(tickets):
    seen_tickets = []
    unique_tickets = {}

    for level in tickets.keys():
        current_tickets = []
        if level in tickets:
            for ticket in tickets[level]:
                if ticket not in seen_tickets:
                    current_tickets.append(ticket)
                    seen_tickets.append(ticket)
            unique_tickets[level] = current_tickets

    return unique_tickets

def filter_by_type():
    unique_tickets = clear_duplicates(tickets)

    for key, value in unique_tickets.items():
        tickets_by_type[types[key]] = value
    print(tickets_by_type)
    return tickets_by_type


filter_by_type()