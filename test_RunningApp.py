import numpy as np
import unittest

from RunningApp import RunningApp


#Format of RunningApp(miles, minutes, heartrate (BPM))
#Getters and setters already made.
class test_RunningApp(unittest.TestCase):

    #Use set_miles() to set miles equal to 3 and then use get_miles() to see if both functions worked.
    def test_set_get_miles(self):

        self.assertEqual(Result, 3)

    #Use set_kilometers() to set kilometers equal to 3 and then use get_kilometers() to see if both functions worked.
    def test_get_kilometers(self):

        self.assertEqual(Result, 3)

    #As you may have noticed before, there is no place to insert kilometers in the constructor, only with set_kilometers().
    #Make a private function called mi_to_km(). This function will be called whenever get_kilometers() is called.
    #Return type should be np.float32().
    # HINT: 1 mile = 1.6km
    def test_mi_to_km(self):

        self.assertEqual(result, 8)

    #Make a private function called km_to_mi().
    # Return type should be np.float32().
    # HINT: Same thing as before but backwards.
    # HINT: What is 3.125 miles equal to?
    def test_km_to_mi(self):

        self.assertEqual(result, np.float32(3.125))

    #Make a function called pace_mi which returns the amount of minutes per mile.
    # NOTE: There is no seconds just minutes, so you'll get like 2.5 minutes.
    # HINT: Return type should be np.float32().
    def test_pace_mi(self):
        self.assertEqual(result, )

    #Make a function called pace_km.
    #Return type should be np.float32().
    # HINT: Same idea as before.
    def test_pace_km(self):
        self.assertEqual(result, )

    #Write a function called print run which produces of a run.
    # HINT:Look at the expected result string to understand how the print_run() function should format it's output string.
    def test_print_run(self):
        Run=RunningApp(2, 15, 110)
        Result=Run.run_summary()
        self.assertEqual(Result, "Summary:\n" \
                                 "Distance: 2 miles / 3.2 kilometers\n" \
                                 "Pace: 7.5 minutes per mile / 4.6875 minutes per kilometer\n" \
                                 "Heart rate was 110bpm")

if __name__ == '__main__':
    unittest.main()