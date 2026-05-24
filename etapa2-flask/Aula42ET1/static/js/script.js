const input = document.getElementById('submit')
const dialog = document.querySelector('dialog')
const close = document.getElementById('close')

if (input && dialog) {
    input.addEventListener('click', () => {
        dialog.showModal()
    })
}

if (close && dialog) {
    close.addEventListener('click', () => {
        dialog.close()
        dialog.style.display = 'none'
    })
}

if (dialog && dialog.querySelector('p')) {
    dialog.showModal()
    dialog.style.display = 'block'
}