
function login(){
    var username=document.getElementById('login_username').value 
    var password=document.getElementById('login_password').value 
    var csrf = document.getElementById('csrf').value
    if(username=='' && password==''){
        alert('you must enter both fields')
    }

    var data={
        'username': username,
        'password': password
    }

    fetch('api/login/',{
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        
        body : JSON.stringify(data)

            }).then(result => result.json()).then(response => {
                if(response.status==200){
                    window.location.href='/'
                }
                else{
                    alert(response.message)
                }
            })
} 


function register(){
    
    var username=document.getElementById('register_username').value 
    var password=document.getElementById('register_password').value 
    var csrf = document.getElementById('csrf').value
    if(username=='' && password==''){
        alert('you must enter both fields')
    }

    var data={
        'username': username,
        'password': password
    }

    fetch('api/register/',{
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        
        body : JSON.stringify(data)

            }).then(result => result.json()).then(response => {
                console.log(response)
                if(response.status==200){
                    
                }
                else{
                    alert(response.message)
                }
            })
} 