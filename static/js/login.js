function validate(){
    if(!document.getElementById('associManager').checked) ||  (!document.getElementById('associMem').checked) || (!document.getElementById('owner').checked)
       || (!document.getElementById('tenant').checked)  || (!document.getElementById('security').checked){
            document.getElementById('label').innerHTML = "select any one"
       }
}