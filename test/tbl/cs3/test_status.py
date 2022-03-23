import struct
import unittest
import cs3tbl


def cast_to_float(x):
    # Python floats are doubles while the tbls contain single-precision floats, so we need to do correct rounding explicitely
    return struct.unpack("f", struct.pack("f", x))[0]


class TestCS3Status(unittest.TestCase):
    def setUp(self):
        self.tbl = cs3tbl.Cs3.from_file("data/cs3/status.tbl")

    def testHeader(self):
        (header,) = self.tbl.header_extra.headers
        self.assertEqual(header.header_name, "status")
        self.assertEqual(header.num_entry, 1)

    def testEntries(self):
        (entry,) = self.tbl.entries
        self.assertEqual(entry.data.script, "mon000")
        self.assertEqual(entry.data.texture, "C_MON000")
        self.assertEqual(entry.data.model, "mon000")
        self.assertEqual(entry.data.model_scale, cast_to_float(1.0))
        self.assertEqual(entry.data.camera_pivot_height, cast_to_float(0.9))
        self.assertEqual(entry.data.hitbox_size, cast_to_float(0.75))
        self.assertEqual(entry.data.unknown_float_1, cast_to_float(4.0))
        self.assertEqual(entry.data.unknown_float_2, cast_to_float(1.8))
        self.assertEqual(entry.data.unknown_float_3, cast_to_float(6.0))
        self.assertEqual(entry.data.unknown_float_4, cast_to_float(24.0))
        self.assertEqual(entry.data.unknown_short_1, 6)
        self.assertEqual(entry.data.unknown_short_2, 1)
        self.assertEqual(entry.data.is_female, 0)
        self.assertEqual(entry.data.level, 7)
        self.assertEqual(entry.data.hp_base, 123)
        self.assertEqual(entry.data.hp_growth, cast_to_float(119))
        self.assertEqual(entry.data.max_ep, 400)
        self.assertEqual(entry.data.start_ep, 400)
        self.assertEqual(entry.data.max_cp, 200)
        self.assertEqual(entry.data.start_cp, 0)
        self.assertEqual(entry.data.str_base, 48)
        self.assertEqual(entry.data.str_growth, cast_to_float(20))
        self.assertEqual(entry.data.def_base, 69)
        self.assertEqual(entry.data.def_growth, cast_to_float(30))
        self.assertEqual(entry.data.ats_base, 58)
        self.assertEqual(entry.data.ats_growth, cast_to_float(20))
        self.assertEqual(entry.data.adf_base, 60)
        self.assertEqual(entry.data.adf_growth, cast_to_float(15))
        self.assertEqual(entry.data.dex_base, 80)
        self.assertEqual(entry.data.dex_growth, cast_to_float(0.2))
        self.assertEqual(entry.data.agl_base, 15)
        self.assertEqual(entry.data.agl_growth, cast_to_float(0.1))
        self.assertEqual(entry.data.eva, 0)
        self.assertEqual(entry.data.spd_base, 42)
        self.assertEqual(entry.data.spd_growth, cast_to_float(0.5))
        self.assertEqual(entry.data.mov_base, 6)
        self.assertEqual(entry.data.mov_growth, cast_to_float(0))
        self.assertEqual(entry.data.exp_base, 64)
        self.assertEqual(entry.data.exp_growth, cast_to_float(4))
        self.assertEqual(entry.data.break_multiplier_base, 120)
        self.assertEqual(entry.data.break_multiplier_growth, cast_to_float(0))
        self.assertEqual(entry.data.earth_efficacy, 160)
        self.assertEqual(entry.data.water_efficacy, 180)
        self.assertEqual(entry.data.fire_efficacy, 80)
        self.assertEqual(entry.data.wind_efficacy, 140)
        self.assertEqual(entry.data.time_efficacy, 180)
        self.assertEqual(entry.data.space_efficacy, 60)
        self.assertEqual(entry.data.mirage_efficacy, 200)
        self.assertEqual(entry.data.psn_efficacy, 150)
        self.assertEqual(entry.data.seal_efficacy, 180)
        self.assertEqual(entry.data.mute_efficacy, 200)
        self.assertEqual(entry.data.blnd_efficacy, 140)
        self.assertEqual(entry.data.slp_efficacy, 120)
        self.assertEqual(entry.data.burn_efficacy, 160)
        self.assertEqual(entry.data.frz_efficacy, 100)
        self.assertEqual(entry.data.petr_efficacy, 150)
        self.assertEqual(entry.data.fnt_efficacy, 90)
        self.assertEqual(entry.data.conf_efficacy, 140)
        self.assertEqual(entry.data.chrm_efficacy, 200)
        self.assertEqual(entry.data.dblw_efficacy, 150)
        self.assertEqual(entry.data.nmr_efficacy, 180)
        self.assertEqual(entry.data.dlay_efficacy, 80)
        self.assertEqual(entry.data.vnsh_efficacy, 100)
        self.assertEqual(entry.data.s_dwn_efficacy, 160)
        self.assertEqual(entry.data.slash_efficacy, 50)
        self.assertEqual(entry.data.thrust_efficacy, 150)
        self.assertEqual(entry.data.pierce_efficacy, 100)
        self.assertEqual(entry.data.strike_efficacy, 400)
        self.assertEqual(entry.data.earth_sepith_base, 3)
        self.assertEqual(entry.data.water_sepith_base, 1)
        self.assertEqual(entry.data.fire_sepith_base, 4)
        self.assertEqual(entry.data.wind_sepith_base, 2)
        self.assertEqual(entry.data.time_sepith_base, 5)
        self.assertEqual(entry.data.space_sepith_base, 4)
        self.assertEqual(entry.data.mirage_sepith_base, 3)
        self.assertEqual(entry.data.sepith_mass_base, 4)
        self.assertEqual(entry.data.earth_sepith_growth, cast_to_float(0.05))
        self.assertEqual(entry.data.water_sepith_growth, cast_to_float(0))
        self.assertEqual(entry.data.fire_sepith_growth, cast_to_float(0.15))
        self.assertEqual(entry.data.wind_sepith_growth, cast_to_float(0.1))
        self.assertEqual(entry.data.time_sepith_growth, cast_to_float(0.075))
        self.assertEqual(entry.data.space_sepith_growth, cast_to_float(0))
        self.assertEqual(entry.data.mirage_sepith_growth, cast_to_float(0.3))
        self.assertEqual(entry.data.sepith_mass_growth, cast_to_float(0.9))
        self.assertEqual(entry.data.drop_id_1, 3112)
        self.assertEqual(entry.data.drop_chance_1, 20)
        self.assertEqual(entry.data.drop_id_2, 60)
        self.assertEqual(entry.data.drop_chance_2, 40)
        self.assertEqual(entry.data.monster_variation_min, cast_to_float(0.9))
        self.assertEqual(entry.data.monster_variation_max, cast_to_float(1.1))
        self.assertEqual(entry.data.flags, "M")
        self.assertEqual(entry.data.name, "Monster Name")
        self.assertEqual(
            entry.data.description,
            "Description line 1\nDescription line 2\nDescription line 3\nDescription line 4",
        )
