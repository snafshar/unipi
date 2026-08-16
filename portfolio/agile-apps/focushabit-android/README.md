# FocusHabit Android

I implemented the Android version as a Kotlin and Jetpack Compose companion to
the iOS application. I kept the product behaviour identical while allowing
each platform to use its native UI conventions.

## Agile product slice

**Story:** As a student, I want to complete today's habit with one tap and see
my streak immediately.

**Acceptance criteria:** the state changes instantly, the completed state is
visible after recomposition, and the screen has a meaningful content
description for accessibility tools.

**Next sprint:** Room persistence, WorkManager reminders, UI tests, and a
weekly progress screen.

## Run

Place `MainActivity.kt` in a new Android Studio Compose project and run it on an
Android emulator or device.
