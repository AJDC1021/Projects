class Statistics:
    def __init__(self,  ages: list):
        self.ages = ages
    
    def count(self):
        count = str(len(self.ages))
        return count
    
    def sum(self):
        summation = sum(self.ages)
        return summation

    def min(self):
        minimum = min(self.ages)
        self.min_value = min(self.ages)
        return minimum

    def max(self):
        maximum = max(self.ages)
        return maximum

    def range(self):
        range_of_list = max(self.ages)-min(self.ages)
        return range_of_list
    
    def mean(self):
        mean_no = round(sum(self.ages)/len(self.ages))
        return mean_no

    
    def median(self):
        median_idx = (len(self.ages) // 2)
        sorted_ages = sorted(self.ages)
        median_no = sorted_ages[median_idx]
        return median_no

    def mode(self):
        mode_list = []
        amount_dict = {}
        distinct_ages = list(dict.fromkeys(self.ages))

        for age in distinct_ages:
            temp = self.ages.count(age)
            amount_dict[age] = temp
        max_amount = max(list(amount_dict.values()))

        for key, value in amount_dict.items():
            if value == max_amount:
                mode_list.append(key)
        
        if len(mode_list) == 1:
            return (mode_list[0], max_amount)
            
        elif len(mode_list) > 1:
            all_modes = []
            for modes in mode_list:
                tuple_mode = (modes, max_amount)
                all_modes.append(tuple_mode)
            return all_modes
        else:
            return "None"     
    
    def variance(self):
        mean = sum(self.ages)/len(self.ages)
        summation = 0
        for age in self.ages:
            summation += (age-mean)**2
        variance_no = round((summation/len(self.ages)), 1)
        return variance_no
    
    def standard_dev(self):
        variance = self.variance()
        sd = round((variance**(1/2)),1)
        return sd
    
    def frequency(self):
        amount = len(self.ages)
        unique_ages = list(dict.fromkeys(ages))
        frequency_list = []
        for age in unique_ages:
            freq = round(((self.ages.count(age))/amount)*100,1)
            freq_tuple = (freq, age)
            frequency_list.append(freq_tuple)
        return frequency_list

    def describe(self):
        return (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {self.mean()}\n"
            f"Median: {self.median()}\n"
            f"Mode: {self.mode()}\n"
            f"Variance: {self.variance()}\n"
            f"Standard deviation: {self.standard_dev()}\n"
            f"Frequency distribution: {self.frequency()}"
        )
    

ages = [31, 26, 34, 37, 27, 26, 27, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(data.describe())