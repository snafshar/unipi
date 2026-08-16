class FocusDesk {
  constructor() { this.tasks = []; this.session = null; }
  addTask(title, priority = 'normal') {
    if (!title.trim()) throw new Error('A task title is required');
    const task = { id: this.tasks.length + 1, title, priority, done: false };
    this.tasks.push(task); return task;
  }
  start(taskId, minutes = 25) {
    if (!this.tasks.some(task => task.id === taskId)) throw new Error('Unknown task');
    this.session = { taskId, remainingSeconds: minutes * 60, state: 'running' };
    return this.session;
  }
  complete(taskId) {
    const task = this.tasks.find(item => item.id === taskId);
    if (!task) throw new Error('Unknown task');
    task.done = true; if (this.session?.taskId === taskId) this.session = null;
    return task;
  }
  progress() { return this.tasks.length ? this.tasks.filter(t => t.done).length / this.tasks.length : 0; }
}

if (require.main === module) {
  const app = new FocusDesk(); const task = app.addTask('Implement the first vertical slice', 'high');
  app.start(task.id, 25); app.complete(task.id);
  console.log({ tasks: app.tasks, progress: app.progress() });
}

module.exports = { FocusDesk };
