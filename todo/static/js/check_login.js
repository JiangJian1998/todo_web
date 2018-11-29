//getElementById缩写方法
function getBI(id){
    return document.getElementById(id);
}

//全部检查
function check() {
    var form = getBI("reg-form");
    var f = true;
    if(!checkUsername()) f=false;
    if(!checkPassword()) f=false;
    if(f) form.classList.add("was-validated");
//    debug
    return false;
//    return f;
}

function checkUsername(){
		var username = getBI("username");
        var feedback = getBI("username-feedback");
		if(username.value==""){
			feedback.innerHTML = "用户名为空！";
			username.classList.add("is-invalid");
			return false;
		}
		else{
		    username.classList.remove("is-invalid");
            username.classList.add("is-valid");
            feedback.innerHTML="";
        }
		return true;
}

function checkPassword(){
		var password = getBI("password");
        var feedback = getBI("password-feedback");
		if(password.value==""){
			feedback.innerHTML = "密码为空！";
			password.classList.add("is-invalid");
			return false;
		}
		else{
		    password.classList.remove("is-invalid");
            password.classList.add("is-valid");
            feedback.innerHTML="";
        }

		return true;
}