def count_vowels(word):
    # Consider both uppercase and lowercase vowels
    vowels = 'aeiouyAEIOUY'
    return sum(1 for char in word if char in vowels)

def calculate_average_vowels(filename):
   
    try:
        # Load entire file into an array of lines
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Initialize counters
        total_vowels = 0
        total_words = 0
        start_counting = False
        
        # Iterate over the array of lines
        for line in lines:
            # Start counting from "CHAPTER 1. Loomings."
            if 'CHAPTER 1. Loomings.' in line:
                start_counting = True
            
            # Skip lines before the starting point
            if not start_counting:
                continue
            
            # Clean and split the line into words
            # Remove punctuation and empty strings
            words = [word.strip('.,!?()[]{}":;') for word in line.split()]
            words = [word for word in words if word]
            
            # Count vowels in each word
            for word in words:
                if word:
                    vowel_count = count_vowels(word)
                    total_vowels += vowel_count
                    total_words += 1
        
        # Calculate and return average
        if total_words > 0:
            return total_vowels / total_words
        return 0
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    
    import os
    
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create full path to the file
    filename = os.path.join(script_dir, "pg2701.txt")
    
    # Calculate average vowels
    average_vowels = calculate_average_vowels(filename)
    
    # Print result
    if average_vowels is not None:
        print(f"Average number of vowels per word: {average_vowels:.2f}")

if __name__ == "__main__":
    main()