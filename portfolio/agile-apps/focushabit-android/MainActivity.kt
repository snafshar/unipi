package com.example.focushabit

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { FocusHabitScreen() }
    }
}

@Composable
fun FocusHabitScreen() {
    var completed by remember { mutableStateOf(false) }
    var streak by remember { mutableIntStateOf(0) }
    Column(Modifier.padding(24.dp)) {
        Text("FocusHabit", style = MaterialTheme.typography.headlineMedium)
        Spacer(Modifier.height(24.dp))
        Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
            Button(onClick = { completed = !completed; if (completed) streak++ }) {
                Text(if (completed) "Completed" else "Complete study habit")
            }
            Text("Streak: $streak", modifier = Modifier.padding(top = 12.dp))
        }
    }
}
