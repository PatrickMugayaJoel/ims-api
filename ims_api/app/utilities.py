def remove_fields(field_list, data_source):
    for field in field_list:
        data_source.pop(field)
