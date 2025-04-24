document.addEventListener("DOMContentLoaded", () => {
  const darkModeToggle = document.getElementById("dark-mode-toggle");
  if (!darkModeToggle) return;

  const body = document.body;

  if (localStorage.getItem("darkMode") === "enabled") {
    body.classList.add("dark-theme");
    darkModeToggle.textContent = "☀️";
  } else {
    body.classList.add("light-theme");
    darkModeToggle.textContent = "🌙";
  }

  const toggleDarkMode = () => {
    if (body.classList.contains("dark-theme")) {
      body.classList.remove("dark-theme");
      body.classList.add("light-theme");
      darkModeToggle.textContent = "🌙";
      localStorage.setItem("darkMode", "disabled");
    } else {
      body.classList.remove("light-theme");
      body.classList.add("dark-theme");
      darkModeToggle.textContent = "☀️";
      localStorage.setItem("darkMode", "enabled");
    }
  };

  darkModeToggle.addEventListener("click", toggleDarkMode);

  // Ensure proper cleanup for BFCache compatibility
  window.addEventListener("pagehide", () => {
    darkModeToggle.removeEventListener("click", toggleDarkMode);
  });
});

litigation
