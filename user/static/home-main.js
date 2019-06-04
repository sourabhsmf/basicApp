function userActions(method , url , data , callbackFn){
    req = new XMLHttpRequest();
    req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        callbackFn(JSON.parse(this.response));
        }
    };
    
    req.open(method , url , true)
    url === "GET" ? req.send() : req.send(data)
}
var getUsers = () => {
    userActions('GET' , '/user/manage' , '' , showUsers)
}
var editUser = user => {
    // postData =  
    // userActions('POST' , '/user/edit/' , )
}
var deleteUser = pk => {
    userActions('GET' , '/user/delete/id/' + pk , '' , removeUserDiv)
}
var showUsers = users => {
    for(user of users){
        createUserDiv(user)
    }
}
function createUserDiv(user){
    if(document.getElementById('user-id-' + user.pk) === null){
        var userDetails = "<div class='user' style='display:inline-block;padding-right:5%' id='user-id-" + user.pk + "'>"
                            +   "<p id='user-email-" + user.pk + "'>"
                            +     user.fields.email 
                            +    "</p>"
                        + "</div>";
        var staticContent = "<div class='user-action' style='display:inline-block' id='user-action-" + user.pk + "'>"
                            +   "<button onclick='deleteUser(" + user.pk + ")'>Delete</button>"
                            +   "<button onclick='editUser("+ user.pk +")'>Edit</button>"
                            + "</div><br>";
        
        document.getElementById("users").innerHTML += (userDetails + staticContent);
        
    }
}
function removeUserDiv(pk){
    document.getElementById('user-id-' + pk).remove()
    document.getElementById('user-action-' + pk).remove()
}