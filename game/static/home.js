document.addEventListener('DOMContentLoaded',function(){
    const data = JSON.parse(document.getElementById('date-data').textContent);
    if(data){
        document.querySelector('.navbar').hidden = false; ///"IT WORKS";
    } else {
        document.querySelector('.navbar').hidden = true;
    }
});