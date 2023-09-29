from src.data.data_manager import get_all_fruits, transform_listdict_to_df


def get_fruit_data(fruit_name: str):
    list_fruits = get_all_fruits(filter_name=fruit_name)
    return transform_listdict_to_df(list_fruits)
