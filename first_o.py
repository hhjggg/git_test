def first(name):
    print("first",name)开始

git config --global user.name "xxx" // 用户名

git config --global user.email "xxx@163.com" // 邮箱

查看git配置信息

git config -l 

配置完之后，这台电脑上所作的所有修改都会自动酱用户名，email发送到主程序中



2. 配置仓库

仓库(respository)中可以保存所有用户开发过程之中所编写的代码的日志记录

如果要开发项目，首先要有一个仓库（磁盘上的一个目录 /home/smi/mypro）

将/Users/yesiming/mypro设置为仓库

cd 

/Users/yesiming/mypro

git init

会产生.git目录



3.添加文件

ps：所有文件使用utf－8编码

新建一个文件 Hello.java

public class Hello {     public static void main(String[] args) {         System.out.println("Hello");     } }

命令：git status

显示：

On branch master



Initial commit



Untracked files:

  (use "git add <file>..." to include in what will be committed)



Hello.java



nothing added to commit but untracked files present (use "git add" to track)



将Hello.java加入到暂存库

git add Hello.java

再次查询状态 git status

显示：

On branch master



Initial commit



Changes to be committed:

  (use "git rm --cached <file>..." to unstage)



new file:   Hello.java


现在的文件并没有真正提交到主分支上（主分支就是我们要运行的程序的代码分支）

3.提交文件信息

在进行每次更新提交时都要加上注释信息，使用”-m”编写注释

git commit –m “hello.java commit”

显示：

[master (root-commit) 299c519] Hello.java commit

 1 file changed, 5 insertions(+)

 create mode 100644 Hello.java

此时，Hello.java就被真正提交到主分支上了，也就是说，文件发布成功了。

命令：git status

显示：

On branch master

nothing to commit, working directory clean

此时显示没有任何信息需要被提交。Git工具下用户每进行一次提交，实际上都会被日记记录下来。

git log Hello.java

commit 299c519af74c9b41e819e7b937706e15bc67e39b // id号，可以用户回滚

Author: yesiming <simon_ie@163.com>

Date:   Sat Apr 16 16:07:28 2016 +0800



    Hello.java commit



4.修改仓库文件

public class Hello {

    public static void main(String[] args) {

        System.out.println("Hello");

  System.out.println(“Wrold”); // 加入了这一行

    }

}

命令：git status

On branch master

Changes not staged for commit:

  (use "git add <file>..." to update what will be committed)

  (use "git checkout -- <file>..." to discard changes in working directory) // 通过checkout恢复



modified:   Hello.java



no changes added to commit (use "git add" and/or "git commit -a")



查看文件的前后区别

命令：git diff Hello.java

显示：

diff --git a/Hello.java b/Hello.java

index 3d41ec8..4dcfb34 100644

--- a/Hello.java

+++ b/Hello.java

@@ -1,5 +1,6 @@

 public class Hello {

     public static void main(String[] args) {

         System.out.println("Hello");

+       System.out.println("Wrold");

     }

 }



提交修改的 Hello.java文件

git add Hello.java

git commit –m “Hello.java modify”

显示：

[master cbc7d89] hello.java modify

 1 file changed, 1 insertion(+)





工作区与暂存区

工作区：磁盘目录（/Users/yesiming/mypro）

仓库：/Users/yesiming/mypro/.git

暂存区：



编写的Hello.java文件保存在工作区中，

当使用add命令后，Hello.java被提交到暂存区（stage）中

使用commit命令之后，才表示发出了真正的修改，而真正可以运行的程序都保存在master分支上。



暂存区操作

使用git add把代码提交到暂存区中

提交修改

git commit –m “”

文件进入暂存区后就可以提交到主分支上了，并且会自动晴空暂存区的内容

所以执行git status会显示

On branch master

nothing to commit, working directory clean



版本回退

每次提交代码都会生成一个commit id，用于版本控制

执行：git log --pretty=oneline

显示操作log:

0c00d3615db09d5e2e173ef317f6b52982c398b7 修改2个文件，测试回退

0d5c5bad0ae28006fe290905401ecd412bea58ea 新增World.java文件

cbc7d8920e18ca8d7f0e32b23e4de53c13c93974 hello.java modify

299c519af74c9b41e819e7b937706e15bc67e39b Hello.java commit



commit id是sha1编码搞定的



在master分支上有个Head指针，永远指想最后一次提交的位置（最后一次提交的commit id）

执行：vim .git/HEAD

显示：ref: refs/heads/master

.git/refs/heads/master

vim master 内容是 0c00d3615db09d5e2e173ef317f6b52982c398b7

其实是这个master文件记录了commit id，打开就能看到，妥妥的是最后一次提交的commit id



回退具体操作：

执行：git reset --hard HEAD~1 // 强制回退到上1次提交

显示：HEAD is now at 0d5c5ba 新增World.java文件

