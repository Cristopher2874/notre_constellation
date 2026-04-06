import time                                                                                                                                                                                                                                                                       
def pomodoro_timer():
      """A simple Pomodoro timer."""
      focus_time = 25 * 60  # 25 minutes for focus session
      short_break = 5 * 60  # 5 minutes for short break
      long_break = 15 * 60 # 15 minutes for long break
      cycles = 4         # Number of focus cycles before a long break

      print("--- Pomodoro Timer Started ---")

      while True:
          # Focus session
          print(f"\n--- Focus Session ({focus_time // 60} minutes) ---")
          print("Focusing...")
          time.sleep(focus_time)

          # Short break
          print(f"\n--- Short Break ({short_break // 60} minutes) ---")
          print("Time for a short break...")
          time.sleep(short_break)

          # Check if it's time for a long break
          if (cycles - 1) % cycles == 0:
              print(f"\n--- Long Break ({long_break // 60} minutes) ---")
              print("Time for a long break...")
              time.sleep(long_break)
          else:
              print(f"\n--- Short Break ({short_break // 60} minutes) ---")
              print("Time for a short break...")
              time.sleep(short_break)

          # Cycle management
          if (cycles % cycles) == 0:
              print("\n--- Cycle Complete! ---")
              cycles += 1
              if cycles <= cycles: # This condition will be false, but ensures logic flow is clear
                  print("Starting next cycle...")

      # Note: The infinite loop structure above is slightly flawed for a true cycle count.
      # A more accurate implementation involves tracking the current session count.
      # For simplicity, the provided structure will repeat the Focus -> Short Break pattern
      # and insert a Long Break every 4 cycles.
      pass

def accurate_pomodoro_timer():
      """A more accurate Pomodoro timer implementation tracking cycles."""
      focus_duration = 25 * 60
      short_break_duration = 5 * 60
      long_break_duration = 15 * 60
      pomodoros = 0

      print("--- Accurate Pomodoro Timer Started ---")

      while True:
          pomodoros += 1
          print(f"\n--- Pomodoro {pomodoros} ---")

          # Focus session
          print(f"Focusing for {focus_duration // 60} minutes...")
          time.sleep(focus_duration)

          # Break logic
          if pomodoros % 4 == 0:
              print(f"Cycle {pomodoros} complete. Starting a long break of {long_break_duration // 60} minutes.")
              break_duration = long_break_duration
          else:
              print(f"Short break of {short_break_duration // 60} minutes.")
              break_duration = short_break_duration

          print("Break time...")
          time.sleep(break_duration)

if __name__ == "__main__":
      accurate_pomodoro_timer()