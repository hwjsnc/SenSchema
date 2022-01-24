meta:
  id: item_help_data
  endian: le
  encoding: UTF-8
doc: |
  Effect descriptions used for autogeneration of item/art/etc descriptions.

  Present in t_itemhelp.tbl.
seq:
  - id: effect_id
    type: u2
  - id: text
    type: strz
  - id: unknown_data
    type: u1
    repeat: expr
    repeat-expr: 9
