/**
 * Created by peter on 11/14/16.
 */
// 显示所有首字母
function showLetters(letters) {
    var letterDom = $("#letters");
    letterDom.empty();
    var dom = div(null, "btn-group btn-group-justified btn-group-raised");
    letterDom.append(dom);
    // dom.append(raisedBtn(null, icon('home'), 'default', null, null, "onLetterClick(this)"));
    dom.append(raisedBtn(null, 'all', 'default', null, null, "onLetterClick(this)"));

    letters[type].forEach(function (letter) {
        dom.append(raisedBtn(null, letter, 'default', null, null, `onLetterClick(this, '${letter}')`));
    });
}


// 取消所有字母按钮的选中效果
function defaultAllLetterBtns() {
    $("#letters a").each(function () {
        $(this).removeClass("btn-primary").addClass("btn-default");
    });
}

// 处理字母按钮的点击消息
function onLetterClick(btn, letter) {
    defaultAllLetterBtns();
    $(btn).removeClass("btn-default").addClass("btn-primary").blur();
    showRoots(letter);
}

// 显示一项meaning
function meaningShowBlock(meaning) {
    var dom = div(null, 'well');
    // dom.append(flatBtn(null, meaning.chinese + "&nbsp;&nbsp;" + meaning.english, "info", null, "lowercase"));
    if (meaning.english) {
        dom.append($(`<div>${meaning.english}&nbsp;&nbsp;${meaning.chinese}</div>`));
    } else {
        dom.append($(`<div>${meaning.chinese}</div>`));
    }
    dom.append(wordsShowBlock(meaning));
    return dom;
}

// 显示词根的所有meaning
function meaningsShowBlock(root) {
    var meanings = [];

    root.meanings.forEach(function (meaning) {
        meanings.push(meaningShowBlock(meaning));
    });

    return meanings;
}

// 显示meaning的所有words
function wordsShowBlock(meaning) {
    if (!meaning.words.length) {
        return null;
    }
    var dom = div(null, 'well');
    // var dom = div();
    var words = "";
    for (var word of meaning.words) {
        words += word.word + "<br>";
    }
    // dom.append(flatBtn(null, words, "default", null, "lowercase"));
    dom.append($(`<div>${words}</div>`));
    return dom;
}

// 显示所有词根
function showRoots(letter) {
    if (letter) {
        curLetter = letter;
    }

    var rootsDom = $("#roots");
    rootsDom.empty();
    for (var root of rootsJson) {
        if (root.type !== type) {
            continue;
        }
        if (letter) {
            var isLetter = false;
            var ls = root.root.split('/');
            for (l of ls) {
                if (l.startsWith(letter)) {
                    isLetter = true;
                    break;
                }
            }
            if (!isLetter) {
                continue;
            }
        }

        var dom = div().append(flatBtn(edit_url.replace('123456', root.id), root.root, 'info', null, 'lowercase'));
        dom.append(meaningsShowBlock(root));

        rootsDom.append(dom);
    }
}

// 显示页面
function showAllRoots() {
    showLetters(letters);
    $("#letters a")[0].click();
}