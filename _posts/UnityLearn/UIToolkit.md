---
layout:     post   				    # 使用的布局（不需要改）
title:      UIToolkit 				# 标题 
subtitle:   Hello World, Hello Blog #副标题
date:       2024-05 				# 时间
author:     KS 						# 作者
header-img: img/post-bg-2015.jpg 	#这篇文章标题背景图片
catalog: true 						# 是否归档
tags:								#标签
    - Unity Learn
---

### UIToolkit
- 工作流：借鉴Web开发工作流
    - UXML：内容和布局，设计各个不同UI控件的包含关系
    - USS：样式设计，作为可复用的外联样式（相对于内联样式）
    - C#脚本：功能行为
    - UIDocument组件：GameObject通过组件关联对应的UI文件
- 优点：
    - 标准化UI开发工作流
    - Flexbox系统，轻松实现UI自动适配
    - USS样式表，让UI样式的修改更为便捷
    - 高性能：远远高于UGUI
- UQuery：查找元素处理，类似项目的GetUIObject根据控件名获取控件对象
    - Query：查找多个元素
    - Q：查找首个元素，等价于Query.First()的处理
    - Query.AtIndex(i)：从Query获取的多个元素中查找索引为i下的元素
- 模板容器：可复用的UI资产
    - 创建流程：选中UXML中UI元素右键创建模板，保存为UXML文件（子UI的概念）
    - 应用场景：将UI中可复用的元素抽出来作为模板来使用，类似目前UI组件化框架中将默认不加载控件升级为预制体的处理
- 自定义控件（Custom controls）：
    - 通过继承VisualElement + 编码模板
    - 应用场景：配合模板容器，在自定义控件的初始化函数中创建已有的模板容器
- Scriptable Object
    - 作用：可复用的数据资产，充当数据容器，可独立存储大量数据，可以理解为我们的导表、Model/VM，先声明数据结构，再创建数据实例（运行时对象或离线创建的assert文件）
    - 编辑器操作：继承ScriptableObject并应用特性[CreateAssetMenu]来支持在编辑器中通过右键菜单栏创建对应的数据实例并存储为.asset文件
    - 应用场景
        - 导表：先声明导表数据结构，通过创建.asset文件来填写导表数据，但每次只能填写一个数据实例对象（可以理解为1行数据），除非表结构设计成可管理全量导表数据
        - Model/VM：通过运行时创建数据实例对象来支撑业务逻辑，且比较方便支持序列化（运行时数据保存为.asset文件）
- Excel导入导出：
    - 背景：ScriptableObject编辑大量数据成本较高
    - 流程：创建Excel->编辑数据->保存为csv->C#脚本中在OnValidate（只在编辑器中生效，游戏运行时不生效，一般用于在编辑器中提供即时的反馈）->加载csv文件数据并解析->填充至序列化字段数据中（最终编辑器中呈现的是列表）
    - 思考：利用Excel二维表的编辑优势并搭建数据源自动(半自动)同步至编辑器的处理流程
- UI交互处理
    - Manipulator操纵器：细颗粒度的交互行为处理，代码复杂度会高一点，但能确保不同交互类型的职责单一
        - 激活过滤器：ManipulatorActivationFilter，可设置交互类型，例如鼠标左键点击还是右键点击（button）、点击次数（clickcount）、修饰键（modifiers）
    - Event事件系统：粗颗粒度的交互行为处理，代码更简单，但一般会将所有处理都放到同一个函数中（除非业务方主动去拆分优化）
- 问题和思考
    - 【问题】编写C#脚本时需要频繁切换UIBuilder复制粘贴控件名，每次Unity切换到前台就会走脚本reload的逻辑，会卡一会体验不是太好
    - 【问题】纯字符串层面的操作控件对象，开发过程中容易出错，也增加后续UI的维护成本
    - 【思考】UIToolkit中可以在UXML中使用相同命名的UI元素，在特定场景下能改善（精简）已有的业务代码写法（我们一般在代码中需要对控件名增加编号后缀代码中使用拼接字符串处理来操作具体控件）
    - 【问题】数据拆分颗粒度较细，基于可视化配置来设计关联，对于查找引用关系需要编辑器提供比较好的支持才行，否则对开发而言是带来额外维护成本；

### 参考资料
- 资源来源：
    - 背景图：opengameart.org
    - UI资源：gameart2d.com
    - 字体下载：fonts.net.cn
