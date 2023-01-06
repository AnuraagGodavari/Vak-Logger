import os

#Filenames
logpwdir = f"{os.path.dirname(__file__)}/../.."

if not os.path.exists(f"{logpwdir}/Logs"):
    os.makedirs(f"{logpwdir}/Logs")
    
logs_dir = f"{logpwdir}/Logs"
masterlog = f"{logpwdir}/Logs/current.log"