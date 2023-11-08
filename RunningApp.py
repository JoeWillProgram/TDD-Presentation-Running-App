import numpy as np
class RunningApp:
    def __init__(self, miles=None, minutes=None, heart_rate=None):
        self.miles=miles
        self.kilometers=None
        self.minutes=minutes
        self.heart_rate=heart_rate

    def set_miles(self, input_miles):
        self.miles = input_miles
        self.kilometers = self.__mi_to_km()

    def set_kilometers(self, input_kilometers):
        self.kilometers = input_kilometers
        self.miles = self.__km_to_mi()

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
        if self.kilometers == None:
            self.kilometers=self.__mi_to_km()
        return self.kilometers

    def get_minutes(self):
        return self.minutes

    def get_heart_rate(self):
        return self.heart_rate

    def __km_to_mi(self):
        if self.kilometers==None:
            raise Exception("No kilometers entered, kilometers is nonetype.")
        return np.float32(self.kilometers/1.6)

    # Parameters:mile
    # Will take in miles and return the distance as kilometers.
    def __mi_to_km(self):
        if self.miles==None:
            raise Exception("No miles entered, miles is nonetype. Miles: ")
        return np.float32(self.miles*1.6)

    def pace_mi(self):
        if self.miles == None:
            raise Exception("No miles entered, miles is nonetype.")
        if self.minutes == None:
            raise Exception("No minutes entered, minutes is nonetype.")
        return np.float32(self.minutes/self.miles)

    def pace_km(self):
        if self.kilometers==None:
            self.set_kilometers(self.__mi_to_km())
        if self.minutes == None:
            raise Exception("No minutes entered, minutes is nonetype.")
        return np.float32(self.minutes/self.kilometers)

    def run_summary(self):
        # NOTE: For whatever reason, whenever self.get_kilometers() is used in an F-String it breaks the float32 decimal
        # and makes it have more decimal points than it actually has, this was fixed in other uses by using float32, IDK why here.
        string_km=str(self.get_kilometers())
        output = "Summary:\n" \
                 f"Distance: {self.get_miles()} miles / {string_km} kilometers\n" \
                 f"Pace: {self.pace_mi()} minutes per mile / {self.pace_km()} minutes per kilometer\n" \
                 f"Heart rate was {self.get_heart_rate()}bpm"
        return output


