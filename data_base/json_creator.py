import ski_resorts
import cultural_resorts
import json


def one_dict(dict_1, dict_2):
    """
    (dict, dict) -> dict

    Return the dictionary with structure for json file.
    """
    dict_for_json = dict()
    dict_for_json['cultural resorts'] = dict_1
    dict_for_json['ski resorts'] = dict_2
    return dict_for_json


def json_write(dictionary):
    """
    (dict) -> None

    Write information to json file.
    """
    with open('data.json', 'w') as f:
        json.dump(dictionary, f, indent=4)


if __name__ == "__main__":
    dict_1 = cultural_resorts.dict_conecter_cultural(cultural_resorts.many_resorts(), cultural_resorts.few_resorts())
    dict_2 = ski_resorts.dict_conecter_ski(ski_resorts.ski_resorts(), ski_resorts.austria_resorts())
    dictionary = one_dict(dict_1, dict_2)
    json_write(dictionary)