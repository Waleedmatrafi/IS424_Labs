document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#color').onchange = function () {
        document.querySelector('#hello').style.color = this.value;
    }

    const submit = document.querySelector('#submit');
    const newColor = document.querySelector('#color');
    submit.disabled = true;

    newColor.onkeyup = () => {

        if (newColor.value.length > 0) {
            submit.disabled = false;
        } else {
            submit.disabled = true;
        }
    }
    document.querySelector('form').onsubmit = () => {
        return false;
    }
});