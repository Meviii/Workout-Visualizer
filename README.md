# Workout Visualizer

## What is this?

This application is intended for those who don't want to bother with excel when creating there workout plans. The application has an easy-to-use GUI which allows for additions of workouts and there exercises. On creation, an Excel document will be outputted with auto formated workouts and exercises. 

## Running as EXE

The updated application exe can be found in the __dist__ folder.

## TODOs

- Option for different style of workout(treadmill, mins, etc)
- Show where Excel file is created.
- Change exercises to a list view
- Add delete/duplicate buttons to workouts
- Add clear one for removing one workout
- Possiblity to add background colour to workout and a background colour for all workouts
- Style/theme flexibility

## Constraints

- Make sure the "output" excel file is closed.
- A day cannot have two workouts with the same name
- Better to split up specific exercises into separate workouts (Eg. Chest. And not Chest & Triceps)

## Bugs

- Using create button twice (when it should be possible) will crash the program in the exe version
- Data is not persisted in the exe version