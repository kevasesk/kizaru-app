var AccountName
var working = false
var authorized = false
var interval
var UserAgent = null
var oldSuccessCount = 0

$.toast = function(text, type='info', duration=1000, close=false){
	switch (type) {
		case 'success': //'linear-gradient(to right, #c8003a, #ff5732 50%)'//
			color = '#56ab2f' // green
			break
		case 'warning':
			color = '#f5af19' // yellow
			break
		case 'error':
			color = '#DA4453' // red
			break
		case 'info':
			color = '#1c92d2' // blue
			break
	}
	Toastify({text: text, duration: duration, close: close, backgroundColor: color}).showToast();
}

async function checkAuth() {
	let login_details = await eel.get_login_details()()
	if (login_details != null) {
		if (login_details['auto_login'] == false || login(login_details['username'], login_details['password']) == false) {
			setBody('login.html')
			$('#login-username').val(login_details['username'])
			$('#login-password').val(login_details['password'])
			$('#login-save-details').attr('checked', true)
		}
	}
	else {
		setBody('login.html')
	}
}

function setBody(filename) {
	$('#body').html($.ajax({
		url: filename,
		cache: false,
		async: false
	}).responseText)
}

async function login(username=null, password=null, saveLoginDetails=true) {
	if (username == null && password == null) {
		username = $('#login-username').val()
		password = $('#login-password').val()
		saveLoginDetails = $('#login-save-details').is(':checked')
	}
	if (username != '' && password != '') {
		let result = await eel.login(username, password, saveLoginDetails)()
		if (result) {
			// $.toast('Успешный вход в аккаунт '+username, 'success', 1000)
			AccountName = username
			setBody('dashboard.html')
			return true
		}
		else {
			$.toast('Не удалось войти', 'error')
			return false
		}
	}
	else {
		$.toast('Пожалуйста, введите логин и пароль', 'warning')
		return false
	}
}

async function logout() {
	let result = await eel.logout()()
	// $.toast('Успешно', 'success')
	AccountName = null
	setBody('login.html')
	checkAuth()
	return true
}

async function loginOnSite(targetId = null) {
	isLoginButtonDisabled = $('#profile-login-btn').attr('disabled')
	if (!authorized && !isLoginButtonDisabled) {
		username = $('#profile-username').val()
		password = $('#profile-password').val()
		if (username != '' && password != '' && UserAgent != null) {
			$.toast('Выполняется вход, ожидайте...', 'info')
			$('#profile-login-btn').attr('disabled', true)
			let result = await eel.login_on_site(username, password, UserAgent)()
			if (result != null) {
				authorized = true
				$('#profile-pic').attr('src', result)
				$('#profile-login-btn').attr('disabled', false)
				$('#profile-username').attr('readonly', true)
				$('#profile-password').attr('readonly', true)
				$('#profile-login-btn').html('Выход');
				$('button[data-bs-target="#'+targetId+'"] span').html(username);
				$('button[data-bs-target="#'+targetId+'"] img').attr('src', result);
				$('#'+targetId).data('username', username);
			
				return true
			}
			else {
				$.toast('Не удалось войти', 'error')
				$('#profile-login-btn').attr('disabled', false)
				return false
			}
		}
		else {
			$.toast('Пожалуйста, введите логин, пароль и User-Agent вашего браузера', 'warning')
			return false
		}
	} else if (authorized) {
		logoutOnSite()
	}
}

async function logoutOnSite() {
	if (authorized) {
		authorized = false
		let result = await eel.logout_on_site()()
		$('#profile-pic').attr('src', 'img/userpic.jpg')
		$('#profile-login-btn').html('Вход')
		// $('#profile-username').val('')
		// $('#profile-password').val('')
		$('#profile-username').attr('readonly', false)
		$('#profile-password').attr('readonly', false)
		return true
	}
}

async function saveLinks(targetId){
	var username = $('#'+targetId).data('username');
	if(username){
		var confirmResult = confirm('Вы уверенны что хотите сохранить текущий список ссылок? Сохранённый будет перезаписан.');
		if(confirmResult){
			links = $('#mail-links').val().split('\n');
			let result = await eel.save_links(username, links)()
			console.log(result);
		}
	}
	return true;
}

