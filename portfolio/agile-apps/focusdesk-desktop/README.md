# FocusDesk — Desktop Focus Planner

I built FocusDesk as a cross-platform desktop planner for students and
developers who need to organise focused work without losing sight of the
larger project. The target platforms are macOS and Windows.

## Product goal

Help me convert a large task into a small, visible work session and review what
I actually completed.

## Agile plan

**MVP user story:** As a student, I want to create a task, start a focus
session, and mark the task complete so that I can make measurable progress.

**Acceptance criteria:**

- A task has a title, priority, and completion state.
- Starting a session shows remaining time and survives window resizing.
- Completing a task updates the daily progress summary.
- Data is stored locally and remains available after restarting the app.

**Sprint 1:** task model, local persistence, task list, and timer vertical slice.  
**Sprint 2:** keyboard shortcuts, filtering, accessibility, and export.  
**Sprint 3:** packaging, automated tests, and macOS/Windows release builds.

## Architecture decision

I kept the domain model independent from the UI so that the same behaviour can
be tested on both operating systems. The current prototype uses a small
dependency-free TypeScript core that can be embedded in a desktop shell such
as Tauri or Electron.

## Retrospective

My main lesson from the first slice was that timer state must be represented as
data rather than inferred from UI events. That makes pause, resume, restart,
and test scenarios predictable.

## Run the prototype

```bash
node focusdesk.js
```
