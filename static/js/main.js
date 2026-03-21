const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggleBtn');

    toggleBtn.addEventListener('click', () => {
        // Mobile par show/hide, Desktop par width change
        if (window.innerWidth >= 1024) {
            sidebar.classList.toggle('w-64');
            sidebar.classList.toggle('w-0');
            sidebar.classList.toggle('hidden');
        } else {
            sidebar.classList.toggle('hidden');
            sidebar.classList.add('fixed', 'inset-y-0', 'left-0', 'z-50', 'w-64');
        }
    });


  document.querySelectorAll(".menu").forEach(menu => {
    const btn = menu.querySelector(".togglemenu");
    const dropdown = menu.querySelector(".dropdown");
    const arrow = menu.querySelector(".arrow");

    btn.addEventListener("click", () => {
      dropdown.classList.toggle("hidden");
      arrow.classList.toggle("rotate-180");
    });
  });