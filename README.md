# 将豆瓣电影和读书同步到Notion
> 基于[malinkang/douban2notion](https://github.com/malinkang/douban2notion)项目

本项目通过Github Action每天定时同步豆瓣电影和读书到Notion，并生成热力图展示您的观影和阅读习惯。


## 功能特点

- 自动同步豆瓣「想看/在看/看过」的电影到Notion数据库
- 自动同步豆瓣「想读/在读/读过」的图书到Notion数据库
- 记录评分、短评、观看/阅读日期等信息
- 支持电影分类、导演、演员信息关联
- 支持图书作者、分类信息关联
- 生成年度热力图，直观展示您的观影和阅读习惯
- 通过GitHub Actions实现每日自动同步

## 环境变量配置

需要在GitHub仓库的Secrets中设置以下环境变量：

### 必需配置
- `NOTION_TOKEN`: Notion API密钥
- `NOTION_MOVIE_URL`: 电影数据库页面URL
- `NOTION_BOOK_URL`: 图书数据库页面URL
- `DOUBAN_NAME`: 豆瓣用户ID

### 可选配置
- `MOVIE_NOTION_TOKEN`: 电影数据库专用Notion TOKEN（如果与图书数据库分开）
- `BOOK_NOTION_TOKEN`: 图书数据库专用Notion TOKEN（如果与电影数据库分开）
- `AUTH_TOKEN`: 豆瓣认证Token（用于获取私有数据）
- `YEAR`: 热力图显示的年份（默认为当前年份）


