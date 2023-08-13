import time

def spped_test():
    text = "The quick brown fox jumps over the lazy dog."
    
    print("Type the following sentence:")
    print(text)
    
    input("Press Enter to start...")
    
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    words = len(text.split())
    characters = len(text)
    wpm = words / (elapsed_time / 60)
    cpm = characters / (elapsed_time / 60)
    
    print("--- Results ---")
    print("Time elapsed: {:.2f} seconds".format(elapsed_time))
    print("Words per minute: {:.2f} wpm".format(wpm))
    print("Characters per minute: {:.2f} cpm".format(cpm))

spped_test()