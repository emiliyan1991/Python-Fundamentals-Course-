legendary_items_dict = {'shards': 0, 'fragments': 0, "motes":0}
junk_items_dict = {}


def print_items(legendary_items_dict, junk_items_dict, special_item):
    print(f"{special_item} obtained!")
    print(f"shards: {legendary_items_dict['shards']}")
    print(f"fragments: {legendary_items_dict['fragments']}")
    print(f"motes: {legendary_items_dict['motes']}")
    for key,value in junk_items_dict.items():
        print(f"{key}: {value}")


def legendary_items():
    while_condition = False
    while True:
        items_list = (input().lower()).split(" ")
        for value,material in zip(items_list[0::2], items_list[1::2]):
            value = int(value)
            material = material.lower()

            if material in ["shards", "fragments", "motes"]:
                legendary_items_dict[material] += value

                if legendary_items_dict[material] >= 250:
                    legendary_items_dict[material] -= 250
                    special_item = ""
                    if material == "shards":
                        special_item = "Shadowmourne"
                    elif material == "fragments":
                        special_item = "Valanyr"
                    elif material == "motes":
                        special_item = "Dragonwrath"

                    while_condition = True
                    print_items(legendary_items_dict, junk_items_dict, special_item)
            else:
                if material not in junk_items_dict:
                    junk_items_dict[material] = value
                else:
                    junk_items_dict[material] += value
            if while_condition:
                break
        if while_condition:
            break

legendary_items()




