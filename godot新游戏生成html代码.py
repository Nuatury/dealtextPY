import pyperclip

def main():
    html_str = input("请输入网址(1--仅用单名字生成)：")

    if html_str == "1":
        html_str = input("单名字:")
        html_str = '/' + html_str + '/' + html_str + '.html'
        
        
    name_str = input("请输入标题：")

    introduce_str = input("请输入说明（这个游戏是一个....的游戏。）输入1自动生成：")
    if introduce_str == "1" :
        introduce_str = "这个游戏是一个" +name_str+ "的游戏。"
    else:
        introduce_str = "这个游戏是一个" +introduce_str+ "的游戏。"

    kind = input("请输入要使用的网站种类\n1--简单\n2--新版\n请输入：")

    str0 =  '<game style="display: inline-block; background-color: #cccccc;"id="gameblock"><p id="gamename_p"> <a href="'+html_str+'"> ' +name_str+'</a></p><p style="color: #137603;">😀'+introduce_str+'</p><p> </p></game>'
    str1 = '<p><a href="'+html_str+'">'+name_str+'</a> </p><p style="color:red">😀'+introduce_str+'</p>'
    if kind == "1":
        print(str1+"\n已复制到剪切板")
        pyperclip.copy(str1)
    elif kind == "2":
        print(str0+"\n已复制到剪切板")
        pyperclip.copy(str0)



if __name__ == "__main__":
    while(1):
        main()
        input_str = input("继续？[y/n]").replace("N","n")
        if input_str == "n":
            break
