//getElementById缩写方法
function getBI(id){
    return document.getElementById(id);
}

//全部检查
function check() {
    var form = getBI("login-form");
    var f = true;
    if(!checkUsername()) f=false;
    if(!checkPassword()) f=false;
    if(f) form.classList.add("was-validated");
//    debug
//    return false;
    return f;
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
        //todo:判定密码重复
		var password1 = getBI("password1");
        var feedback1 = getBI("password1-feedback");
        var feedback2 = getBI("password2-feedback")
		if(password1.value==""){
			feedback1.innerHTML = "密码为空！";
			password1.classList.add("is-invalid");
			return false;
		}
		else{
		    password1.classList.remove("is-invalid");
            password1.classList.add("is-valid");
            feedback1.innerHTML="";
        }
        if(password2.value==""){
			feedback2.innerHTML = "密码为空！";
			password2.classList.add("is-invalid");
			return false;
		}
		else{
		    password2.classList.remove("is-invalid");
            password2.classList.add("is-valid");
            feedback2.innerHTML="";
        }
        if(password1.value != password2.value){
            feedback1.classList.add("is-invalid");
            feedback2.classList.add("is-invalid");
            feedback1.innerHTML="两次密码输入不一致！";
            feedback2.innerHTML="请检查输入！";
            return false;
        }

		return true;
}