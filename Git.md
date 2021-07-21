## 1.安装git

### 配置

1. 在git的命令行中配置用户姓名和邮箱  

   > git config --global user.name ""
   >
   > git config --globla user.email ""  

2. 创建版本库

   > git init

### 常用命令

> git add <filename>			//添加到暂存区
>
> git commit -m "message" 	//提交到本地仓库
>
> git status 								//查看工作区状态，是否有修改，文件为提交等
>
> git diff <file>						//查看文件的不同，改什么内容
>
> git log 									//查看历史记录，显示从最近到最远的日志
>
> git reset -- hard HEAD^   	//版本回退

### 创建SSH Key

> ssh -keygen -t rsa -C "user email"
>
> 把公钥链接到github后，推送到远程仓库
>
> git remote add origin URL
>
> git push -u origin master
>
> 从远程克隆
>
> git clone URL

### 创建与合并分支

> git branch 							//查看分支，当前分支用*标识
>
> git branch name 				//创建分支
>
> git checkout -b name 		//创建并切换分支
>
> git checkout name			 //切换分支
>
> git merge name 				//合并某分支到当前分支