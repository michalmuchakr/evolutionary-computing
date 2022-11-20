def sort_population(members):
    # TODO max vs min update
    # sort population members in ascending order
    sorted_population = sorted(
        members,
        key=lambda member: member.value
    )
    return sorted_population
