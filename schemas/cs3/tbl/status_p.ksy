meta:
  id: status_p
  endian: le
  encoding: UTF-8
  imports:
    - /components/cs3/character
    - status
seq:
  - id: character_id
    type: character
  - id: status
    type: status