再次查看.git/refs/heads/master文件，内容变成了0d5c5bad0ae28006fe290905401ecd412bea58ea

查看文件会发现文件内容变回了[0d5c5bad0ae28006fe290905401ecd412bea58ea 新增World.java文件] 这次提交后的内容



取消回退操作：

找到最新的commit id 

git log --pretty=oneline(git log也可以)



// 这一部分是在ubuntu上操作的，呵呵呵

比较工作区中的文件与仓库中文件的区别

git diff HEAD Hello.java

将最后一次提交的文件与工作区中的文件对比（HEAD指向最后一次提交）



恢复文件操作：

修改Hello.java，但是没有做git add

git checkout –Hello.java

恢复到上一次提交之后的状态



修改Hello.java ，并且执行了git add

git reset HEAD Hello.java

把暂存区的文件恢复到工作区

git checkout –Hello.java

恢复到上一次提交之后的状态



删除文件

rm Hello.java

git commit -a -m “删除Hello.java”



恢复删除文件

git reset --hard 6b67a25 //  6b67a25是提交删除Hello.java之前的commit id



远程操作



git远程地址：https://github.com/ietown/mypro_remote.git



1.将本地仓库于远程地址关联起来

git remote add origin https://github.com/ietown/mypro_remote.git // 貌似是把url赋值给origin



2.将内容推送到远程仓库（github）

git push -u origin master

将所有文件从本地master分支推送到origin上，-u表示将远程master于本地master关联



3.切换远程地址

先再次新增一个远程关联

git remote add test https://github.com/ietown/mypro_remote.git

执行：git remote 显示

origin

test

git remote set-url origin https://github.com/ietown/mypro_remote.git



4.查看远程仓库

git remote -v

显示：

origin https://github.com/ietown/mypro_remote.git (fetch)

origin https://github.com/ietown/mypro_remote.git (push)

test https://github.com/ietown/mypro_remote.git (fetch)

test https://github.com/ietown/mypro_remote.git (push)



4.删除远程仓库

删除test远程仓库

git remote rm test



5.修改文件

修改Hello.java和World.java

git commit -a -m "先提交修改的2个文件，之后会提交到github上" // 增加到本地仓库

git push origin master

显示：

Username for 'https://github.com': ietown

Password for 'https://ietown@github.com': 

Counting objects: 7, done.

Delta compression using up to 4 threads.

Compressing objects: 100% (4/4), done.

Writing objects: 100% (4/4), 547 bytes | 0 bytes/s, done.

Total 4 (delta 2), reused 0 (delta 0)

To https://github.com/ietown/mypro_remote.git

   6b67a25..98db940  master -> master



克隆仓库（拉取远程代码，正常的项目操作）

1.在github上建立远程respository，要选取初始化，建立README文件

2.本地git clone https://github.com/ietown/mypro_remote_bak.git

3.写完文件后先提交本地，然后提交到远程

git add

git commit

git push origin master



分支操作

1.创建分之

git branch bro

2.查看分支

执行：git branch

查看：

  brh

* master // 指针指向master

3.切换分支

git checkout brh

* brh

  master

4.删除分支

git branch -d brh

5.创建并且切换到刚创建的分支

git checkout -b brh



6.分支操作

修改Hello.java文件

git status 显示如下

On branch brh // 这里是brh了，以前是master

Changes not staged for commit:

  (use "git add <file>..." to update what will be committed)

  (use "git checkout -- <file>..." to discard changes in working directory)



modified:   Hello.java



no changes added to commit (use "git add" and/or "git commit -a")



执行 git commit -a -m “” 提交修改 // 这里很重要，不过不提交，那么切换到master分支后，master分支也会显示修改过这个文件，因为文件的修改没有进入仓库，而是留在工作区



然后在切换到master分支

查看状态：

On branch master

Your branch is up-to-date with 'origin/master'.

nothing to commit, working directory clean

内容没有变化

查看Hello.java文件，内容也是在brh分支上修改之前的内容

这说明，git的分支之间是独立的



把brh分支提交到github

git push origin brh

查看：

Counting objects: 3, done.

Delta compression using up to 4 threads.

Compressing objects: 100% (3/3), done.

Writing objects: 100% (3/3), 355 bytes | 0 bytes/s, done.

Total 3 (delta 2), reused 0 (delta 0)

To https://github.com/ietown/mypro_remote.git

 * [new branch]      brh -> brh



再去github上查看，会看到2个分支



合并分支

最终发布的版本一定是在master分支上，所以发布前需要讲brh与master分支合并（合并到master分支）

先切换到主分支

执行git merge brh

显示

Updating 3e385a1..0927e7d

Fast-forward

 Hello.java | 2 ++

 1 file changed, 2 insertions(+)

Fast-forward：快速合并，不会产生新的commit id，只是利用合并子分支的commit id（head指向master,master执行brh的最新commit id）



