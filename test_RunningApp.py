import unittest, numpy as np
from RunningApp import RunningApp

# Format of RunningApp(miles, minutes, hearrate (BPM))
class test_RunningApp(unittest.TestCase):

    #Use set_miles() to set miles equal to 3 and then use get_miles() to see if both functions worked.
    def test_set_get_miles(self):
        Run = RunningApp()
        Run.set_miles(3)
        Result=Run.get_miles()
        self.assertEqual(Result, 3)

    #Use set_kilometers to set kilometers equal to 3 and then use get_kilometers() to see if both functions worked.
    def test_get_kilometers(self):
        Run = RunningApp()
        Run.set_kilometers(3)
        Result = Run.get_kilometers()
        self.assertEqual(Result, 3)

    #As you may have noticed before, there is no place to insert kilometers in the constructor, only with set_kilometers().
    #make a private function called mi_to_km(). This function will be called whenever get_kilometers() is called.
    # HINT: 1 mile = 1.6km
    def test_mi_to_km(self):
        Run = RunningApp(5)
        result = Run.get_kilometers()
        self.assertEqual(result, 8)

    # HINT: Same thing as before but backwards.
    def test_km_to_mi(self):
        Run = RunningApp()
        Run.set_kilometers(5)
        result=Run.get_miles()
        self.assertEqual(result, np.float32(3.125))

    #Pace is minutes per mile. Make a function called pace_mi which returns the amount of minutes per mile.
    def test_pace_mi(self):
        Run=RunningApp(3,21)
        result=Run.pace_mi()
        self.assertEqual(result, 7)

    # Hint: Same idea as before.
    def test_pace_km(self):
        Run=RunningApp(3,21)
        result=Run.pace_km()
        self.assertEqual(result, 4.375)

    #HINT:Look at the expected result string to understand how the print_run() function should format it's output string.
    def test_print_run(self):
        Run=RunningApp(2, 15, 110)
        Result=Run.run_summary()
        self.assertEqual(Result, "Summary:\n" \
                                 "Distance: 2 miles / 3.2 kilometers\n" \
                                 "Pace: 7.5 minutes per mile / 4.6875 minutes per kilometer\n" \
                                 "Heart rate was 110bpm")

if __name__ == '__main__':
    unittest.main()