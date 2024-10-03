import os
import codecs

# 构建平假名、片假名和浊音、半浊音的罗马音映射表
hiragana_katakana_to_romaji = {
    # 平假名
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "wo", "ん": "n",
    "ゔ": "vu",  # 平假名「ゔ」
    
    # 浊音 平假名
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",

    # 半浊音 平假名
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
    
    # 片假名
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
    "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
    "ワ": "wa", "ヲ": "wo", "ン": "n",
    "ヴ": "vu",  # 片假名「ヴ」

    # 浊音 片假名
    "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
    "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
    "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do",
    "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",

    # 半浊音 片假名
    "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po",
    
    # 小写的拗音 平假名
    "ゃ": "xya", "ゅ": "xyu", "ょ": "xyo", "ぁ":"xa","ぉ":"xo","ぃ":"xi","ぅ":"xu","ぇ":"xe",
    
    # 小写的拗音 片假名
    "ャ": "xya", "ュ": "xyu", "ョ": "xyo","ァ":"xa","ォ":"xo","ィ":"xi","ゥ":"xu","ェ":"xe"
}

# 将平假名、片假名文本转换为罗马音
def convert_to_romaji(text):
    result = ""
    for char in text:
        if char in hiragana_katakana_to_romaji:
            result += hiragana_katakana_to_romaji[char]
        else:
            result += char  # 如果不是假名字符，直接保留
    return result

# 重命名目录下的文件名，将平假名、片假名转换为罗马音
def rename_files_in_directory(directory_path):
    # 获取目录中的所有文件和子文件夹
    for filename in os.listdir(directory_path):
        # 跳过文件夹
        if os.path.isdir(os.path.join(directory_path, filename)):
            continue

        # 转换文件名
        new_filename = convert_to_romaji(filename)

        # 如果文件名没有改变，则跳过
        if new_filename == filename:
            continue

        # 获取旧文件的完整路径和新文件的完整路径
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_filename)

        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

if __name__ == "__main__":
    # 指定要处理的目录路径
    directory = input('dir:')
    
    # 调用重命名函数
    rename_files_in_directory(directory)
    
    print("文件重命名完成！")
