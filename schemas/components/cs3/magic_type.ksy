meta:
  id: magic_type
  endian: le
seq:
  - id: type_id
    type: u1
    enum: magic_types
enums:
  magic_types:
    0: no_interaction # move, item use, enhance, triple advantage bonus damage, ...
    1: attack
    2: debuff # Chrono Break, analyze, various Dector crafts
    3: heal
    4: buff
    5: brave_order