import random
import time
import matplotlib.pyplot as plt
import numpy as np

class ArrayAnalyzer:
    def __init__(self, stambuk="028"):
        self.max_value = 250 - int(stambuk)
        random.seed(28) 
        
    def generate_array(self, n):
        return [random.randint(1, self.max_value) for _ in range(n)]
    
    def check_uniqueness(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return False
            seen.add(num)
        return True
    
    def calculate_worst_case(self, n):
        return n * n
    
    def calculate_average_case(self, n):
        return n * np.log2(n)
    
    def analyze_arrays(self):
        n_values = [100, 150, 200, 250, 300, 350, 400, 500]
        worst_cases = []
        avg_cases = []
        
        # Calculate cases
        for n in n_values:
            worst_cases.append(self.calculate_worst_case(n))
            avg_cases.append(self.calculate_average_case(n))
            
            # Generate and test array
            arr = self.generate_array(n)
            is_unique = self.check_uniqueness(arr)
            print(f"\nArray size {n}:")
            print(f"First 10 elements: {arr[:10]}...")
            print(f"Is unique: {is_unique}")
        
        # Save results to file
        with open("worst_avg.txt", "w") as f:
            f.write("Analysis Results\n")
            f.write("===============\n\n")
            for i, n in enumerate(n_values):
                f.write(f"n = {n}:\n")
                f.write(f"Worst Case: {worst_cases[i]:.2f}\n")
                f.write(f"Average Case: {avg_cases[i]:.2f}\n\n")
        
        # Create plot
        plt.figure(figsize=(12, 8))
        plt.plot(n_values, worst_cases, 'r-', label='Worst Case (O(n²))')
        plt.plot(n_values, avg_cases, 'b-', label='Average Case (O(n log n))')
        plt.xlabel('Array Size (n)')
        plt.ylabel('Time Complexity')
        plt.title('Time Complexity Analysis')
        plt.legend()
        plt.grid(True)
        plt.savefig('complexity_analysis.pdf')
        plt.savefig('complexity_analysis.jpg')
        plt.close()

def main():
    
    analyzer = ArrayAnalyzer() 
    analyzer.analyze_arrays()

if __name__ == "__main__":
    main()