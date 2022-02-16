var AccountName
var working = false
var authorized = false
var interval
var oldSuccessCount = 0

$.toast = function(text, type='info', duration=2000, close=false){
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

async function loginOnSite(targetId = null, parentId = null, onlySwitch = false) {
	isLoginButtonDisabled = $('#'+targetId+' [data-role="profile-login-btn"]').attr('disabled')
	if (!authorized && !isLoginButtonDisabled) {
		username = $('#'+targetId+' [data-role="profile-username"]').val()
		password = $('#'+targetId+' [data-role="profile-password"]').val()
		ua = $('#'+targetId+' [data-role="ua"]').val()
		if (username != '' && password != '' && ua != null) {
			if(onlySwitch){
				$.toast('Выполняется вход, ожидайте...', 'info')
			}
			$('#login-modal').show();
			$('#'+targetId+' [data-role="profile-login-btn"]').attr('disabled', true)
			let result = await eel.login_on_site(username, password, ua)()
			if (result != null) {
				authorized = true
				$('#'+targetId+' [data-role="profile-pic"]').attr('src', result)
				$('#'+targetId+' [data-role="profile-login-btn"]').attr('disabled', false)
				$('#'+targetId+' [data-role="profile-username"]').attr('readonly', true)
				$('#'+targetId+' [data-role="profile-password"]').attr('readonly', true)
				$('#'+targetId+' [data-role="profile-login-btn"]').remove();
				$('button[data-bs-target="#'+targetId+'"] span').html(username);
				$('button[data-bs-target="#'+targetId+'"] img').attr('src', result);
				$('#'+targetId).data('username', username);
				$('#'+parentId).data('username', username);
				$('#login-modal').hide();
			
				return true
			}
			else {
				$('#login-modal').hide();
				$.toast('Не удалось войти', 'error')
				$('#'+targetId+' [data-role="profile-login-btn"]').attr('disabled', false)
				return false
			}
		}
		else {
			$.toast('Пожалуйста, введите логин, пароль и User-Agent вашего браузера', 'warning')
			return false
		}
	} else if (authorized) {
		logoutOnSite()
		loginOnSite(targetId)
	}
}

async function logoutOnSite() {
	if (authorized) {
		authorized = false
		let result = await eel.logout_on_site()()
		// $('#profile-pic').attr('src', 'img/userpic.jpg')
		// $('#profile-login-btn').html('Вход')
		// $('#profile-username').val('')
		// $('#profile-password').val('')
		// $('#profile-username').attr('readonly', false)
		// $('#profile-password').attr('readonly', false)
		return true
	}
}
async function closeTab(targetId, childId){
	var confirmResult = confirm('Вы уверенны что хотите закрыть эту анкету?');
	if(confirmResult){
		var username = $('#'+targetId).data('username');
		let result = await eel.closeTab(username)()
		if(result === true){
			$('#'+targetId).remove();
			$('#'+childId).remove();
			$.toast('Вы вышли из анкеты', 'success')
		}else{
			$.toast('Что-то пошло не так при закрытии таба.', 'error')
		}
	}
}

async function saveLinks(targetId){
	var username = $('#'+targetId).data('username');
	if(username){
		var confirmResult = confirm('Вы уверенны что хотите сохранить текущий список ссылок? Сохранённый будет перезаписан.');
		if(confirmResult){
			links = $('#'+targetId+' [data-role="mail-links"]').val().split('\n');
			let result = await eel.save_links(username, links)()
			if(result === true){
				$.toast('Ссылки сохранены', 'success')
			}else{
				$.toast('Что-то пошло не так при сохранении ссылок.', 'error')
			}
		}
	}else{
		$.toast('Вам нужно сначало залогинится в анкету', 'warning')
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
				$('#'+targetId+' [data-role="mail-links"]').val(links);
				$.toast('Ссылки загруженны', 'success')
			}else{
				$.toast('Что-то пошло не так загрузке ссылок.', 'error')
			}
		}
	}else{
		$.toast('Вам нужно сначало залогинится в анкету', 'warning')
	}
	return true;
}

async function initAccounts(){
	let accounts = await eel.load_accounts()()
	if(accounts.length == 0){
		$('#newAccountItem').trigger('click');
	}else{
		for (var username in accounts) {
			createNewAccount(accounts[username]);
		}
	}
}

