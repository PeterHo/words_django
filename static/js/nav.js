/**
 * Created by peter on 11/14/16.
 */

var prefixBtn;
var rootBtn;
var suffixBtn;

function defaultAllNavBtn() {
    prefixBtn.removeClass("btn-primary").addClass("btn-default");
    rootBtn.removeClass("btn-primary").addClass("btn-default");
    suffixBtn.removeClass("btn-primary").addClass("btn-default");
}

function setNavBtnStyle(type) {
    defaultAllNavBtn();
    if (type === 'prefix') {
        prefixBtn.addClass("btn-primary");
    } else if (type === 'root') {
        rootBtn.addClass("btn-primary");
    } else if (type === 'suffix') {
        suffixBtn.addClass("btn-primary");
    }
}

function onNavBtnClick(btn, root_type) {
    if (rootsJson) {
        // 有词根信息,直接显示
        type = root_type;
        setNavBtnStyle(type);
        btn.blur();
        showAllRoots();
    } else {
        // 无词根信息,跳转页面
        window.location.href = list_url + '?type=' + root_type;
    }
}

$(function () {
    prefixBtn = $("#prefix_btn");
    rootBtn = $("#root_btn");
    suffixBtn = $("#suffix_btn");

    setNavBtnStyle(type);

    prefixBtn.click(function () {
        onNavBtnClick(prefixBtn, 'prefix');
    });
    rootBtn.click(function () {
        onNavBtnClick(rootBtn, 'root');
    });
    suffixBtn.click(function () {
        onNavBtnClick(suffixBtn, 'suffix');
    });
});
