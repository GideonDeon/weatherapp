$('#clickable').click(function(){
    $('#accordion').css('height','10em')
})
$('#close').click(function(){
    $('#accordion').css('height','0')
})
$('#map').click(function(){
    $('#gmap').css('height','20em')
})


function time(){
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let ss = date.getSeconds();
    let session = 'AM';
    let text = document.getElementById('text')
    if(hh>=12){
        session='PM'
    }
    hh = (hh<10)? "0" + hh : hh;
    mm = (mm<10)? "0" + mm : mm;
    ss = (ss<10)? "0" + ss : ss;
    let display = `${hh}:${mm}:${ss}`
    document.getElementById("clock").innerHTML = display;
    let sess = `${session}`
    document.getElementById("session").innerHTML = sess
   
    setTimeout( function(){time()},1000)  
    if(hh<12){
        text.innerHTML = 'Good Morning!'
    }else if(hh>=17){
        text.innerHTML = 'Good Evening!'
    }else if(hh>=12){
        text.innerHTML = 'Good Afternoon!'
    }
}time()
