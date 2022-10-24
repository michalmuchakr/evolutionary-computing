def sort_population(members):
    # sort population members in ascending order
    sorted_population = sorted(
        members,
        key=lambda member: member.value
    )
    return sorted_population
