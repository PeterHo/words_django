/**
 * Created by peter on 11/14/16.
 */
var curLetter = "";

function icon(name) {
    return `<i class="material-icons">${name}</i>`;
}

function button(href, text, style, color, type, extraClass, onclick) {
    href = href || 'javascript:void(0);';
    var btn = $(`<a href="${href}" class="btn btn-${style} btn-${color}">${text}</a>`);
    if (type) {
        btn.attr('type', type);
    }
    if (extraClass) {
        btn.addClass(extraClass);
    }
    if (onclick) {
        btn.attr('onclick', onclick);
    }
    return btn;
}

function raisedBtn(href, text, color, type, extraClass, onclick) {
    return button(href, text, 'raised', color, type, extraClass, onclick);
}

function flatBtn(href, text, color, type, extraClass, onclick) {
    return button(href, text, '', color, type, extraClass, onclick);
}

function realBtn(id, text, color, type, extraClass) {
    var btn = $(`
            <button id="${id}" class="btn btn-raised btn-${color}">${text}</button>
        `);
    if (type) {
        btn.attr('type', type);
    }
    if (extraClass) {
        btn.addClass(extraClass);
    }
    return btn;
}

function floatInput(id, label, text) {
    text = text || '';
    var input = $(`
            <div class="form-group label-floating">
                <label for=${id} class="control-label">${label}</label>
                <input class="form-control" id=${id} type="text" name=${id} value="${text}">
            </div>
        `);
    return input;
}

function div(id, className) {
    var dom = $("<div></div>");
    if (id) {
        dom.attr('id', id);
    }
    if (className) {
        dom.addClass(className);
    }
    return dom;
}
