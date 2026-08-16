import SwiftUI

struct Habit: Identifiable {
    let id = UUID()
    var title: String
    var completedToday = false
    var streak = 0
}

struct FocusHabitView: View {
    @State private var habits = [Habit(title: "Study for 25 minutes")]

    var body: some View {
        NavigationStack {
            List($habits) { $habit in
                HStack {
                    Button { habit.completedToday.toggle(); if habit.completedToday { habit.streak += 1 } }
                    label: { Image(systemName: habit.completedToday ? "checkmark.circle.fill" : "circle") }
                    VStack(alignment: .leading) {
                        Text(habit.title)
                        Text("Streak: \(habit.streak) days").font(.caption).foregroundStyle(.secondary)
                    }
                }
                .accessibilityLabel("\(habit.title), streak \(habit.streak) days")
            }
            .navigationTitle("FocusHabit")
        }
    }
}