async function loadLinks(targetId){
	var username = $('#'+targetId).data('username');
	if(username){
		var confirmResult = confirm('Вы уверенны что хотите загрузить сохраненный список ссылок? Текущий будет утерян.');
		if(confirmResult){
			let result = await eel.load_links(username)()
			console.log(Array.isArray(result))
			if(Array.isArray(result)){
				var links = '';
				for(var i=0;i< result.length ;i++){
					links += result[i] + '\n';
				}
				$('#mail-links').val(links);
			}else{
				console.log(result);
			}
		}
	}
	return true;
}

function updateProgressBar(now, max) {
	$('.progress-text').html(now + ' из ' + max)
	$('#progress').css('width', (now/max*100) + '%')
}

async function start() {
	if (working) {
		// просто открыть модальное окно
		$('#progressModal').modal('show')

	} else {
		// запустить рассылку
		links = $('#mail-links').val().split('\n')
		text = $('#mail-text').val()
		updateProgressBar(0, links.length)
		if (links.length != 0 && text != '' && UserAgent != null && authorized) {
			working = true
			$('#progressModal').modal('show')
			interval = setInterval(async function(){
				successCount = await getSuccessCount()
				// закругляемся
				if (!working || (oldSuccessCount != 0 && successCount == 0)) {
					clearInterval(interval)
					stop(true)
					$.toast('Рассылка завершена', 'success')
				}
				oldSuccessCount = successCount
				updateProgressBar(successCount, links.length)
			}, 1000)
			$('#start-btn').html('Работаем...')
			let result = await eel.start_mailing(links, text, UserAgent)()
			return true
		}
		else {
			$.toast('Пожалуйста, укажите всю необходимую информацию для запуска рассылки', 'warning')
			return false
		}
	}
}

async function stop(frontendOnly=false) {
	if (working) {
		working = false
		$('#progressModal').modal('hide')
		updateProgressBar(0, 0)
		$('#start-btn').html('Начать работу')
		if (!frontendOnly) {
			let result = await eel.stop_mailing()()
		}
		return true
	}
	else {
		// $.toast('В данный момент рассылка неактивна', 'warning')
		return false
	}
}

async function getSuccessCount() {
	if (working) {
		let result = await eel.get_success_count()()
		return parseInt(result)
	}
	else {
		// $.toast('В данный момент рассылка неактивна', 'warning')
		return 0
	}
}

async function setUserAgent() {
	ua = $.trim($('#ua').val())
	if (ua != '' && ua.match(/^[a-zA-Z0-9 \s\\.,/:;\+\-_\)\(\[\]]*$/gm) && ua.length >= 16) {
		UserAgent = ua
		let result = await eel.set_user_agent(ua)()
		$.toast('Успешно', 'success')
		return true
	}
	else {
		$.toast('Пожалуйста, укажите User-Agent вашего браузера', 'warning')
		return false
	}
}

async function getUserAgent() {
	let result = await eel.get_user_agent()()
	if (result != null) {
		$('#ua').val(result)
		UserAgent = result
		return true
	}
}

var createNewAccount = function(){
	var tabContent = $('#tabContent');

	var navItemTemplate = $('#navItemTemplate');
	var navContentTemplate = $('#navContentTemplate');
	
	var id = Date.now();
	var target = 'tab' + Date.now();

	var templateText = navItemTemplate.html();
	templateText = templateText.replaceAll('${id}', id);
	templateText = templateText.replaceAll('${target}', '#' + target);
	templateText = templateText.replaceAll('${img}', 'img/userpic.jpg');
	templateText = templateText.replaceAll('${label}', 'Новый профиль');
	$(templateText).insertBefore(".nav-item.add");

	var templateContentText = navContentTemplate.html();
	templateContentText = templateContentText.replaceAll('${id}', target);
	tabContent.append(templateContentText);

	$('button[data-bs-target="#'+target+'"]').trigger('click');
	
};
var deleteTab = function(element){
	var result = confirm("Вы уверены что хотите выйти из этого аккаунта?");
	if(result){
		$(element).parent('li').remove();
		$($(element).data('target')).remove();
	}
};

$(document).on('click', '#newAccountItem',function(){
	createNewAccount();
});

$(document).on('click', '.nav-item .close',function(){
	deleteTab(this);
});



