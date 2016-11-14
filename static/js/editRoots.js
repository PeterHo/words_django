/**
 * Created by peter on 11/14/16.
 */
var indexList = [0];
var wordIndexList = [0];

function meaningEditBlock(index, meaning) {
    meaning = meaning || {chinese: '', english: ''};
    var dom = div(`meaning_${index}`, 'well');
    dom.append(realBtn(`del_meaning_${index}`, icon('delete'), 'danger', null, 'btn-xs pull-right onTop'));
    dom.append(realBtn(`add_meaning_${index}`, icon('add'), 'success', null, 'btn-xs pull-right onTop'));
    dom.append(floatInput(`meaning_chinese_${index}`, 'Chinese', meaning.chinese));
    dom.append(floatInput(`meaning_english_${index}`, 'English', meaning.english));
    dom.append(div(`meaning_word_${index}`));
    return dom;
}

function wordEditBlock(meaningIndex, wordIndex, word) {
    word = word || {word: ''};
    var dom = div(`word_${meaningIndex}_${wordIndex}`, 'well');
    dom.append(realBtn(`del_word_${meaningIndex}_${wordIndex}`, icon('delete'), 'danger', null, 'btn-xs pull-right onTop'));
    dom.append(realBtn(`add_word_${meaningIndex}_${wordIndex}`, icon('add'), 'success', null, 'btn-xs pull-right onTop'));
    dom.append(floatInput(`word_word_${meaningIndex}_${wordIndex}`, 'Word', word.word));
    return dom;
}


function wordCanDel(btn) {
    var re = /del_word_(\d{1,3})_(\d{1,3})/;
    var meaning_id = re.exec($(btn).attr('id'))[1];
    if ($("button[id^='add_word_" + meaning_id + "_']").size() < 2) {
        $.snackbar({content: "已是最后一项"});
        return false;
    } else {
        return true;
    }
}

function meaningCanDel(btn) {
    if ($("button[id^='add_meaning_']").size() < 2) {
        $.snackbar({content: "已是最后一项"});
        return false;
    } else {
        return true;
    }
}

function addWordBlock(meaningIndex) {
    var index = Math.max.apply(null, wordIndexList) + 1;
    var word = wordEditBlock(meaningIndex, index);
    $("#meaning_word_" + meaningIndex).append(word);
    wordIndexList.push(index);
    $("button[id^='add_word_']").unbind('click').click(function () {
        var re = /add_word_(\d{1,3})_(\d{1,3})/;
        var meaning_id = re.exec($(this).attr('id'))[1];
        addWordBlock(meaning_id);
        return false;
    });
    $("button[id^='del_word_']").unbind('click').click(function () {
        if (wordCanDel(this)) {
            $(this).parent().remove();
        }
        return false;
    });
}

function addMeaningBlock() {
    var index = Math.max.apply(null, indexList) + 1;
    var meaning = meaningEditBlock(index);
    $("#meanings").append(meaning);
    indexList.push(index);
    $("button[id^='add_meaning_']").unbind('click').click(function () {
        addMeaningBlock();
        return false;
    });
    $("button[id^='del_meaning_']").unbind('click').click(function () {
        if (meaningCanDel(this)) {
            $(this).parent().remove();
        }
        return false;
    });
    addWordBlock(index);
}

function editWordBlock(meaningIndex, meaning) {
    if (meaning.words.length == 0) {
        return addWordBlock(meaningIndex);
    }
    for (word of meaning.words) {
        var index = Math.max.apply(null, wordIndexList) + 1;
        var word = wordEditBlock(meaningIndex, index, word);
        $("#meaning_word_" + meaningIndex).append(word);
        wordIndexList.push(index);
        $("button[id^='add_word_']").unbind('click').click(function () {
            var re = /add_word_(\d{1,3})_(\d{1,3})/;
            var meaning_id = re.exec($(this).attr('id'))[1];
            addWordBlock(meaning_id);
            return false;
        });
        $("button[id^='del_word_']").unbind('click').click(function () {
            if (wordCanDel(this)) {
                $(this).parent().remove();
            }
            return false;
        });
    }
}

function editMeaningBlock(root) {
    if (root.meanings.length == 0) {
        return addMeaningBlock();
    }
    for (meaning of root.meanings) {
        var index = Math.max.apply(null, indexList) + 1;
        $("#meanings").append(meaningEditBlock(index, meaning));
        indexList.push(index);
        $("button[id^='add_meaning_']").unbind('click').click(function () {
            addMeaningBlock();
            return false;
        });
        $("button[id^='del_meaning_']").unbind('click').click(function () {
            if (meaningCanDel(this)) {
                $(this).parent().remove();
            }
            return false;
        });
        editWordBlock(index, meaning);
    }
}