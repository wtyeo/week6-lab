import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):
    def test_initializes_member_and_zero_balance(self):
        duck_fine = DuckFine("member-123")

        self.assertEqual(duck_fine.member_id, "member-123")
        self.assertEqual(duck_fine.total_owed, 0.0)

    def test_first_two_late_days_are_free(self):
        duck_fine = DuckFine("member-123")

        fee = duck_fine.charge(2)

        self.assertEqual(fee, 0.0)

    def test_charges_half_dollar_for_each_chargeable_day(self):
        duck_fine = DuckFine("member-123")

        fee = duck_fine.charge(4)

        self.assertEqual(fee, 1.0)

    def test_deluxe_charge_doubles_the_fee(self):
        duck_fine = DuckFine("member-123")

        fee = duck_fine.charge(4, deluxe=True)

        self.assertEqual(fee, 2.0)

    def test_single_charge_is_capped_at_maximum_fee(self):
        duck_fine = DuckFine("member-123")

        fee = duck_fine.charge(20)

        self.assertEqual(fee, DuckFine.MAX_FEE)

    def test_charges_are_added_to_total_owed(self):
        duck_fine = DuckFine("member-123")

        duck_fine.charge(4)
        duck_fine.charge(3)

        self.assertEqual(duck_fine.total_owed, 1.5)

    def test_negative_days_late_raise_value_error(self):
        duck_fine = DuckFine("member-123")

        with self.assertRaises(ValueError):
            duck_fine.charge(-1)

    def test_one_late_day_is_free(self):
        duck_fine = DuckFine("member-123")

        fee = duck_fine.charge(1)

        self.assertEqual(fee, 0.0)


if __name__ == "__main__":
    unittest.main()
