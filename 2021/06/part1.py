class Fish:
    def __init__(self, ttb=8):
        self.time_to_breed = ttb

    def reproduce(self):
        if(self.time_to_breed == 0):
            self.time_to_breed=6
            return Fish(8)

        self.time_to_breed -= 1
        return False

    def __str__(self):
        return str(self.time_to_breed)

with open('input.txt') as f:
    fish_school = [Fish(int(counter)) for counter in f.readlines()[0].strip().split(',')]


    print(f"Initial State: {','.join([ str(fish) for fish in fish_school])}")
    for day in  range(1,80+1):
        for fish in fish_school[:]:
            new_fish = fish.reproduce()
            if new_fish:
                fish_school.append(new_fish)

        # print(f"After {day:2} day{'s:' if day > 1 else ': '} {','.join([ str(fish) for fish in fish_school])}")

    print(f"Total fish after {day} days: {len(fish_school)}")
