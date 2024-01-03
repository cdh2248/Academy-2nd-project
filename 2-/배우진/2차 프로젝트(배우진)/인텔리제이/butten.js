const addButton = document.querySelector('#add-button');

addButton.addEventListener('click', () => {
    const input = document.querySelector('#input');
    const text = input.value.trim();

    if (text !== '') {
        addToList(text);
        input.value = '';
        input.focus();
    }
});

function addToList(text) {
    const list = document.querySelector('#list');

    const newListItem = document.createElement('li');
    const newDIV = document.createElement('div');
    newListItem.classList.add('list-item');

    newListItem.innerHTML = text;
    newDIV.innerHTML = text;
    list.appendChild(newListItem);
    list.appendChild(newDIV);
}