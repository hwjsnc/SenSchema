meta:
  id: magicbo
  endian: le
seq:
  - id: magic_id
    type: u2
  - id: unknown_data
    type: u1
    repeat: expr
    repeat-expr: 72
