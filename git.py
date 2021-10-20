# 新建目录
git init #初始化git本地仓库

git remote add origin https://gitee.com/neu-shouliang-qi/ssl-algorithm.git # 当提示error: remote origin already exists.，先删除 git remote rm origin

git pull origin master  # pull到本地仓库

# 加文件到新建文件夹

# 保存所有/指定文件到缓存区
git add . # 添加所有文件
git add + 文件名  

git commit -m "初始化"    # 添加文件描述

git push origin master  #将本地仓库推送到远程仓库