function updateProgressBar(now, max) {
	$('.progress-text').html(now + ' из ' + max)
	$('#progress').css('width', (now/max*100) + '%')
}

async function start(targetId) {
	if (working) {
		// просто открыть модальное окно
		$('#progressModal').modal('show')

	} else {
		// запустить рассылку
		links = $.trim($('#'+targetId+' [data-role="mail-links"]').val()).split('\n')
		text = $('#'+targetId+' [data-role="mail-text"]').val()
		ua = $('#'+targetId+' [data-role="ua"]').val()
		imageId = $('#'+targetId+' [data-role="gallery-image-data-id"]').val()
		updateProgressBar(0, links.length)
		if (links.length != 0 && text != '' && ua != '' && authorized && imageId !='') {
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
			$('#'+targetId+' [data-role="start-btn"]').html('Работаем...')
			$('#progressModal').data('target-id', targetId);
			let result = await eel.start_mailing(links, text, ua, imageId)()
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
		var targetId = $('#progressModal').data('target-id');
		$('#'+targetId+' [data-role="start-btn"]').html('Начать работу')
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

async function setUserAgent(targetId) {
	ua = $.trim($('#'+targetId+' [data-role="ua"]').val());
	username = $.trim($('#'+targetId).data('username'));
	if (ua != '' && ua.match(/^[a-zA-Z0-9 \s\\.,/:;\+\-_\)\(\[\]]*$/gm) && ua.length >= 16) {
		let result = await eel.set_user_agent(ua, username)()
		$.toast('Успешно', 'success')
		return true
	}
	else {
		$.toast('Пожалуйста, укажите User-Agent вашего браузера', 'warning')
		return false
	}
}

async function getUserAgent(targetId) {
	username = $.trim($('#'+targetId).data('username'))
	let result = await eel.get_user_agent(username)()
	if (result != null) {
		$('#'+targetId+' [data-role="ua"]').val(result)
		return true
	}
}

var createNewAccount = function(account = {}, focus = false){
	var tabContent = $('#tabContent');

	var navItemTemplate = $('#navItemTemplate');
	var navContentTemplate = $('#navContentTemplate');
	
	var id = Date.now();
	var target = 'tab' + id;

	var templateText = navItemTemplate.html();
	var accountImage = account.image ?? 'img/userpic.jpg';
	var accountUsername = account.username ?? '';
	var accountUsernameData = account.username ?? 'Новый профиль';
	var accountPasword = account.password ?? '';
	var accountUa = account.ua ?? '';

	templateText = templateText.replaceAll('${id}', id);
	templateText = templateText.replaceAll('${childId}', target);
	templateText = templateText.replaceAll('${target}', '#' + target);
	templateText = templateText.replaceAll('${img}', accountImage);
	templateText = templateText.replaceAll('${username}', accountUsername);
	templateText = templateText.replaceAll('${usernameData}', accountUsernameData);
	$(templateText).insertBefore(".nav-item.add");

	var templateContentText = navContentTemplate.html();
	templateContentText = templateContentText.replaceAll('${id}', target);
	templateContentText = templateContentText.replaceAll('${parentId}', id);
	templateContentText = templateContentText.replaceAll('${img}', accountImage);
	templateContentText = templateContentText.replaceAll('${username}', accountUsername);
	templateContentText = templateContentText.replaceAll('${password}', accountPasword);
	templateContentText = templateContentText.replaceAll('${ua}', accountUa);
	tabContent.append(templateContentText);

	if(focus){
		$('button[data-bs-target="#'+target+'"]').trigger('click');
	}
	
};

$(document).on('click', '#newAccountItem',function(){
	createNewAccount({}, true);
});

$(document).on('click', '.nav-item .close',function(){
	deleteTab(this);
});

$(document).on('click', 'button[data-bs-target]',function(){
	var username = $($(this).data('bs-target') + ' [data-role="profile-username"]').val();
	var password = $($(this).data('bs-target') + ' [data-role="profile-password"]').val();
	if (username != '' && password != '') {
		var formId = $(this).data('child-id');
		var tabId = $(this).data('id');
		loginOnSite(formId, tabId, true);
	}
});



