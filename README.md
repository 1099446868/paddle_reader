# paddle_reader
**单行文本阅读器，划水神器**

- 这是一款具有极简ui的 单行文本阅读器，无聊划水的不二选择

- main.py 是主运行文件，可以修改 dir = r"E:/paddle_reader/file/test"，打开你想打开的小说文件，需要注意的是文件名需要和目录名称相同。
 如 test.txt的文件名跟test目录名一样。
  
- 小说阅读的行数记录保存在reader.db中，修改表中的记录再重启软件即可跳转到目标行数。
  
- dist中的main.exe文件是打包好的可执行文件，如果需要可以直接直接，需要注意的是 该文件的存放位置和小说存放位置需要跟 main.py中的 dir一致。
