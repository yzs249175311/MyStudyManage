<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgff8ce7d">1. 文件</a>
<ul>
<li><a href="#org1897396">1.1. 前端</a></li>
<li><a href="#orgaa90711">1.2. 后端</a>
<ul>
<li><a href="#orgf958068">1.2.1. </a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#orgebae6fc">2. 流程</a>
<ul>
<li><a href="#org9b50d7c">2.1. 前端</a>
<ul>
<li><a href="#org6b477cc">2.1.1. 添加一个主模块</a></li>
<li><a href="#orgaf1d0e3">2.1.2. 将前端的数据传入后端</a></li>
</ul>
</li>
<li><a href="#orgbb0d546">2.2. 后端</a>
<ul>
<li><a href="#orgaede1f4">2.2.1. 接收前端传来的参数</a></li>
<li><a href="#orga382fc8">2.2.2. 调用数据库数据</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="orgff8ce7d"></a>

# 文件


<a id="org1897396"></a>

## 前端


<a id="orgaa90711"></a>

## 后端


<a id="orgf958068"></a>

### 


<a id="orgebae6fc"></a>

# 流程


<a id="org9b50d7c"></a>

## 前端


<a id="org6b477cc"></a>

### 添加一个主模块

1.  第一步:在menu.xml和menu<sub>module.xml文件中添加Node元素,并在ModuleConstants.as文件中添加相应变量</sub>

    -   右键项目——>属性——>flex模块——>把主模块\*\*\*\*<sub>MainModule.mxml文件添加进去</sub>
    
    ![img](image/添加模块.png)

2.  第二步:修改项目中raw文件夹中的ClientUI.fla

    -   ClientUI.fla文件中button的类型为SimpleButton。
    
    -   button的名字"\_"(下划线)后面的书在要与menu.xml文件中Node元素的id相对应。
    
    -   注意:Clientui.fla文件修改完成后要导出成\*.swf和\*.swc文件,并同\*.fla文件一同放回项目中。

3.  第三步:创建主模块和子模块

    主模块(例):
    \\#+BEGIN<sub>SRC</sub>:
    public function initSubModule():{
        addModule(ModuleConstants.MyCustom<sub>MODULE</sub><sub>022002</sub>, new MyCustom()); //将子模块与Node对应起来
        addModule(ModuleConstants.MyCustom<sub>MODULE</sub><sub>022001</sub>, new MyCustom<sub>step1</sub>());
        addModule(ModuleConstants.MyCustom<sub>MODULE</sub><sub>022003</sub>, new MyCustom<sub>step3</sub>());		
    }
    \\#+END<sub>SRC</sub>


<a id="orgaf1d0e3"></a>

### 将前端的数据传入后端

-   调用方法DoSerViceUtil.doService()
-   最后一个参数reqUrl 应该为sysconfig.xml文件中name为CONTEXT<sub>URL元素的中的元素的name</sub>
-   报文需要在iprocess.xml文件中配置


<a id="orgbb0d546"></a>

## 后端


<a id="orgaede1f4"></a>

### 接收前端传来的参数

1.  写相应的Controller文件

    -   @autowired:自动加载
    
    -   @RequestMapping(value = ""):映射相应的报文,value对应的为前端DoServiceUtil.doService()第一个参数
    -   @ResponseBody


<a id="orga382fc8"></a>

### 调用数据库数据

1.  1.完成xxxDao.java和xxxDao.xml文件,以及xxxInf.java文件

2.  2.完成xxxService.java和xxxServiceImpl.java文件

3.  3.在mybatis-config-hdcctptran.xml中配置xxxInf.java文件的别名

4.  4.xxxController.java文件中自动加载xxxService,并调用相关方法。

5.  注意:

    -   xxxService.java文件中要自动加载xxxDao类(即添加注解@autowired)
    -   xxxDao.xml文件中parameterType的值为xxxDao.java中对应方法的的参数类型,resultType的值为对应方法返回值list<>泛型中的类型,一般为 xxxInf。

