import numpy as np
class RunningApp:
    def __init__(self, miles=None, minutes=None, heart_rate=None):
        self.miles=miles
        self.kilometers=None
        self.minutes=minutes
        self.heart_rate=heart_rate

    def set_miles(self, input_miles):
        self.miles = input_miles

    def set_kilometers(self, input_kilometers):
        self.kilometers = input_kilometers

    def set_minutes(self, input_minutes):
        self.minutes = input_minutes

    def set_minutes(self, input_kilometers):
        self.kilometers = input_kilometers

    def set_heart_rate(self, input_heart_rate):
        self.heart_rate=input_heart_rate

    def get_miles(self):
        if self.miles==None:
            raise Exception("No miles entered, miles is nonetype.")
        return self.miles

    def get_kilometers(self):
        if self.miles == None:
            raise Exception("No miles entered, miles is nonetype. Kilometers are automatically gotten through conversion of miles.")
        return self.kilometers

    def get_minutes(self):
        return self.minutes

    def get_heart_rate(self):
        return self.heart_rate

    def __km_to_mi(self):
        pass

    def __mi_to_km(self):
        pass

    def pace_mi(self):
        pass

    def pace_km(self):
        pass

    def run_summary(self):
        # NOTE: Use str() around kilometers, otherwise it breaks. I have no idea why it does this.
        pass


