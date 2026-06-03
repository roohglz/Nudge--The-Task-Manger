document.addEventListener("DOMContentLoaded", () => {
    const tasks = document.querySelectorAll(".task");

    tasks.forEach(task => {
        task.addEventListener("click", () => {
            task.classList.toggle("active");
        });
    });
});
