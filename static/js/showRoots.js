/**
 * Created by peter on 11/14/16.
 */
// 显示所有首字母
function showLetters(letters) {
    var letterDom = $("#letters");
    letterDom.empty();
    letterDom.append(raisedBtn(null, 'all', 'default', null, null, "onLetterClick(this)"));
    for (var letter of letters[type]) {
        letterDom.append(raisedBtn(null, letter, 'default', null, null, `onLetterClick(this, '${letter}')`));
    }
}

// 取消所有字母按钮的选中效果
function defaultAllLetterBtns() {
    $("#letters > a").each(function () {
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
    dom.append(flatBtn(null, meaning.chinese + "&nbsp;&nbsp;" + meaning.english, "info", null, "lowercase"));
    dom.append(wordsShowBlock(meaning));
    return dom;
}

// 显示词根的所有meaning
function meaningsShowBlock(root) {
    var meanings = [];
    for (var meaning of root.meanings) {
        meanings.push(meaningShowBlock(meaning));
    }

    return meanings;
}

// 显示meaning的所有words
function wordsShowBlock(meaning) {
    var dom = div(null, 'well');
    var words = "";
    for (var word of meaning.words) {
        words += "&nbsp;&nbsp;" + word.word;
    }
    dom.append(flatBtn(null, words, "default", null, "lowercase"));
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
        if (letter && !root.root.startsWith(letter)) {
            continue;
        }

        var dom = div().append(flatBtn(edit_url.replace('123456', root.id), root.root, 'info', null, 'lowercase'));
        dom.append(meaningsShowBlock(root));

        rootsDom.append(dom);
    }
}

// 显示页面
function showAllRoots() {
    showLetters(letters);
    $("#letters > a")[0].click();
}