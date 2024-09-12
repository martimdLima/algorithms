class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        daily_temperatures = [0] * n
        current_temps = []
        days = 0

        for idx in range(n - 1):
            day = idx
            days = 0

            if temperatures[day] < temperatures[day + 1]:
                daily_temperatures[idx] = 1
                continue

            current_temps = temperatures[day:n]

            for i in range(1, len(current_temps)):
                if current_temps[i] <= current_temps[0]:
                    days += 1
                else:
                    days += 1
                    daily_temperatures[day] = days
                    break

        return daily_temperatures

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        num_temps = len(temperatures)
        daily_temperatures = [0] * num_temps
        stack = []

        for day in range(num_temps):
            # if current temp > future temp we have found a warmer day
            while stack and temperatures[day] > temperatures[stack[-1]]:
                future_day = stack.pop()
                # calculate the difference in days
                daily_temperatures[future_day] = day - future_day
            stack.append(day)

        return daily_temperatures
