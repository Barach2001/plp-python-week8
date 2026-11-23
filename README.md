# Personal Mini-Toolkit

A beginner-friendly Python command-line program created for the PLP Future Proof With Python Week 8 final project.

## What the toolkit does

The program has a menu with three tools:

1. **Study Task List** — add study tasks and view the tasks stored while the program is running.
2. **Grade Average Calculator** — enter scores from 0 to 100 and calculate the average.
3. **Basic Calculator** — add, subtract, multiply, or divide two numbers.

The main menu keeps running until the user selects **4. Quit**. Invalid input is handled with helpful messages.

## Files in this project

- `toolkit_plan.txt` — program plan, menu flow, data structures, and testing checklist.
- `toolkit.py` — Python source code.
- `screenshots/` — sample console-run screenshots for the menu, invalid choice, and each tool.
- `README.md` — project overview and instructions.

## How to run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python toolkit.py
```

On some computers, use `python3 toolkit.py` instead.

## Reflection (edit this to match your own experience)

The most challenging part of this project was organizing the tools so that each one could return to the main menu. Checking user input also required careful testing because users may enter letters or numbers outside the accepted range. One bug that took time to track down was making sure invalid input did not stop the program unexpectedly. I used loops to keep asking for valid information and conditions to decide what should happen next. I also used a list so study tasks could be added and displayed while the program was running. If I had one more week, I would add a way to save tasks in a file so they are still available after the program closes.

**Before submitting:** review this reflection and change it if it does not accurately describe your own experience. Run the program yourself and replace/add screenshots captured on your own computer if your instructor expects personal execution evidence.
