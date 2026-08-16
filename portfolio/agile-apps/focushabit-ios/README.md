# FocusHabit iOS

I designed this iOS application as a lightweight habit and study tracker. I
used SwiftUI because the screen can be derived directly from observable state,
which keeps the first vertical slice small and testable.

## Agile product slice

**Story:** As a student, I want to check off today's study habit and see my
weekly streak so that I can maintain a consistent routine.

**MVP acceptance criteria:** a habit can be created, today's completion can be
toggled, and the streak changes only once per calendar day.

**Backlog:** local persistence, reminder notifications, accessibility labels,
weekly charts, and optional iCloud synchronisation.

## Run

Open `FocusHabit.swift` in an Xcode SwiftUI iOS project. The view is deliberately
small: I would add persistence and notifications in the next sprint after
validating the interaction with users.
