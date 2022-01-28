meta:
  id: magic_category
  endian: le
seq:
  - id: category_id
    type: u1
    enum: category_types
enums:
  category_types:
    1: attack
    2: counter
    3: move
    4: use_item
    5: ailment_penalty
    #6: unused
    7: flee
    8: advantage_damage
    #9: unused
    10: link_support_1
    11: link_support_2
    12: link_support_3
    20: art
    #21: unused
    22: mech_art
    # 23-29: unused
    30: craft
    31: s_craft
    32: brave_order
