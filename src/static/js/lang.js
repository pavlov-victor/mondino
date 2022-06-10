function createCookie(name,value,days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else var expires = "";
    document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name,"",-1);
}

// Объединение библиотек
if (typeof rus1 != undefined) {
    Object.assign(rus, rus1);
}
if (typeof eng1 != undefined) {
    Object.assign(eng, eng1);
}

var rus_select = document.getElementById("rus");
var eng_select = document.getElementById("eng");

function checkLang() {
    if (lang == "rus") {
        rus_select.classList.add('actLang');
        eng_select.classList.remove('actLang');
    } else if (lang == "eng") {
        eng_select.classList.add('actLang');
        rus_select.classList.remove('actLang');
    }
}

// Меняет содержимое элемента по словарю,
// необходимо в элементе указать caption(значение в словаре)
// и в классе добавить localization
function changeLang(to) {
    createCookie("lang", to, 2051, 01, 15);
    lang = to;
    var r = document.getElementsByClassName('localization');
    if (lang == "rus") {
        for (i = 0; i < r.length; i++) {
            var key = (r[i].getAttribute('caption'));
            r[i].innerHTML = rus[key];
        }
    } else if (lang == "eng") {
        for (i = 0; i < r.length; i++) {
            var key = (r[i].getAttribute('caption'));
            r[i].innerHTML = eng[key];
        }
    } 
    checkLang(lang);
}

var lang = readCookie("lang");
if (lang == null) {
    createCookie("lang", "rus", 100);
    lang = "rus";
}
checkLang();
changeLang(lang);