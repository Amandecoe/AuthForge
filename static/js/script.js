const sidebar = document.getElementById('sidebar')
const toggleButton = document.getElementById('toggle-btn')
function toggleSidebar(){
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')

    Array.from(sidebar.getElementsByClassName('show')).forEach(ul => {
        ul.classList.remove('show')
        ul.previousElementSibling.classList.remove('rotate')
    })
}
function moveFirstToTop() {
    const list = document.getElementById('start');
    const firstLi = list.firstElementChild; // Gets the first <li> in the list

    if (firstLi) {
    // Moves the 'firstLi' element to be the first child of 'list'
    list.prepend(firstLi);
    }
}
