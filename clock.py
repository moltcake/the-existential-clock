import time

import random



def start_existential_crisis():
  
    print("Welcome to the Existential Clock.")
  
    print("This tool tracks the time you are successfully wasting.")
  


    start_time = time.time()
  
    excuses = [
      
        "Thinking about that one time you said 'You too' to a waiter.",
      
        "Wondering if your cat actually likes you.",
      
        "Considering starting a podcast about grass.",
      
        "Refreshing your email for no reason.",
      
        "Reading a README for a tool that does nothing."
      
    ]
  


    try:
      
        while True:
          
            elapsed = int(time.time() - start_time)
          
            activity = random.choice(excuses)
          
            print(f"\r[Wasted: {elapsed}s] Current Activity: {activity}", end='')
          
            time.sleep(2)
          
    except KeyboardInterrupt:
      
        print(f"\nCongratulations! You wasted {int(time.time() - start_time)} seconds.")
      
        print("Go do something productive. Or don't. I'm just a script.")
      


if __name__ == '__main__':
  
    start_existential_crisis()




















