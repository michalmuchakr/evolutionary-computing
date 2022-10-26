def split_list_into_chunks(list_to_split, chunk_size):
    return [list_to_split[index:index + chunk_size] for index in range(0, len(list_to_split), chunk_size)]
