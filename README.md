# Keylogger using Python: Proof of Concept

**Description:** This python script logs every keystroke on the system to an output file whose path is `filename`, which the user can change as per their needs.

## Requirements
- Python 3.12.x interpreter must be installed
- `pynput` module (install with `pip install pynput`)

## Usage
Run the following in terminal:
```
python <path-to-script>/keylogger.py
```
The script will start executing and the output file will be updated every 5 seconds. The rate of update can be changed by changing the interval parameter in line:25
```
25        threading.Timer(interval=5.0, function=log, args=(filename, )).start()
```

## Important
This tool is developed only for educational purposes and as a proof of concept.
