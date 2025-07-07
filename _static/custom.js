// _static/custom.js
document.addEventListener("DOMContentLoaded", function () {
  const menuItems = document.querySelectorAll('.wy-menu-vertical .toctree-l1');

  menuItems.forEach(function(item) {
    const subMenu = item.querySelector('ul');

    if (subMenu && !item.querySelector('.toctree-expand')) {
      // Add + icon span manually
      const expandSpan = document.createElement('span');
      expandSpan.className = 'toctree-expand';
      expandSpan.textContent = '+';
      item.insertBefore(expandSpan, item.firstChild);
    }
  });
});
