/**
 * Filtruje zadania o statusie "completed", sortuje je według id i zwraca ich tytuły
 * @param {Array<{id: number, title: string, status: string}>} tasks - tablica zadań
 * @returns {Array<string>} - posortowane tytuły ukończonych zadań
 */
function getCompletedTaskTitles(tasks) {
  return tasks
    .filter(task => task.status === "completed")
    .sort((a, b) => a.id - b.id)
    .map(task => task.title);
}

