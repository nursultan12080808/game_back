let i = 0
if (i == 0){
    category_menu.style = 'display: none;'
}
category.addEventListener('click', () => {
    if(i){
        crest.classList = 'bx bx-chevron-down crest1'
        category_menu.style = 'display: none;'
        i = 0
    }else{
        crest.classList = 'bx bx-chevron-down crest'
        category_menu.style = ''
        i = 1
    }
})
burger_menu.addEventListener('click', () => {
    nav_menu.classList = 'nav_menu'
})
close1.addEventListener('click', () => {
    nav_menu.classList = 'nav_menu1'
})
lupa.addEventListener('click', ()=>{
    model_nav3.classList = 'nav_model4'
})
model_nav3.classList = 'none'
x2.addEventListener('click', () =>{
    model_nav3.classList = 'nav_model3'
})
filter_burger_btn.addEventListener('click', () => {
    blur1.classList = 'blur'
    filter_burger.classList = 'form_filter nav_filter'
})
blur1.addEventListener('click', () =>{
    blur1.classList = 'blur none'
    filter_burger.classList = 'form_filter'
})