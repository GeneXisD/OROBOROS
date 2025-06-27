import subprocess

AGENTS = {
   "atlas": "python3 atlas_agent.py",
   "gesture": "python3 gesture_listener.py"
}

def summon_oroboros():
   print("[OROBOROS] Summoning ritual agents...")
   for name, cmd in AGENTS.items():
       print(f"[OROBOROS] Launching {name}...")
       subprocess.Popen(cmd, shell=True)

if __name__ == "__main__":
   summon_oroboros()
