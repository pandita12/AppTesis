let div = document.querySelector(".table-responsive");
let btn = document.querySelector(".download");
btn.addEventListener('click', () => {
     html2pdf().from(div).save()
});
    