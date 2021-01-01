### 简介

该框架是采用微软的 `playwright` 包编写的自动化引擎，另外一个 `titans` 框架所
使用的 `Selenium` 包编写的自动化将废弃，之后采用这个引擎为主。

#### 为什么废弃 `Selenium` 采用 `playwright` ?

`Selenium` 是个非常不错的浏览器操作包，但是这个包在我在实际生产中却出现过许多浏览器
没有释放的问题，导致机器内存泄漏。然而这些问题一直都是存在的，在集群环境中更是致命。
然后采用 `playwright` 的原因也很简单。这个有大厂进行支持，保证能够对问题进行修复。然后
`chrome` 浏览器也是微软出品的，所以对于如何避免内存泄漏，操作浏览器根据高效，这个应该
是有非常丰富的经验。

### 部署

```shell

# 安装框架依赖包 
pip install -r requirements.txt

# 安装浏览器 Playwright requires Python 3.7+
python -m playwright install

```
