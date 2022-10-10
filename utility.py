def split_list_into_chunks(list_to_split, chunk_size):
    chunked_list = list()

    for i in range(0, len(list_to_split), chunk_size):
        chunked_list.append(list_to_split[i:i + chunk_size])

    return chunked_list
