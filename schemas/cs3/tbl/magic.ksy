meta:
  id: magic
  endian: le
  encoding: UTF-8
  imports:
    - /components/cs3/character
    - /components/cs3/magic_category
    - /components/cs3/effect
    - /components/common/element
    - /components/common/target_types
seq:
  - id: magic_id
    type: u2
  - id: character_restriction
    type: character
  - id: flags
    type: strz
  - id: category
    type: magic_category
  - id: type
    type: magic_type
  - id: element
    type: u1 # Can't use element since it's u2
  - id: juna_specific
    type: u1
  - id: target_type
    type: target_type
  - id: target_range
    type: f4
  - id: target_size
    type: u1
  - id: unknown_float_1
    type: f4
  - id: unknown_float_2
    type: f4
  - id: unknown_float_3
    type: f4
  - id: effects
    type: effect
    repeat: expr
    repeat-expr: 5
  - id: cast_delay
    type: u1
  - id: recovery_delay
    type: u1
  - id: cost
    type: u2
  - id: unbalance_bonus
    type: u1
  - id: break_bonus
    type: u2
  - id: level_learn
    type: u1
    doc: Level at which the craft is learned.
  - id: sort_id
    type: u2
  - id: animation
    type: strz
  - id: name
    type: strz
  - id: description
    type: strz
