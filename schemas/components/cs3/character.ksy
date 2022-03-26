meta:
  id: character
  endian: le
seq:
  - id: character_id
    type: u2
    enum: characters
enums:
  characters:
    0: rean
    1: alisa
    2: elliot
    3: laura
    4: machias
    5: emma
    6: jusis
    7: fie
    8: gaius
    9: millium
    10: juna
    11: kurt
    12: altina
    13: musse
    14: ash
    15: sara
    16: aurelia
    17: agate
    18: angelica
    19: olivert
    20: tita
    21: tio
    22: sharon
    23: claire
    24: lechter
    25: towa
    26: patrick
    200: jessica
    61696: male_only
    61697: female_only
    # the following values are probably garbage because they only appear for a few books and a VM card
    61699: unknown_3
    61700: unknown_4
    61701: unknown_5
    61702: unknown_6
    61703: unknown_7
    61704: unknown_8
    61705: unknown_9
    61706: unknown_10
    61707: unknown_11
    61708: unknown_12
    65535: no_restriction
